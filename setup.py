from distutils.core import setup

REQUIRES = [
    'requests',
    'structlog',
    'curlify',
    'allure-pytest'
]
setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/NadezhdaDudnik/restclient.git',
    license='MIT',
    author='Nadezhda Dudnik',
    author_email='-',
    install_requires=REQUIRES,
    description='restclient with allure and logger'
)
