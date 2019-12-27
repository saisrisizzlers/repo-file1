#calculate persons age based on months and years.
#this is a feature of aadhar branch.
name = str(input("please enter your good name:"))
year = int(input("please enter the year you are born"))
print(year)
currentage = 2019 - year
months = currentage*12
days = currentage*365
print("hello "+name+" .you are %d years old." % (currentage))
print("hello "+name+" .you are %d months old." % (months))
def aad():
    num = input ("please enter you aad number")
    print(num)
    aad()
