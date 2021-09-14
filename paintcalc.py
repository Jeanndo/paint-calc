# Paint calculator
print('Paint Calculator');
print('Enter the wall size as width and height in meters or press enter to stop');
print('example:10,30');

#Variables
walls =[]; # list of wall measurements in meter
gallons = 1/350; # one gallon can cover 350 square meter
total =0; #Total Gallons to buy 

# Get user inputs
while True:
   s=input('Enter wall size:')
   if len(s)==0:break

   # verify inputs
   sqmtrs= s.split(',')
   if len(sqmtrs)<2:
      print('Invalid format')
      break

   # converting inputs to integers
   w= int(sqmtrs[0])
   h= int(sqmtrs[1])
   item=[w,h]
   walls.append(item)
   print(f'Adding: {item}')

#calculting numbers
   print(f'You have entered: {walls}')

   for m in walls:
      w=m[0]
      h=m[1]
      area=w*h
      val=area*gallons
      total+=val
print(f'You need to buy: {round(total,2)} gallons')






