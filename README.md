# Trading-with-Machine-Learning
Startup

1. Create a virtual environment conda create -n trader python=3.10
2. Activate it conda activate trader
3. Install initial deps pip install lumibot timedelta alpaca-trade-api
4. Install transformers and friends pip install torch torchvision torchaudio transformers
5. Update the API_KEY and API_SECRET with values from your Alpaca account
6.Run the bot python tradingbot.py

N.B. Torch installation instructions will vary depending on your operating system and hardware. See here for more: https://github.com/nicknochnack/MLTradingBot/blob/main/pytorch.org

If you're getting an SSL error when you attempt to call out to the Alpaca Trading api, you'll need to install the required SSL certificates into your machine.

Download the following intermediate SSL Certificates, these are required to communicate with Alpaca
https://letsencrypt.org/certs/lets-encrypt-r3.pem
https://letsencrypt.org/certs/isrg-root-x1-cross-signed.pem
Once downloaded, change the file extension of each file to .cer
Double click the file and run through the wizard to install it, use all of the default selections.
