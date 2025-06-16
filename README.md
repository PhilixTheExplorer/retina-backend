requirements.txt and Procfile are for railway config, not related with the model. But you may add extra in requirements.txt according to your needs in the model.

You can just go to your backend api to see server is running. Test with new url if you deploy your own backend server on railway (https://railway.com). This is my test deployment server in railway.

```bash
https://retina-backend-production.up.railway.app/
```

## Use Curl

From Command Prompt or Terminal, you can run this to test predict api

```bash
curl -X POST -F "file=@cat.jpg" https://retina-backend-production.up.railway.app/predict
```
