##Rudy Garcia
import math, sys
import time, sys

print("Hello, this is a program for finding the factors for any postive number you input")

def correct_input(x):
  is_integer = False
  while is_integer is False:
      try:
        x = int(x)
        is_integer = True
      except ValueError:
        x = input("I need a valid number, please:\t") 
        is_integer = False
  return x

def initials(x):
  sqrt_num = math.sqrt(x)
  divisor = math.floor(sqrt_num)
  end_root= divisor
  divisor_even= divisor%2
  x_even= x%2
  if x_even==0:
      count_by =1
  elif x_even ==1 and divisor_even==0:
      count_by =2
      divisor -= 1
  elif x_even ==1 and divisor_even ==1:
    count_by=2
  return count_by, divisor, end_root

def factor_finder(number, count_by, divisor):
  factor_list = ""
  count_factors = 0
  t_1= time.process_time()
  while divisor>0: 
    upper_factor = number/divisor
    if upper_factor.is_integer() is True:
      upper_factor = int(upper_factor)
      factor_list += f"({divisor},{upper_factor})\n"
      count_factors += 1
    else:
      factor_list += ""
    divisor -= count_by
  t_2= time.process_time()
  total_time= t_2 - t_1
  if count_factors == 1:
    verb, factor_ending, third_part= "is", "", "it is"
  else:
    verb, factor_ending, third_part= "are", "s", "they are"
  return factor_list, count_factors, total_time, verb, factor_ending, third_part

def main(count): 
  if count == 0:
    x = input("To start, what is the number you want to factor:\t")
  if count != 0: 
    x= input("What number do you want to factor:\t")
  x= correct_input(x)
  count_by, divisor, end_root= initials(x)
  factors, count_factors, total_time, verb, factor_ending, third_part = factor_finder(x, count_by, divisor)
  speed_1= float(end_root/total_time)
  speed = round(speed_1,10)
  if count_factors== 1:
    return f"\n{x} is a prime number!"
  return F"There {verb} {count_factors} factor{factor_ending}! Here {third_part}:\n{factors}\nIt took {total_time} seconds to process {end_root} numbers!\nThats {speed} numbers per second!"
  count +=1 

restart =""
while restart =="":
  count = 0
  print(main(count))
  restart= input("Hit enter to restart, or enter any key to quit ")
  count +=1 
print("I hope you enjoyed this program, have a good day!")