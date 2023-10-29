from gpiozero import LED

led = LED(27)

while True:
  print("\n0) 關閉 LED 燈")
  print("1) 打開 LED 燈")
  print("2) 離開程式")
  light = input("你的選擇 (0|1|2): ")
  if light == "0":
      led.off()
  if light == "1":
      led.on()
  if light == "2":
      break