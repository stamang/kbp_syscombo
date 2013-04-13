import sys, string, re,os, time, pickle, csv
from BeautifulSoup import BeautifulStoneSoup
sys.path.append('/Users/suzy/Desktop/slot-filler-validation_db/syscombo/')
from processfunctions import *

#read in query data
queryData = readquerydata()
keys = queryData[0]
values = queryData[1]
types = queryData[2]
nameid = {}
nameid = dict(zip(keys, values))
print nameid

#get candidate slots
query_slots = {}
query_slot_list = readqueryslottemplate()
keys = query_slot_list[0]
values = query_slot_list[1]
query_slots = dict(zip(keys, values))
print query_slots

#get answers








