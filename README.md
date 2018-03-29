django-rules-guardian-sample
====

Overview

## Description

・django-rules django-guardian 併用時のサンプルコードです。

紹介記事：[[Python] Djangoで行レベルのアクセス制限をかける](https://qiita.com/okoppe8/items/dbbf363ec2b1329f1bf7)

## Usage

Windows 

```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py migrate
manage.py createsuperuser 
manage.py runserver
```

Open URL http://localhost:8000
