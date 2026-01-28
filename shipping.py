# Shipping cost calculator

#declaring variables
final_price = 0
flat_charge = 0
flat_charge_ground = 20.00
flat_charge_prem = 125.00
flat_charge_drone = 0
valid = True
#input variables
weight = 0
shipping = 0 #we symbolize 0 for ground shipping 1 for premium ground shipping and 2 for drone shippimg

#user input section
input('''Welcome to Petridis express, here you can estimate your shipping cost,
We are offering three shipping options!, enter:
  0 for ground shipping.
  1 for premium ground shipping.
  2 for drone shipping.
  
   Press Enter to continue.''')
try:
    weight = float(input('Enter weight(kg):'))
except:
    print('Invalid weight!')
    valid = False
if valid:
    try:
        shipping = int(input('Enter shipping option:'))
    except:
        print('Invalid shipping type!')
        valid = False
if valid:
    if not shipping in (0, 1, 2):
        print('Invalid shipping type!')
        valid = False
  
 

#base charge
if shipping == 0:
  flat_charge = flat_charge_ground
elif shipping == 1:
  flat_charge = flat_charge_prem
elif shipping == 2:
  flat_charge = flat_charge_drone
else: 
  print('Error')
  valid = False
#ground
if valid:
 if shipping == 0 or shipping == 1:
  if weight <= 2 and weight > 0:
   final_price = flat_charge+weight*1.50
  elif weight > 2 and weight <= 6:
   final_price = flat_charge+weight*3.00
  elif weight >6 and weight<=10:
   final_price = flat_charge+weight*4.00
  elif weight >10:
   final_price = flat_charge+weight*4.75
  else:
   print('Error')
   valid = False


#drone
 elif shipping == 2:
  if weight <= 2 and weight > 0:
   final_price = flat_charge+weight*4.50
  elif weight > 2 and weight<=6:
   final_price = flat_charge+weight*9.00
  elif weight > 6 and weight<=10:
   final_price = flat_charge+weight*12.00
  elif weight >= 10:
   final_price = flat_charge+weight*14.25
  else:
   print('Error')
   valid = False
#result   
if valid:
  print('Your total shipping cost is:', round(final_price, 2),'€')


