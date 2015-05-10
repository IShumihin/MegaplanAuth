from setuptools import setup, find_packages

setup(
    name='MegaplanAuth',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['hashlib', 'hmac', 'simplejson'],
    url='',
    license='',
    author='shuma',
    author_email='shmikhin.ivan@yandex.ru',
    description='Django auth from megaplan'
)
