from setuptools import setup, find_packages

setup(
    name='jogovelha',
    version='0.1',
    description='Um pacote que executa um Jogo da Velha',
    install_requires=['numpy'],
    packages=find_packages()
)