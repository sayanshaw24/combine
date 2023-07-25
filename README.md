# combine.AI
Combining Microsoft's Bing Chat and Bing Image Creator capabilities to automate design creation.

<p align="center">
  <img alt="Light" src="./examples/xbox/0.jpeg" width="49%">
  <img alt="Dark" src="./examples/onnxruntime/0.jpeg" width="49%">
</p>
<sub>powered by Bing Chat, Bing Image Creator, and EdgeGPT</sub>

## About

**combine.AI** leverages cloud compute on Azure for lighting fast design powered by state-of-the-art machine learning models for text generation and image creation with ChatGPT and DALL-E using Microsoft's Bing Chat and Bing Image Creator.

As part of the 2023 Microsoft AI Platform Fix, Hack, Learn initiative, we plan to answer the question, "What strategies should we undertake to make the community aware of Azure being the best and most differentiated place for open source generative AI?" The answer lies within the question - spreading awareness of AI on Azure and its ingenuity. As a developer on [ONNXRuntime Extensions](https://github.com/microsoft/onnxruntime-extensions), I have received numerous requests of collaboration or simply messages from our internal teams regarding them finding a certain existing or potential new feature useful for one of their products. Upon asking a PM of ours why we do not post marketing videos alike those of Microsoft's Surface products that would spread awareness about the amazing work we are doing, I found out that AI Platform simply does not have a marketing team due to budget constraints and thereby the PMs handle all marketing. 

I could only imagine how much AI Platform and open source generative AI on Azure in general would grow if we properly marketed our work and wide variety of brilliant projects that could be useful to so many within and outside the company. Now, with combine.AI, we can stick to Satya's goal of doing more with less, and automate marketing and design by combining open-source tools such as EdgeGPT with Microsoft's Bing Chat and Bing Image Creator and deploying on Azure.

## Usage

### Collect cookies

1. Open Microsoft Edge and ensure you are logged into your Microsoft account.
2. Open [bing.com/chat](https://bing.com/chat)
3. If you see a chat feature, you are good to continue!
4. Install the Cookie-Editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
5. Go to [bing.com](https://bing.com)
6. Open the Cookie-Editor extension
7. Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard.)
8. Paste your cookies into a file `bing_cookies_*.json`.
   - NOTE: The **cookies file name MUST follow the regex pattern `bing_cookies_*.json`**, such that it can be recognized by internal cookie processing mechanisms.

### Run `create.py`

`python create.py --cookie-file "./bing_cookies_chat.json" --prompt "product to create design for"`

## Feedback

Have comments or questions? Please reach out to me on Teams or Outlook (alias: sayanshaw).
