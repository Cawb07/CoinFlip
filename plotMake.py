from __future__ import division
#import os, popen2 # I commented this out because the popen2
#################### libraries are depreciated
import sys
import random
import numpy
import matplotlib.pyplot as plt

#Here are the variables you will want to change
numberOfCoins = 10000
numberOfRepetitions = 10000 #how many times to repeat the experiment
binIncrement = 0.01


#here is some setup stuff you don't have to worry about but might want to use
heads = 1
tails = 0

#here is a list for storing all our final outcomes
#we're defining a macrostate by the fraction of heads
forBinning = [] #where to store all the results

currState = 0
for i in range (0,numberOfRepetitions):
    orderParam = 0 
    #The order parameter is the sum of of the heads and tails 
    #50 heads followed by 50 tails = 50 tails followed by 50 heads
    #all heads --> orderParam = numberOfCoins * heads = numberOfCoins, heads = 1
    #all tails --> orderParam = numberOfCoins * tails = 0, tails  = 0
    #50% heads --> orderParam =  (numberOfCoins * tails)/2 = numberOfCoins/2
    
    for j in range (0, numberOfCoins):
        randomNumber =  random.random() #Random number between 0 and 1.  
        
############################## MY CHANGES ########################################        
        #If it's less than 0.5 then it's heads, more is tails
        ###################################### START EDIT HERE, A
        # Here goes an if else statement determine the value of a parameter called "currState"
        # basically it should either be heads or tails (use the heads/tails variables above)
        # as well as the value of randomNumber
        ##################################### END EDIT HERE, A
        if randomNumber < 0.5:
            currState = 1
        else:
            currState = 0
            
        # print ("The current state is ", currState, ".")
##################################################################################


############################## MY CHANGES ########################################
        ####################################### START EDIT HERE, B
        # here goes something where you add some number to the orderParam.  You'll have to use the currState that you defined above.
        ####################################### END EDIT HERE, B
        if currState == 1:
            orderParam += 1
##################################################################################

    fractionHeads = orderParam/numberOfCoins #number of coins that came up heads
    percentHeads = fractionHeads * 100
    #print percentHeads
    forBinning.append(fractionHeads)

#sort your data for easier binning
forBinning = sorted(forBinning)

#set up the histograms
histogram = [] #make an empty list
i = -binIncrement/2 #leftmost part of "window"
j = 0 #for array indexing
while i < 1.0 + binIncrement/2:  #clear out the histogram
    histogram.append(0) #add a bunch of zeroes
    #print "The left bin coordinate is", i, ".", "The histogram value is ", histogram[j], "."
    i = i + binIncrement #this is the next bin's leftmost part of the window
    j = j + 1 #the next index

jmax = j - 1 # the number of "bins"

currBinMax = binIncrement/2  # Because we want the first bin to be centered at 0
############################## this is the "rightmost" part of the bin.
#since our data is sorted, anything less than the first bin will be in the very beginning of our sorted data
#and then the next chunk will be for the second, etc...
j = 0 #index for the bins
i = 0 #index for the coinflip tries
#here we are taking all our "Tries" and putting it in the appropriate bin (fraction of heads or tails)
for j in range (0,jmax):  
    while i < numberOfRepetitions and forBinning[i] < currBinMax:
        histogram[j] = histogram[j] + 1
        i = i + 1
    currBinMax = currBinMax + binIncrement
#print forBinning
#print histogram


###################### MY CHANGES ##########################################################################
#normalize, the integral under should = 1
################################### START EDIT HERE, C
#You need to come up with the normalizationFactor.  Note, that the integral under the curve should equal 1.  Because the probability of being in SOME state should be 1.
#use the "rectangle method" (no need to get fancy with trapezoids).
#you'll need to use the total number of trials (i.e. numberOfReptitions) and the binIncrement (width of your bin) variables.
#normalizationFactor = ?
################################### END EDIT HERE, C
normalizationFactor = binIncrement*numpy.sum(histogram)
print "The area under the curve is", normalizationFactor, "."
print "\n"
############################################################################################################


