# RomanNo.Conversion
_romanNumeral.py
_ conversion of roman numerals
_ author: miro holec
_ date: Jun 2, 2023
_ examples: CMXCVIII, XVI, MMXXIII, MCMLXXVII, MCMXLIV


## output

Step 1: Conversion of Roman Numbers into a list of decimals

CMXCVIII = [100, 1000, 10, 100, 5, 1, 1, 1]
XVI = [10, 5, 1]
MMXXIII = [1000, 1000, 10, 10, 1, 1, 1]
MCMLXXVII = [1000, 100, 1000, 50, 10, 10, 5, 1, 1]
MCMXLIV = [1000, 100, 1000, 10, 50, 1, 5]

Step 2: Assessment of the correct mathematical operators

CMXCVIII = [-100, 1000, -10, 100, 5, 1, 1, 1]
XVI = [10, 5, 1]
MMXXIII = [1000, 1000, 10, 10, 1, 1, 1]
MCMLXXVII = [1000, -100, 1000, 50, 10, 10, 5, 1, 1]
MCMXLIV = [1000, -100, 1000, -10, 50, -1, 5]

Step 3: Calculate the sum of the values of each roman number
RESUSLTS

CMXCVIII    =  [-100, 1000, -10, 100, 5, 1, 1, 1]        =  998       
XVI         =  [10, 5, 1]                                =  16        
MMXXIII     =  [1000, 1000, 10, 10, 1, 1, 1]             =  2023      
MCMLXXVII   =  [1000, -100, 1000, 50, 10, 10, 5, 1, 1]   =  1977      
MCMXLIV     =  [1000, -100, 1000, -10, 50, -1, 5]        =  1944 
