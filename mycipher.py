#!/bin/bash

import sys

message = ""
shift = sys.argv[1]

for x in sys.stdin:
  message = message + x

#Removes punctuation.
newmessage = ""
count = 0
while message.isalpha() == False:
  if message[count].isalpha() == False:
    message = message.replace(message[count], "")
    count = 0
  else:
    count += 1

message = message.upper()
#Creating ceasar cipher.
for x in message:
  n = ord(x)
  for y in range(int(shift)):
    n += 1
    if n > 90:
      n = 65
  newmessage = newmessage + chr(n)
#Divides new message.
nm2 = newmessage[0:]
divide = []
while len(nm2) > 5:
  divide.append(nm2[0:5])
  nm2 = nm2[5:]
divide.append(nm2)

#Print cipher.
output = ""
for x in range(len(divide)):
  if (x % 10) == 0:
    print(output.strip())
    output = ""
  output += f' {divide[x]}'
print(output.strip())
