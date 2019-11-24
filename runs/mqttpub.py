import paho.mqtt.client as mqtt
from subprocess import Popen
import re
import sys
import time
import fileinput
import argparse

def main():

  parser = argparse.ArgumentParser(description='OpenWB MQTT Publisher')
  parser.add_argument('--qos', '-q', metavar='qos', type=int, help='The QOS setting', default=0)
  parser.add_argument('--retain', '-r', dest='retain', action='store_true', help='If true, retain this publish')
  parser.set_defaults(retain=False)

  args = parser.parse_args()

  client = mqtt.Client()
  client.connect("localhost")

  for line in sys.stdin:
    m = re.match('(.*)=(.*)', line)
    if m:
      #print("Publishing '%s' :: '%s'" % (m.group(1), m.group(2)))
      client.publish(m.group(1), payload=m.group(2), qos=args.qos, retain=args.retain)

  client.loop(timeout=2.0)

if __name__ == "__main__":
    main()
