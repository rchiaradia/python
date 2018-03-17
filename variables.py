#https://www.guru99.com/variables-in-python.html
# Declare a variable and initialize it
f = 0
print (f)
# re-declaring the variable works
f = 'guru99'
print (f)

#Once the integer is declared as string, it can concatenate both "Guru" + str("99")= "Guru99" in the output.
a="Guru"
b = 99
print(a+str(b))

#Local & Global Variables

# Declare a variable and initialize it
f = 101
print(f)

# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print(f)
someFunction()
print(f)

#Using the keyword global, you can reference the global variable inside a function.
f = 101
print(f)
# Global vs.local variables in functions
def someFunction():
  global f
  print(f)
  f = "changing global variable"
someFunction()
print(f)


#Delete a variable
f = 11;
print(f)
del f
print(f)
