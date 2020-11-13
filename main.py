##Rudy Garcia
import math, sys
import time, sys

print("Hello, this is a program for finding the factors for any postive numput you input")

def factor_finder(number):
  factor_list = ""
  count_factors = 0
  is_integer = False
  while is_integer is False:
    try:
      number = int(number)
      is_integer = True
    except ValueError:
      number = input("I need a valid number, please:\t") 
      is_integer = False
  number_even= number %2
  sqrt_num = math.sqrt(number)
  divisor = math.floor(sqrt_num)
  end_root= divisor
  if number_even==0:
    count_by =1
  if number_even ==1:
    count_by =2
  else: 
    count_by= 1
  while divisor>0: 
    upper_factor = number/divisor
    if upper_factor.is_integer() is True:
      upper_factor = int(upper_factor)
      factor_list += f"({divisor},{upper_factor})\n"
      count_factors += 1
    else:
      factor_list += ""
    divisor -= count_by
  return factor_list, end_root, count_factors

def main(): 
  restart=""
  count = 0
  while restart =="":
    if count == 0:
      x = input("To start, what is the number you want to factor:\t")
    if count != 0: 
      x= input("What number do you want to factor:\t")
    t_1= time.process_time()
    factors, end_root, count_factors = factor_finder(x)
    t_2= time.process_time()
    total_time= t_2 - t_1
    speed_1= float(end_root/total_time)
    speed = round(speed_1,10)
    if count_factors== 1:
      print(f"\n{x} is a prime number!")
    print(F"There are {count_factors} factors! Here they are:\n{factors}")
    print(f"It took {total_time} seconds to process {end_root} numbers!\nThats {speed} numbers per second!")
    restart= input("Hit enter to restart, or enter any key to quit ")
    count +=1 
  print("I hope you enjoyed this program, have a good day!")

main()
