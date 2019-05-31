# Python Google OAuth  And Download Playlist

**ÖNEMLİ!** Tamamen bilgi amaçlıdır uygulamanızı kesinlikle tavsiye etmiyorum. 
Google hesabınızın var olduğu buna bağlı bir youtube'da bir playlist'inizin olduğu ve sisteminizde python ve pip kurulu olduğunu varsayıyorum.  Public bir playlist için username pass boş geçebilirsiniz 

**IMPORTANT!** I definitely don't recommend it. For information purposes only.


# Auth Credentials

Öncelikle [Google Credentials](https://console.developers.google.com/apis/credentials) ile bir OAuth istemci kimliği oluşturuyoruz.  Oluşturduğumuz kimliği JSON formatında indiriyoruz. İndirdiğiniz json kaynağını secret.json olarak yeniden adlandırıp proje dizinine kaydedinin.

![imagem](https://user-images.githubusercontent.com/12594797/58480349-de6d6480-8162-11e9-8fce-9e46f351e3cf.png)

![caps3](https://user-images.githubusercontent.com/12594797/58702708-36001000-83af-11e9-9062-802b5798d4a7.png)


## Install Pip Packages

```
$ pip install google-api-python-client 
$ pip install youtube_dl
$ pip install google-auth-oauthlib
$ pip install ffmpeg-python

```

## Install ffmpeg
 [Ffmpeg Download](https://ffmpeg.org/download.html) adresinden yükleyip kurun.  **bin** dizinini ortam değişkenlerine path tanımlamayı unutmayın.
 
 ![caps1](https://user-images.githubusercontent.com/12594797/58702399-61362f80-83ae-11e9-879a-bb23064bda09.png)

## Run Python
```
$ python  yapis.py
```