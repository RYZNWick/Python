year = int(input("enter a year"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("Given year is a leap year",year)
       else:                 #if all fall..
           print("Given year is not a leap year",year)
   else:                     
       print("Given year is a leap year",year)
else:
   print("Given year is not a leap year",year)