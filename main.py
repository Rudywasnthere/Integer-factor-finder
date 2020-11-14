##Rudy Garcia
import math, sys
import time, sys
restart = ""
count = 0
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
  sqrt_num = math.sqrt(number)
  divisor = math.floor(sqrt_num)
  end_root= divisor
  while divisor>0: 
    upper_factor = number/divisor
    if upper_factor.is_integer() is True:
      upper_factor = int(upper_factor)
      factor_list += f"({divisor},{upper_factor})\n"
      count_factors += 1
    else:
      factor_list += ""
    divisor -= 1
  return factor_list, end_root, count_factors

while restart == "":
  if count == 0:
    x = input("To start, what is the number you want to factor:\t")
  if count != 0: 
    x= input("What number do you want to factor:\t")
  t_1 = time.perf_counter()
  factors, end_root, count_factors = factor_finder(x)
  t_2 = time.perf_counter()
  process_time= t_2 - t_1
  speed= end_root/process_time
  if count_factors ==1:
    verb= 'is'
    factor_ending= ""
    third_part = "it is"
    print(f"\n{x} is a prime number!\n")
  elif count_factors !=1:
    verb= "are"
    factor_ending= "s"
    third_part = "they are"
  print(f"There {verb} {count_factors} factor{factor_ending}! Here {third_part}:\n{factors}\nIt took {process_time} seconds to process {end_root} numbers!\nThats {speed} numbers per second!")
  restart= input("Hit enter to restart, or enter any key to quit ")
  count +=1 

