#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""This is some sample code I found that I am extending
  So far I have done:
  Find all files with DNA info in DIR
  Parse all files and find all DNA Chunks
  in each chunk find the primer sequence (if it exists)
  store all the 104char segments after the primer
  
  TODO:
  generate pyroprints (python)
  generate pyroprints (CUDA)
  compare pyroprints
"""

import sys
import os
import itertools

# Define a main() function that prints a little greeting.
def main():
  #Find all files in Dir
  path = 'Genome Sequences/ecoli36cassettes/'
  listing = os.listdir(path)
  allSequences =[]
  for infile in listing:
    #print "current file is: " + 'Genome Sequences/ecoli36cassettes/' + infile
    # Open File 
    f = open('Genome Sequences/ecoli36cassettes/' + infile)
    #print("currentFile: "+infile)
    substring = ""
    for line in f:
      if ">" in line:
        #print("NewSection:")
        allSequences.append(substring)
        #print(entireFile)
        substring = line
      else:
        substring += line.replace("\r\r\n","")
        #print(substring)
    f.close() 
  #TODO: Parse Primer from file Primer.txt
  #16-23 primer GGAACCTGCGGTTGGATCAC
  #23-5 primer CGTGAGGCTTAACCTT
  
  seqList = []
  primer = "GGAACCTGCGGTTGGATCAC"
    
  for sequence in allSequences:
    #print("sequence" + sequence)
    #find primer
    if primer in sequence:
      primerLoc = sequence.find(primer)
      #print('Found Primer At:' + str(primerLoc))
      #print("Found Primer in Sequence:" + sequence[primerLoc:primerLoc+20])
      #print("Found Sequence after Primer:" + sequence[primerLoc+20:primerLoc+20+140])
      #get next 104 chars
      seqList.append(sequence[primerLoc+20:primerLoc+20+140])
  uniqueSequences = []
  #find unique strings
  for oneSeq in seqList:
    #print("OneSeq::")
    #print(oneSeq)
    if oneSeq not in uniqueSequences:
      #print("found non unique seq:")
      #print(oneSeq)
      uniqueSequences.append(oneSeq)
      # else:
      #uniqueSequences.append(oneSeq)

  print("uniqueSequences") 
  print uniqueSequences
  allCombinations = itertools.combinations_with_replacement(uniqueSequences,7)
  #print ("Number of Unique Combinations: " + len(allCombinations))
  #print(len(allCombinations))
  numCombos = 0
  for oneCombo in allCombinations:
    numCombos = numCombos +1
    print(oneCombo)
    #print(numCombos)
    # for i in range(0, 100):
    #   print(allCombinations[0])

  #perform Pearson Corralation on pyroprints

  #save all sequences 

  #???
 
  #Profit!


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