normalized = []
#This is what actually gets printed out in the end.  
#Two column data, first column is the fraction of heads (our order parameter), second column is the probability of observing that fraction of heads
for i in range (0, len(histogram)):
    normalized.append(histogram[i]/normalizationFactor)
    #integral = integral + ? # use this if you like to check your normalization 
    #print "For", binIncrement*i*100, "percent of the coins land heads, the probability is", normalized[i]
    print "\n"

print normalized
print "The length of this array is", len(normalized)
normalizedArea = binIncrement*numpy.sum(normalized)
print "The area under the normalized curve is", normalizedArea
print "\n"

print "The number of bins is", jmax

pos = numpy.arange(jmax+1)
pos = pos/100
print pos

plt.bar(pos, normalized, binIncrement, color='g', alpha = 0.25)
plt.xlabel('Percent Coins Landed Heads')
plt.ylabel('Probability')
plt.title('CoinFlip Histogram')


#Here are the variables you will want to change
numberOfCoins = 1000
numberOfRepetitions = 10000 #how many times to repeat the experiment
binIncrement = 0.01


#here is some setup stuff you don't have to worry about but might want to use
heads = 1
tails = 0

#here is a list for storing all our final outcomes
#we're defining a macrostate by the fraction of heads
forBinning = [] #where to store all the results

currState = 0
for i in range (0,numberOfRepetitions):
    orderParam = 0 
    #The order parameter is the sum of of the heads and tails 
    #50 heads followed by 50 tails = 50 tails followed by 50 heads
    #all heads --> orderParam = numberOfCoins * heads = numberOfCoins, heads = 1
    #all tails --> orderParam = numberOfCoins * tails = 0, tails  = 0
    #50% heads --> orderParam =  (numberOfCoins * tails)/2 = numberOfCoins/2
    
    for j in range (0, numberOfCoins):
        randomNumber =  random.random() #Random number between 0 and 1.  
        
############################## MY CHANGES ########################################        
        #If it's less than 0.5 then it's heads, more is tails
        ###################################### START EDIT HERE, A
        # Here goes an if else statement determine the value of a parameter called "currState"
        # basically it should either be heads or tails (use the heads/tails variables above)
        # as well as the value of randomNumber
        ##################################### END EDIT HERE, A
        if randomNumber < 0.5:
            currState = 1
        else:
            currState = 0
            
        # print ("The current state is ", currState, ".")
##################################################################################


############################## MY CHANGES ########################################
        ####################################### START EDIT HERE, B
        # here goes something where you add some number to the orderParam.  You'll have to use the currState that you defined above.
        ####################################### END EDIT HERE, B
        if currState == 1:
            orderParam += 1
##################################################################################

    fractionHeads = orderParam/numberOfCoins #number of coins that came up heads
    percentHeads = fractionHeads * 100
    #print percentHeads
    forBinning.append(fractionHeads)

#sort your data for easier binning
forBinning = sorted(forBinning)

#set up the histograms
histogram = [] #make an empty list
i = -binIncrement/2 #leftmost part of "window"
j = 0 #for array indexing
while i < 1.0 + binIncrement/2:  #clear out the histogram
    histogram.append(0) #add a bunch of zeroes
    #print "The left bin coordinate is", i, ".", "The histogram value is ", histogram[j], "."
    i = i + binIncrement #this is the next bin's leftmost part of the window
    j = j + 1 #the next index

jmax = j - 1 # the number of "bins"

currBinMax = binIncrement/2  # Because we want the first bin to be centered at 0
############################## this is the "rightmost" part of the bin.
#since our data is sorted, anything less than the first bin will be in the very beginning of our sorted data
#and then the next chunk will be for the second, etc...
j = 0 #index for the bins
i = 0 #index for the coinflip tries
#here we are taking all our "Tries" and putting it in the appropriate bin (fraction of heads or tails)
for j in range (0,jmax):  
    while i < numberOfRepetitions and forBinning[i] < currBinMax:
        histogram[j] = histogram[j] + 1
        i = i + 1
    currBinMax = currBinMax + binIncrement
