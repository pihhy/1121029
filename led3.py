from gpiozero import PWMLED
from time import sleep

led = PWMLED(27)

while True:
  led.value = 0
  sleep(0.5)
  led.value = 0.5
  sleep(0.5)
  led.value = 1
  sleep(0.5)