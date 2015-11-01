#!/usr/bin/env python
""" Script to quickly parse cable modem pages and return the data in json """
__author__ = 'qry3vavna'
__version__ = '0.1'

from itertools import izip
import json
from lxml import html
import requests

def fetch(site):
  cable = []
  url = 'http://192.168.100.1/' + site + '.htm'
  get = requests.get(url)
  tree = html.fromstring(get.text)
  tds = tree.xpath('//td//text()')
  i = iter(tds)
  if 'Logs' in site:
      for log in izip(i,i,i,i):
        cable.append(log)
  elif 'Help' in site:
      for n in range(7):
          cable.append(tds[n].strip().split(':'))
  else:
      cable.append(dict(izip(i,i)))
  return cable


if __name__ == '__main__':
  cable_modem = []
  cable_res = {}
  pages = ['indexData', 'cmAddressData' , 'cmLogsData', 'cmHelpData']
  for page in pages:
      cable_res = {page:fetch(page)}
      cable_modem.append(dict(cable_res))

  print(json.dumps(cable_modem))
