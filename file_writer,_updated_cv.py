# -*- coding: utf-8 -*-
import sys
import MAAIN

sys.run('updated_data.csv' < 'data.csv')
file=sys.argv[1]
with open(file) as f:
  csv=f.readlines()

with open('updated_data.csv','a') as f:
    for i in csv:
      f.write(i)

if len(csv)>=50:
  MAAIN.algo()