#print forBinning
#print histogram


###################### MY CHANGES ##########################################################################
#normalize, the integral under should = 1
################################### START EDIT HERE, C
#You need to come up with the normalizationFactor.  Note, that the integral under the curve should equal 1.  Because the probability of being in SOME state should be 1.
#use the "rectangle method" (no need to get fancy with trapezoids).
#you'll need to use the total number of trials (i.e. numberOfReptitions) and the binIncrement (width of your bin) variables.
#normalizationFactor = ?
################################### END EDIT HERE, C
normalizationFactor = binIncrement*numpy.sum(histogram)
print "The area under the curve is", normalizationFactor, "."
print "\n"
############################################################################################################


normalized = []
#This is what actually gets printed out in the end.  
#Two column data, first column is the fraction of heads (our order parameter), second column is the probability of observing that fraction of heads
for i in range (0, len(histogram)):
    normalized.append(histogram[i]/normalizationFactor)
    #integral = integral + ? # use this if you like to check your normalization 
    #print "For", binIncrement*i*100, "percent of the coins land heads, the probability is", normalized[i]
    print "\n"

print normalized
print "The length of this array is", len(normalized)
normalizedArea = binIncrement*numpy.sum(normalized)
print "The area under the normalized curve is", normalizedArea
print "\n"

print "The number of bins is", jmax

pos = numpy.arange(jmax+1)
pos = pos/100
print pos

plt.bar(pos, normalized, binIncrement, color='b', alpha = 0.25)
plt.xlabel('Percent Coins Landed Heads')
plt.ylabel('Probability')
plt.title('CoinFlip Histogram')

#Here are the variables you will want to change
numberOfCoins = 100
numberOfRepetitions = 10000 #how many times to repeat the experiment
binIncrement = 0.01


#here is some setup stuff you don't have to worry about but might want to use
heads = 1
tails = 0

#here is a list for storing all our final outcomes
#we're defining a macrostate by the fraction of heads
forBinning = [] #where to store all the results

currState = 0
for i in range (0,numberOfRepetitions):
    orderParam = 0 
    #The order parameter is the sum of of the heads and tails 
    #50 heads followed by 50 tails = 50 tails followed by 50 heads
    #all heads --> orderParam = numberOfCoins * heads = numberOfCoins, heads = 1
    #all tails --> orderParam = numberOfCoins * tails = 0, tails  = 0
    #50% heads --> orderParam =  (numberOfCoins * tails)/2 = numberOfCoins/2
    
    for j in range (0, numberOfCoins):
        randomNumber =  random.random() #Random number between 0 and 1.  
        
############################## MY CHANGES ########################################        
        #If it's less than 0.5 then it's heads, more is tails
        ###################################### START EDIT HERE, A
        # Here goes an if else statement determine the value of a parameter called "currState"
        # basically it should either be heads or tails (use the heads/tails variables above)
        # as well as the value of randomNumber
        ##################################### END EDIT HERE, A
        if randomNumber < 0.5:
            currState = 1
        else:
            currState = 0
            
        # print ("The current state is ", currState, ".")
##################################################################################


############################## MY CHANGES ########################################
        ####################################### START EDIT HERE, B
        # here goes something where you add some number to the orderParam.  You'll have to use the currState that you defined above.
        ####################################### END EDIT HERE, B
        if currState == 1:
            orderParam += 1
##################################################################################

    fractionHeads = orderParam/numberOfCoins #number of coins that came up heads
    percentHeads = fractionHeads * 100
    #print percentHeads
    forBinning.append(fractionHeads)

#sort your data for easier binning
forBinning = sorted(forBinning)

