# Trading-with-Machine-Learning
Startup

1. Create a virtual environment ``conda create -n trader python=3.10``
2. Activate it ``conda activate trader``
3. Install initial deps ``pip install lumibot time delta alpaca-trade-API``
4. Install transformers and friends ``pip install torch torch-vision torch audio transformers. ``
5. Update the ``API_KEY`` and ``API_SECRET`` with values from your Alpaca account
6. Run the bot ``python tradingbot.py``

If you get an SSL error when you attempt to call out to the Alpaca Trading API, you'll need to install the required SSL certificates into your machine.

1. Download the following intermediate SSL Certificates; these are required to communicate with Alpaca
- https://letsencrypt.org/certs/lets-encrypt-r3.pem
- https://letsencrypt.org/certs/isrg-root-x1-cross-signed.pem
2. Once downloaded, change the file extension of each file to ``.cer``
3. Double click the file and run through the wizard to install it, use all of the default selections.
