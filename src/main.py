import neo
from machine import Pin
# from adafruit_led_animation.animation.blink import Blink
# import adafruit_led_animation.color as color

from src.adafruit_led_animation.animation.blink import Blink
from src.adafruit_led_animation.animation.comet import Comet
from src.adafruit_led_animation.animation.chase import Chase
from src.adafruit_led_animation.sequence import AnimationSequence
from src.adafruit_led_animation.color import PURPLE, AMBER, JADE

def start(env=None, requests=None, logger=None, time=None, updater=None):

  log = logger(append='main')
  log("Starting..")

  # Update to match the pin connected to your NeoPixels
  # pixel_pin = board.D6
  # Update to match the number of NeoPixels you have connected
  num_pixels = 100
  pixel_pin = 26
  pixels = neo.Pixel(Pin(pixel_pin, Pin.OUT), num_pixels)

  # pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

  blink = Blink(pixels, speed=0.5, color=JADE)
  comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
  # chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=AMBER)

  animations = AnimationSequence(blink, comet, advance_interval=2, auto_clear=True)

  while True:
    animations.animate()

# start()