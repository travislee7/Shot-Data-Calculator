import csv
from itertools import islice
from calculate import calculate

rawData = open('shots_data.csv')
shotData = csv.reader(rawData)

teamA = list(islice(shotData, 1, 281))          #separate Team A's shot data from Team B's
teamB = list(shotData)

travis = calculate(teamA, teamB)                #create a class where calculations are done
travis.allShots()
travis.twoShotCalculation()
travis.ncThreeShotCalculation()
travis.cThreeShotCalculation()
travis.printData()

