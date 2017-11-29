#!/usr/bin/python
# -*- coding: utf-8 -*-
#======================================================================#
#                          Christianah Adigun                          #
#                          adigu002@d.umn.edu                          #

#          EVALUATING MY NOT-SO-CRAPTOGRAPHIC HASH FUNCTION            #

# This program reads hexadecimal values from a file line by line and   #
#        performs given analysis on the inputs.                        #
#======================================================================#

import sys, csv, math
def evaluate(filename):
    # Empty lists to store computations from hex Values 
    allValues = list()
    origValues = list()
    modValues = list()
    origBinValues = list()
    modBinValues = list()
    avgCols = list('00000000000000000000000000000000')
    avgOrigCols = list('00000000000000000000000000000000')
    differences = list()
    # Variables for average ratio of digests
    avgDigest = 0
    avgOrigDigest = 0
    cout = 0

    # Computation of values
    with open(filename, 'r') as f:
        for line in f.readlines():
            cout += 1
            allValues.append(str(line)[0:8])
            digest = str(line)[0:10]
            thisDigest = bin(int(digest,16)).replace('0b', '').zfill(32)
            # Compute average for a specific digest in orig/n or mod/n
            avgDigest += (thisDigest.count('1')/32.0)
            for i in range(0, 32):
                # counter of 1s in each column of digest
                if (thisDigest[i] == '1'):
                    avgCols[i] = int(avgCols[i]) + 1
            
            if cout % 2 != 0 :
                origValues.append(str(line)[0:8]) # Store orig/n file hex value in list
                origBinValues.append(thisDigest) # Store orig/n file binary value in list
                # Compute average for a specific digest in orig/n
                avgOrigDigest += (thisDigest.count('1')/32.0)
                for i in range(0, 32):
                    if (thisDigest[i] == '1'):
                        avgOrigCols[i] = int(avgOrigCols[i]) + 1

            else:
                modValues.append(str(line)[0:8]) # Store mod/n file hex value in list
                modBinValues.append(thisDigest) # Store mod/n file binary value in list

    percentCol = 100 - (len(set(allValues)) * 100.0 / len(allValues))
    avgDigOnes = avgDigest / len(allValues)
    avgOrigDigest = avgOrigDigest / len(origValues)

    for i in range (0, 32):
        avgCols[i] = avgCols[i] / float(len(allValues)) * 100
        avgCols[i] = "{0:.2f}".format(avgCols[i])

    for i in range (0, 32):
        avgOrigCols[i] = avgOrigCols[i] / float(len(origValues)) * 100
        avgOrigCols[i] = "{0:.2f}".format(avgOrigCols[i])

    for i in range (0, len(origBinValues)):
        diff = int(origBinValues[i],2) ^ int(modBinValues[i],2)
        x = '{0:b}'.format(diff)
        differences.append(x.count('1'))

    # Write values of differences to CSV file
    with open('differences.csv', 'wb') as csvfile:
        csvWriter = csv.writer(csvfile, dialect='excel')
        for i in range (0, len(differences)):
            Col = [0]
            Col[0] = differences[i]
            csvWriter.writerow(Col)

    # Write values of average ratio of 1s in Columns to CSV file
    with open('columns.csv', 'wb') as csvfile:
        csvWriter = csv.writer(csvfile, dialect='excel')
        for i in range (0, len(avgOrigCols)):
            Col = [0]
            Col[0] = avgOrigCols[i]
            csvWriter.writerow(Col)

    # Information Entropy Calculation
    probabilityOrig = 1 / float(len(set(origValues)))
    entropyOrig = (probabilityOrig) * math.log((1/probabilityOrig), 2) * len(origValues)
    probabilityAll = 1 / float(len(set(allValues)))
    entropyAll = (probabilityAll) * math.log((1/probabilityAll), 2) * len(allValues)    

    # Display Results
    print "1. The number of unique digest values\n"
    print "\to Total number of Unique Digests in orig/n: {}\n".format(len(set(origValues)))
    print "\to Total number of Unique Digests in mod/n: {}\n".format(len(set(modValues)))
    print "\to Total number of all Unique Digests: {}\n".format(len(set(allValues)))
    print "\to Percentage rate of Collision: {}%\n".format(percentCol)
    print "2. The average ratio of 1s to 0s in digests\n"
    print "\to Average ratio of 1s to 0s in all digests: {}\n".format(avgDigOnes)
    print "\to Average ratio of 1s to 0s in orig/n digests: {}\n".format(avgOrigDigest)
    print "3. Average ratio of 1s to 0s in columns(left to right)\n"
    print "\tThe ratio of 1s to 0s based on the orig/ input: {}\n".format(avgOrigCols)
    print "\tThe ratio of 1s to 0s based on the orig/ and mod/ input: {}\n".format(avgCols)
    print "4. Average difference between paired orig/n and mod/n entries: \n"
    print "\t{}\n".format(differences)
    print "5. The information entropy across digests\n"
    print "\to The information entropy across digests in orig/n: {}\n".format(entropyOrig)
    print "\to The information entropy across all digests: {}\n".format(entropyAll)

evaluate(sys.argv[1])
