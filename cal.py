import pyfiglet

banner = pyfiglet.figlet_format("TG-Cal")
print(banner)

print("The Calculater U Need\n")
print("Enter + to do addition\n")
print("Enter * to do Multiplicatipn\n")
print("Enter - to do subraction\n")
print("Enter / to do division\n")


ui=input("Enter a Choice - ")

if ui=="+" :
  num1=float(input("Enter First Number : "))
  num2=float(input("Enter Second Number : "))
  res=(num1+num2)
  result=str(res)
  print("Your Result  : "+result)

elif ui=="*" :
  num1=float(input("Enter First Number : "))
  num2=float(input("Enter Second Number : "))
  res=(num1*num2)
  result=str(res)
  print("Your Result  : "+result)

elif ui=="-" :
  num1=float(input("Enter First Number : "))
  num2=float(input("Enter Second Number : "))
  res=(num1-num2)
  result=str(res)
  print("Your Result  : "+result)

elif ui=="/" :
  num1=float(input("Enter First Number : "))
  num2=float(input("Enter Second Number : "))
  res=(num1/num2)
  result=str(res)
  print("Your Result  : "+result)

else :
  print("Plzz Enter Right Selection")
