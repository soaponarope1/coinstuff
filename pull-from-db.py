#!/usr/local/bin/python3.6

# import our modules
import time
import pymongo
import sys
import csv

# connect to the database and collection
mongoclient = pymongo.MongoClient('localhost', 27017)
db = mongoclient.hist_data
collection = db.historical

# define variables we will use
validSymbolList = ['BTCUSDT' ,'ETHUSDT' ,'ETHBTC', 'XRPUSDT', 'XRPBTC', 'BCCUSDT', 'BCCBTC', 'EOSUSDT', 'EOSBTC', 'XLMUSDT', 'XLMBTC', 'LTCUSDT', 'LTCBTC']
field_names = ['Open Price', 'High Price', 'Low Price', 'Volume', 'Close Time']

# function to pull data from db
def pullData ( symbol ):
	print ('Pulling data for: ' + symbol)
	#time.sleep(5)
	coin_data = collection.find({"ID": symb},{"openPrice":1,"highPrice":1,"lowPrice":1,"volume":1,"closeTime":1})
	with open('%s.csv' % symbol, 'w', newline = '') as f_output:
		csv_output = csv.writer(f_output)
		csv_output.writerow(field_names)
		
		for coin in coin_data:
			csv_output.writerow(
				[
				str(coin['openPrice']),
				str(coin['highPrice']),
				str(coin['lowPrice']),
				str(coin['volume']),
				str(coin['closeTime'])
				])
	print('Done pulling data. Output file \"%s.csv created\"' % symbol)

# take our arguments
if len(sys.argv) <= 1:
	print('Please enter a symbol \"pull-from-db BTCUSDT\"')
	exit(1)
symb = sys.argv[1]

# see if supplied argument is valid
if any(sym in symb for sym in validSymbolList):
	# if it is valid, pull our data
	pullData( symbol = symb )
else:
	symList = ','.join(map(str,validSymbolList))
	print('Invalid symbol \"' + symb + '\", please use one of the following: ' + symList)
	exit(1)