#set up the histograms
histogram = [] #make an empty list
i = -binIncrement/2 #leftmost part of "window"
j = 0 #for array indexing
while i < 1.0 + binIncrement/2:  #clear out the histogram
    histogram.append(0) #add a bunch of zeroes
    #print "The left bin coordinate is", i, ".", "The histogram value is ", histogram[j], "."
    i = i + binIncrement #this is the next bin's leftmost part of the window
    j = j + 1 #the next index

jmax = j - 1 # the number of "bins"

currBinMax = binIncrement/2  # Because we want the first bin to be centered at 0
############################## this is the "rightmost" part of the bin.
#since our data is sorted, anything less than the first bin will be in the very beginning of our sorted data
#and then the next chunk will be for the second, etc...
j = 0 #index for the bins
i = 0 #index for the coinflip tries
#here we are taking all our "Tries" and putting it in the appropriate bin (fraction of heads or tails)
for j in range (0,jmax):  
    while i < numberOfRepetitions and forBinning[i] < currBinMax:
        histogram[j] = histogram[j] + 1
        i = i + 1
    currBinMax = currBinMax + binIncrement
#print forBinning
#print histogram


###################### MY CHANGES ##########################################################################
#normalize, the integral under should = 1
################################### START EDIT HERE, C
#You need to come up with the normalizationFactor.  Note, that the integral under the curve should equal 1.  Because the probability of being in SOME state should be 1.
#use the "rectangle method" (no need to get fancy with trapezoids).
#you'll need to use the total number of trials (i.e. numberOfReptitions) and the binIncrement (width of your bin) variables.
#normalizationFactor = ?
################################### END EDIT HERE, C
normalizationFactor = binIncrement*numpy.sum(histogram)
print "The area under the curve is", normalizationFactor, "."
print "\n"
############################################################################################################


normalized = []
#This is what actually gets printed out in the end.  
#Two column data, first column is the fraction of heads (our order parameter), second column is the probability of observing that fraction of heads
for i in range (0, len(histogram)):
    normalized.append(histogram[i]/normalizationFactor)
    #integral = integral + ? # use this if you like to check your normalization 
    #print "For", binIncrement*i*100, "percent of the coins land heads, the probability is", normalized[i]
    print "\n"

print normalized
print "The length of this array is", len(normalized)
normalizedArea = binIncrement*numpy.sum(normalized)
print "The area under the normalized curve is", normalizedArea
print "\n"

print "The number of bins is", jmax

pos = numpy.arange(jmax+1)
pos = pos/100
print pos

plt.bar(pos, normalized, binIncrement, color='r', alpha = 0.25)
plt.xlabel('Percent Coins Landed Heads')
plt.ylabel('Probability')
plt.title('CoinFlip Histogram')

#Here are the variables you will want to change
numberOfCoins = 10
numberOfRepetitions = 10000 #how many times to repeat the experiment
binIncrement = 0.01


#here is some setup stuff you don't have to worry about but might want to use
heads = 1
tails = 0

#here is a list for storing all our final outcomes
#we're defining a macrostate by the fraction of heads
forBinning = [] #where to store all the results

currState = 0
for i in range (0,numberOfRepetitions):
    orderParam = 0 
    #The order parameter is the sum of of the heads and tails 
    #50 heads followed by 50 tails = 50 tails followed by 50 heads
    #all heads --> orderParam = numberOfCoins * heads = numberOfCoins, heads = 1
    #all tails --> orderParam = numberOfCoins * tails = 0, tails  = 0
    #50% heads --> orderParam =  (numberOfCoins * tails)/2 = numberOfCoins/2
    
    for j in range (0, numberOfCoins):
        randomNumber =  random.random() #Random number between 0 and 1.  
        
