from gpiozero import LED
from time import sleep
from signal import pause

led1 = LED(27)
led2 = LED(22)

# led = LED("GPIO27")   # 給 GPIO 腳位，跟上一行意義相同！
#led1 = LED("J8:13")    # 定義為樹莓派的腳位

while True:
  led1.on()
  sleep(0.5)
  led2.off()
  sleep(1)
  led2.on()
  sleep(0.5)
  led1.off()
  sleep(1)
pause()