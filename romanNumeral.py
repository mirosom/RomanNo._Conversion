# romanNumeral.py
# conversion of roman numerals
# author: miro holec
# date: Jun 2, 2023
# examples: CMXCVIII, XVI, MMXXIII, MCMLXXVII, MCMXLIV

# loop for looping through romans, then calling a
# function1 for converting a string to a list of decimals
# this appends the gained list to values
# next function2 calls function3 which evaluates the values if + or -
# and then calculates the sum, appends to results
# function4 could print out


def convert(string):
    list_with_values = []
    for ch in string:
        list_with_values.append(numerals[ch])
    return list_with_values

def assess_operators(list_without_operator):  # decides about the operator -/+
    return_list = [] # maybe unused
    for i in range(len(list_without_operator)):
        val = list_without_operator[i]
        for j in range(len(val)-1):
            if val[j] < val[j+1]:
                val[j] = val[j]*(-1)
        list_without_operator[i] = val

def calculate(list_of_values):
    results = []
    for val in list_of_values:
        results.append(sum(val))
    return results

romans = ['CMXCVIII', 'XVI', 'MMXXIII', 'MCMLXXVII', 'MCMXLIV']
values = []
results = []
numerals = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    }

def main():
    for string in romans:
        values.append(convert(string))
    
    print(f"Step 1: Conversion of Roman Numbers into a list of decimals\n")
    for i in range(len(romans)):
        print(f"{romans[i]} = {values[i]}")
    
    print(f"\nStep 2: Assessment of the correct mathematical operators\n")
    assess_operators(values)
    for i in range(len(romans)):
        print(f"{romans[i]} = {values[i]}")    
    
    print(f"\nStep 3: Calculate the sum of the values of each roman number\nRESUSLTS\n")
    results= calculate(values)
    for i in range(len(romans)):
        
        print("{:<10}".format(romans[i]),
              ' = ',
              "{:<40}".format('['+ ', '.join(str(dig) for dig in values[i])+ ']'),
              ' = ',
              "{:<10}".format(results[i]))
    
main()