############################## MY CHANGES ########################################        
        #If it's less than 0.5 then it's heads, more is tails
        ###################################### START EDIT HERE, A
        # Here goes an if else statement determine the value of a parameter called "currState"
        # basically it should either be heads or tails (use the heads/tails variables above)
        # as well as the value of randomNumber
        ##################################### END EDIT HERE, A
        if randomNumber < 0.5:
            currState = 1
        else:
            currState = 0
            
        # print ("The current state is ", currState, ".")
##################################################################################


############################## MY CHANGES ########################################
        ####################################### START EDIT HERE, B
        # here goes something where you add some number to the orderParam.  You'll have to use the currState that you defined above.
        ####################################### END EDIT HERE, B
        if currState == 1:
            orderParam += 1
##################################################################################

    fractionHeads = orderParam/numberOfCoins #number of coins that came up heads
    percentHeads = fractionHeads * 100
    #print percentHeads
    forBinning.append(fractionHeads)

#sort your data for easier binning
forBinning = sorted(forBinning)

#set up the histograms
histogram = [] #make an empty list
i = -binIncrement/2 #leftmost part of "window"
j = 0 #for array indexing
while i < 1.0 + binIncrement/2:  #clear out the histogram
    histogram.append(0) #add a bunch of zeroes
    #print "The left bin coordinate is", i, ".", "The histogram value is ", histogram[j], "."
    i = i + binIncrement #this is the next bin's leftmost part of the window
    j = j + 1 #the next index

jmax = j - 1 # the number of "bins"

currBinMax = binIncrement/2  # Because we want the first bin to be centered at 0
############################## this is the "rightmost" part of the bin.
#since our data is sorted, anything less than the first bin will be in the very beginning of our sorted data
#and then the next chunk will be for the second, etc...
j = 0 #index for the bins
i = 0 #index for the coinflip tries
#here we are taking all our "Tries" and putting it in the appropriate bin (fraction of heads or tails)
for j in range (0,jmax):  
    while i < numberOfRepetitions and forBinning[i] < currBinMax:
        histogram[j] = histogram[j] + 1
        i = i + 1
    currBinMax = currBinMax + binIncrement
#print forBinning
#print histogram


###################### MY CHANGES ##########################################################################
#normalize, the integral under should = 1
################################### START EDIT HERE, C
#You need to come up with the normalizationFactor.  Note, that the integral under the curve should equal 1.  Because the probability of being in SOME state should be 1.
#use the "rectangle method" (no need to get fancy with trapezoids).
#you'll need to use the total number of trials (i.e. numberOfReptitions) and the binIncrement (width of your bin) variables.
#normalizationFactor = ?
################################### END EDIT HERE, C
normalizationFactor = binIncrement*numpy.sum(histogram)
print "The area under the curve is", normalizationFactor, "."
print "\n"
############################################################################################################


normalized = []
#This is what actually gets printed out in the end.  
#Two column data, first column is the fraction of heads (our order parameter), second column is the probability of observing that fraction of heads
for i in range (0, len(histogram)):
    normalized.append(histogram[i]/normalizationFactor)
    #integral = integral + ? # use this if you like to check your normalization 
    #print "For", binIncrement*i*100, "percent of the coins land heads, the probability is", normalized[i]
    print "\n"

print normalized
print "The length of this array is", len(normalized)
normalizedArea = binIncrement*numpy.sum(normalized)
print "The area under the normalized curve is", normalizedArea
print "\n"

print "The number of bins is", jmax

pos = numpy.arange(jmax+1)
pos = pos/100
print pos

plt.bar(pos, normalized, binIncrement, color='y', alpha = 0.25)
plt.xlabel('Percent Coins Landed Heads')
plt.ylabel('Probability')
plt.title('CoinFlip Histogram')

plt.text(.2, 60, r'Green: 10000 coins')
plt.text(.2, 55, r'Blue: 1000 coins')
plt.text(.2, 50, r'Red: 100 coins')
plt.text(.2, 45, r'Yellow: 10 coins')
plt.text(.2, 40, r'Brown: all overlap')
plt.text(.6, 50, r'Alpha(opacity) = .25')

plt.show()