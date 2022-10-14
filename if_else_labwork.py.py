x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)

def myfunc():
  global x
  



print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"


myfunc()
print("Python is " + x)

a = 23
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  if a > b: print("a is greater than b")
  if a > b: print("a is greater than b")

  a = 330
b = 360
print("b") if a > b else print("a")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a=25
b=5
c=35
if a > b and c > a:
  print("both conditions are true")

a=25
b=5
c=35
if a > b or c > a:
  print("at least one of the conditions is true")

  
#nested if
  x=21

  if x > 10:
    print("above ten,")
    if x > 20:
      print("also above 20!")

a=24
b=2000

if b > a:
  pass


