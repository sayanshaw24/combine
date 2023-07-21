# from EdgeGPT.EdgeUtils import Query, Cookie, ImageQuery
# from pathlib import Path

# # Clean images folder
# try:
#     shutil.rmtree("/bing_images")
# except OSError as e:
#     print("Error: %s - %s." % (e.filename, e.strerror))

# product = "onnxruntime"
# prompt = f"describe {product} without saying {product}"

# q = Query(
#   prompt,
#   style="creative",  # or: 'balanced', 'precise'
#   cookie_files=["./bing_cookies_chat.json"]
# )
# print(q)
# i = ImageQuery(
#   str(q),
#   cookie_files=["./bing_cookies_chat.json"]
# )
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from EdgeGPT.ImageGen import ImageGen

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageEnhance

import argparse
import json
import os
import sys
import shutil
import asyncio
import textwrap

import cv2
import numpy as np

async def chat(args, prompt):
    cookies = json.loads(open(args.cookie_file, encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative, simplify_response=True)
    #print(json.dumps(response, indent=2))
    output_text = response["text"]
    await bot.close()
    return output_text

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=70)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height

if __name__ == "__main__":
    # Clean images folder
    try:
        shutil.rmtree("./output")
    except OSError as e:
        print("NOTE - No output folder to clean: %s - %s." % (e.filename, e.strerror))

    parser = argparse.ArgumentParser()
    parser.add_argument("-U", help="Auth cookie from browser", type=str)
    parser.add_argument("--cookie-file", help="File containing auth cookie", type=str)
    parser.add_argument(
        "--prompt",
        help="Prompt to generate images for",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--output-dir",
        help="Output directory",
        type=str,
        default="./output",
    )
    parser.add_argument(
        "--quiet", help="Disable pipeline messages", action="store_true"
    )
    args = parser.parse_args()
    # Load auth cookie
    with open(args.cookie_file, encoding="utf-8") as file:
        cookie_json = json.load(file)
        for cookie in cookie_json:
            if cookie.get("name") == "_U":
                args.U = cookie.get("value")
                break

    if args.U is None:
        raise Exception("Could not find auth cookie")

    # Ask Chat
    while True:
        try:
            description = asyncio.run(chat(args, f"give me a 10 word generic description of {args.prompt} without saying {args.prompt}"))
            print(description + "\n")
            break
        except Exception as e:
            print(e)
            continue
    
    while True:
        try:
            features = asyncio.run(chat(args, f"what are the top 4 features of {args.prompt}"))
            print(features + "\n")
            # print(len(features))
            print("**************************************")
            break
        except Exception as e:
            print(e)
            continue

    while True:
        try:
            # Create image generator
            image_generator = ImageGen(args.U, args.quiet)
            image_generator.save_images(
                image_generator.get_images(description + "without text"),
                output_dir=args.output_dir,
            )
            break
        except Exception as e:
            print(e)
            continue

    for i in range(4):
        features = features[features.index("[")+10:]
        start = features.index("**: ")+3
        end = features.index("[")
        # print(f"\nStart: {start}\n")
        # print(f"End: {end}\n\n")
        feature = features[start:end]
        print(f"\nFeature {i+1}: " + feature + "\n")

        img = Image.open(f"./output/{i}.jpeg")

        #image brightness enhancer
        enhancer = ImageEnhance.Brightness(img)
        factor = 0.5 # darkens the image
        img = enhancer.enhance(factor)

        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("SEGOEUI.TTF", 24)
        # draw.text((x, y),"Sample Text",(r,g,b))
        # draw.text((102, 512),feature,(255,255,255),font=font)
        draw_multiple_line_text(img, feature, font, (255,255,255), 400)
        img.save(f"./output/{i}.jpeg")