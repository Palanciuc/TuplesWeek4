value = (10,8,9,18)



def menu():
  global value
  option = ''
  while(option != 6):
    print('*** Tuple Example ***')
    print('1. Print Tuple ***')
    print('2. Loop over tuple')
    print('3. Copy Tuple')
    print('4. Convert to List')
    print('5. Sort a tuple')
    print('6. Exit ***')
    option = int(input('Please enter option: '))

    if(option == 1):
     print(value)
    elif(option == 2):
      for x in value:
        print(x)
      #Loop through the tuple printing each element
    elif(option == 3):
      start = int(input('Enter start of range: '))
      end = int(input('Enter end of range: '))
      newtuple = value[start:end]
      print(newtuple)
    elif(option == 4):
      templist = list(value)
      templist.append(100)
      value = tuple(templist)
      print(value) 
    elif(option == 5):
      templist = list(value)
      templist = sorted(templist, reverse = True)
      value = tuple(templist)
      print(value)