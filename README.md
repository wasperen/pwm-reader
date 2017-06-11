# PWM Reader
This module provides a class that can read and derive
 * frequency
 * pulse width
 * duty cycle

from a Pulse Width Modulation (PWM) input on a GPIO of
a Raspberry Pi.

The code is taken from http://abyz.co.uk/rpi/pigpio/code/read_PWM_py.zip
and full credits should go to the original creator over there.

## example usage
```python
import time
import pigpio

PWM_GPIO = 4
RUN_TIME = 60.0
SAMPLE_TIME = 2.0

the_pi = pigpio.pi()

p = PWMReader(the_pi, PWM_GPIO)

start = time.time()

while (time.time() - start) < RUN_TIME:

    time.sleep(SAMPLE_TIME)

    f = p.frequency()
    pw = p.pulse_width()
    dc = p.duty_cycle()

    print("f={:.1f} pw={} dc={:.2f}".format(f, int(pw+0.5), dc))

p.cancel()

the_pi.stop()
```
