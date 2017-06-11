from distutils.core import setup

setup(
    name='pwm_reader',
    version='1.0',
    packages=[''],
    url='https://github.com/wasperen/pwm-reader.git',
    license='MIT',
    author='',
    author_email='pigpio@abyz.co.uk',
    install_requires=[
        'pigpio',
    ],
    description='Class to monitor a PWM signal and calculate the frequency, pulse width, and duty cycle.'
)
