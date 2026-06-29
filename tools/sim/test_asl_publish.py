#!/usr/bin/env python3
import time
import cereal.messaging as messaging

pm = messaging.PubMaster(['advisorySpeedLimit'])

i: int     = 0
speed: int = 0

while True:
  msg = messaging.new_message('advisorySpeedLimit')
  msg.advisorySpeedLimit.speed = speed
  msg.valid = True
  msg.advisorySpeedLimit.valid = True
  pm.send('advisorySpeedLimit', msg)
  print("Sent advisorySpeedLimit =", speed)
  i += 1
  if i % 15 == 0:
      speed += 5
  if speed > 25:
      print("speed is at max, exiting...")
      exit()
  time.sleep(0.5)

