import ctypes
import io
import os
import sys
import math
import subprocess

ALPHABET = \
  ".0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"#0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
charLen = len(ALPHABET)

def encode (n):
  try:
    return ALPHABET [n]
  except IndexError:
    raise Exception ("cannot encode: %s" % n)

def dec_to_base (dec = 0, base = charLen):
  if dec < base:
    return encode (dec)
  else:
    return dec_to_base (dec // base, base) + encode (dec % base)

def decode (s):
    try:
        return ALPHABET.index(s)
    except ValueError:
        raise Exception ("cannot decode: %s" % s)

def base_to_dec (s, base = charLen, pow = 0):
    if s is "":
        return 0
    else:
        return decode (s[-1]) * (base ** pow) + base_to_dec (s[0:-1], base, pow + 1)
        
start = '000000'

lastCount = base_to_dec(startPass)

while True:
	now = dec_to_base(lastCount)
    print("count=>",lastCount," str=>",now)
	if start=='ZZZZZZ':
    	break
    lastCount+=1
