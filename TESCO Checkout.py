import  time
ration = 4 

print ("It is 2030, Society has developed the ability to code and understand it")
time.sleep (4)
print ("There is now no need to have graphical user interfaces. This is a Checkout System from the future")
time.sleep (1)
print ("Loading..")
time.sleep (1)
print ("Welcome to the TESCO Checkout System")
print ("What is your name?")
name = input ()

print ("Hello", name)
time.sleep (0.5)
print ("What do you want to insert into your basket?")
print ("The UK Government has issued an ration due to the war at bay. You only insert")
print ("4 products per session")

product = input ()

if product == "Banana":
    ration = ration-1
    print ("Your ration is now", ration)

elif product == "Apple":
    ration = ration-1
    print ("Your ration is now", ration)

