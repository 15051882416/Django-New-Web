"""
Django settings for django_01 project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(!az*nhv-51*ki2f*d1(#m+e(@03-cqy77gtmy=a++2=4@7&fl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # 调试开关，True是调试模式，Flase是关闭调试模式

# 两种方式在括号种加*，或者加入该服务器的地址
ALLOWED_HOSTS = ['127.0.0.1','47.93.8.105']
# ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.course',
    'apps.cms',
    'apps.news',
    'apps.payinfo',
    'apps.xfzauth',
    'rest_framework'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根目录的url路径设置
ROOT_URLCONF = 'django_01.urls'

from django.templatetags import static

# 模板设置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 会在当前项目下的‘templates’文件夹下寻找所有的文件
        'DIRS': [os.path.join (BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # auth中的user中有属性.is_authenticated可以判断该用户是否存在
                'django.contrib.messages.context_processors.messages',
            ],
            # 在setting文件中按照如下配置后，在后续的模板中就不用再加载静待模板。省去了所有文件中的这句代码‘{% load static%}’
            'builtins': ['django.templatetags.static'] # 模板内置标签
        },
    },
]

WSGI_APPLICATION = 'django_01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# 数据库信息配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'mydb',
        'USER':'root',
        'PASSWORD':'QAZwsx1992,.',
        'HOST':'127.0.0.1',
        'POST':'3306',

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# AUTH_USER_MODEL 这个属性时Django内置的，它会主动的到文件中来
# 查找这个属性，如果找到了，那么就会使用这个属性指定的模型来作为User对象
# AUTH_USER_MODEL 这个属性是一个字符串，它的规则是'appname.Modelname'
# 如果设置了AUTH_USER_MODEL ,那么项目的makemigrations以及migrate命令
# 必须要在设置（setting文件配置）完这些东西之后执行
AUTH_USER_MODEL = 'xfzauth.User'


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us' # 语言配置

TIME_ZONE = 'Asia/Shanghai' # 时区配置

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# 静态文件路径配置
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 同步到服务器部署时，关闭Debug模式，需要新建一个文件夹
# 用于收集所有的文件

# STATIC_ROOT = '/static_dist/' # 没有设置路径，会默认存放在根目录下
STATIC_ROOT = os.path.join(BASE_DIR,'static_dist')

# 存储文件路径配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# 七牛云相关的配置
QINIU_ACCESS_KEY = ''
QINIU_SECRET_KEY = ''
QINIU_BUCKET_NAME = ''
QINIU_DOMAIN = ''


# Ueditor编辑器配置
# 上传服务器配置
UEDITOR_UPLOAD_TO_SERVER = True
UEDITOR_UPLOAD_PATH = MEDIA_ROOT
UEDITOR_CONFIG_PATH = os.path.join(BASE_DIR,'static','ueditor','config.json')

# 上传七牛云配置
UEDITOR_QINIU_ACCESS_KEY = QINIU_ACCESS_KEY
UEDITOR_QINIU_SECRET_KEY = QINIU_SECRET_KEY
UEDITOR_QINIU_BUCKET_NAME = QINIU_BUCKET_NAME
UEDITOR_QINIU_DOMAIN = QINIU_DOMAIN
UEDITOR_UPLOAD_TO_QINIU = True

# 定义首页新闻一页展示多少条新闻
ONE_PAGE_NEWS_COUNT = 1

# 百度云的配置
# 控制台->用户中心->用户ID
BAIDU_CLOUD_USER_ID = ''
# 点播VOD->全局设置->发布设置->安全设置->UserKey
BAIDU_CLOUD_USER_KEY = ''