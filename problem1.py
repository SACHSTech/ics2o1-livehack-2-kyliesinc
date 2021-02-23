
# title
print ("****Fine based on how much over the speed limit the driver is going.****")

# get speed limit and user's speed
speed_limit = int(input("Speed limit (in km/hr): "))
user_speed = int(input("Enter the recorded speed of the car (in km/hr): "))

# determine fine based on the speed limit and user's speed
if speed_limit >= user_speed:
  print ("Congratulations, you are within the speed limit! ")
  exit()
elif speed_limit + 31 <= user_speed:
  print ("You are speeding and your fine is $570!")
  exit()
elif speed_limit + 20 >= user_speed:
  print ("You are speeding and your fine is $100.")
  exit()
else:
  print ("You are speeding and your fine is $270.")
  exit()