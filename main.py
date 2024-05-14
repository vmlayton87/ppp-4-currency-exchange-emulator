class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
  
  #add magic methods here
  def __repr__(self):
  # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
    return f"{round(self.value, 2)} {self.unit}"
  
  def __str__(self):
    #This method returns the same value as __repr__(self).
    return f"{round(self.value, 2)} {self.unit}"
    
  
  def __add__(self,other): # currency object + other
    #Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
    
    if type(other) == int or type(other) == float:
      # if other is not a Currency object, it is treated as a USD value
      other = Currency(other, "USD")
      
    # creates a new value to print. this changes the other's unit to match the self's unit and adds the values
    new_value = self.value + (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
    # then returns the new value in the self's unit
    return Currency(new_value, self.unit)

  def __iadd__(self,other): # +=
    return Currency.__add__(self,other)
    # This is the same as (calls) __add__(self,other)

  def __radd__(self,other): # other + currency object
  # This method is similar to __add__(self,other), but occurs when an int or float tries to add a Currency object. (Treat the int/float as having a USD value.)  
    # print('self: ', self, 'other: ', other)
    # the print here shows me that when you have int + currency object, it changes the self to currency object and other to the integer.
    if type(other) == int or type(other) == float:
      # print('inside if statement')
      # if other is not a Currency object, it is treated as a USD value
      other = Currency(other, "USD")
      # print(other)
    # creates a new value to print. this changes the self's unit to match the other's unit and adds the values
    new_value = other.value + (self.value / Currency.currencies[self.unit] * Currency.currencies[other.unit])
    # then returns the new value in the other's unit
    return Currency(new_value, other.unit)
  

# All __sub__(self,other) type functions are parallel to __add__(self,other) type functions.
  def __sub__(self,other): # currency object - other 
    #Defines the '-' operator. If other is a Currency object, the currency values are subtracted and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.

    if type(other) == int or type(other) == float:
      # if other is not a Currency object, it is treated as a USD value
      other = Currency(other, "USD")

    # creates a new value to print. this changes the other's unit to match the self's unit and subtracts the values in the order they were given
    new_value = self.value - (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
    # then returns the new value in the self's unit
    return Currency(new_value, self.unit)
  
  def __isub__(self,other): # -=
    return Currency.sub(self,other)
    
  def __rsub__(self,other): # other - currency object
      # This method is similar to __sub__(self,other), but occurs when an int or float tries to add a Currency object. (Treat the int/float as having a USD value.)
    # print('self: ', self, 'other: ', other)
    # the print here shows me that when you have int + currency object, it changes the self to currency object and other to the integer.
    if type(other) == int or type(other) == float:
      # print('inside if statement')
      # if other is not a Currency object, it is treated as a USD value
      other = Currency(other, "USD")
    # creates a new value to print. this changes the self's unit to match the other's unit and subtracts the values in the original order given
    new_value = other.value - (self.value / Currency.currencies[self.unit] * Currency.currencies[other.unit])
      # then returns the new value in the other's unit
    return Currency(new_value, other.unit)
  

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
