from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

def findAvg(nums):
  sum = 0;
  for item in nums:
    sum+=item
  return sum/len(nums)

def findMax(nums):
  max = nums[0]
  for item in nums:
    if item > max:
      max = item

  return max


def findMin(nums):
  min = nums[0]
  for item in nums:
    if item < min:
      min = item
  
  return min

def findMedian(nums):
  if len(nums)%2==0:
    return (nums[(int)(len(nums)/2)-1] + nums[(int)(len(nums)/2)]) / 2
  else:
    return nums[(int)(len(nums)/2)]


def findQuartileOne(nums):  
  if len(nums)%2 == 0:
    if len(nums)%4==0:
      return (nums[(int)(len(nums)/4)-1] + nums[(int)(len(nums)/4)]) / 2
    else:
      return nums[(int)(len(nums)/4)]
  else:
    return (nums[(int)(len(nums)/4)-1] + nums[(int)(len(nums)/4)]) / 2


def findQuartileThree(nums):
  if len(nums)%2 == 0:
    if len(nums)%4==0:
      return (nums[(int)(len(nums)*3/4)-1] + nums[(int)(len(nums)*3/4)]) / 2
    return nums[(int)(len(nums)*3/4)]
  else:
    return (nums[(int)(len(nums)*3/4)] + nums[(int)(len(nums)*3/4)+1]) / 2

def findIQR(nums):
  return findQuartileThree(nums) - findQuartileOne(nums)

#Lists are pre-sorted 

Phoenician_MSE_Data = [4.398024691,4.71283906,5.757931034,6.398977987,6.581740443,7.25,7.284735812,8.378983635,9.151494565,10.9267806267806]

Sanskrit_MSE_Data = [6.64236972704714,6.87992831541218,8.42477396021699, 9.35793172690763, 9.53660049627791, 9.74320882852292, 11.3505084745762, 12.1596610169491]

Arabic_MSE_Data = [6.94135802469135,7.43709884467265,11.1940345368916,11.2740909090909,16.3664]

Greek_MSE_Data = [3.721407625,3.739130435,4.048387097,5.802677942,5.927489177,7.749452155,8.422975352,9.805405405,11.45520717,13.75]


data = [
  
  ['Statistics of MSE Values', 'Phoenician', 'Sanskrit','Arabic','Greek'],
  ['Minimum', findMin(Phoenician_MSE_Data), findMin(Sanskrit_MSE_Data), findMin(Arabic_MSE_Data), findMin(Greek_MSE_Data)],
    ["Maximum", findMax(Phoenician_MSE_Data), findMax(Sanskrit_MSE_Data),findMax(Arabic_MSE_Data),findMax(Greek_MSE_Data)],
  ['1st Quartile', findQuartileOne(Phoenician_MSE_Data), findQuartileOne(Sanskrit_MSE_Data), findQuartileOne(Arabic_MSE_Data), findQuartileOne(Greek_MSE_Data)],
  ['3rd Quartile', findQuartileThree(Phoenician_MSE_Data), findQuartileThree(Sanskrit_MSE_Data), findQuartileThree(Arabic_MSE_Data), findQuartileThree(Greek_MSE_Data)],
  ['Interquartile Range', findIQR(Phoenician_MSE_Data), findIQR(Sanskrit_MSE_Data), findIQR(Arabic_MSE_Data), findIQR(Greek_MSE_Data)],
  ['Average', findAvg(Phoenician_MSE_Data), findAvg(Sanskrit_MSE_Data), findAvg(Arabic_MSE_Data), findAvg(Greek_MSE_Data)]
]


# display table
print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))

#to identify outliers using interquartile range method
print("\nData range to identify outliers using IQR:\n");

print("Phoenician range: ", findQuartileOne(Phoenician_MSE_Data) - (1.5 * findIQR(Phoenician_MSE_Data)), " to ", findQuartileThree(Phoenician_MSE_Data) + (1.5 * findIQR(Phoenician_MSE_Data)))

print("Sanskrit range: ", findQuartileOne(Sanskrit_MSE_Data) - (1.5 * findIQR(Sanskrit_MSE_Data)), " to ", findQuartileThree(Sanskrit_MSE_Data) + (1.5 * findIQR(Sanskrit_MSE_Data)))

print("Arabic range: ", findQuartileOne(Arabic_MSE_Data) - (1.5 * findIQR(Arabic_MSE_Data)), " to ", findQuartileThree(Arabic_MSE_Data) + (1.5 * findIQR(Arabic_MSE_Data)))

print("Greek range: ", findQuartileOne(Greek_MSE_Data) - (1.5 * findIQR(Greek_MSE_Data)), " to ", findQuartileThree(Greek_MSE_Data) + (1.5 * findIQR(Greek_MSE_Data)))



# display graph showing average values and IQRs
X = ['Phoenician','Sanskrit','Arabic','Greek'] 
avgVal = [findAvg(Phoenician_MSE_Data),findAvg(Sanskrit_MSE_Data),findAvg(Arabic_MSE_Data),findAvg(Greek_MSE_Data)] 
IQR = [findIQR(Phoenician_MSE_Data),findIQR(Sanskrit_MSE_Data),findIQR(Arabic_MSE_Data),findIQR(Greek_MSE_Data)] 

X_axis = np.arange(len(X)) 

plt.bar(X_axis - 0.2, avgVal, 0.4, label = 'Average') 
plt.bar(X_axis + 0.2, IQR, 0.4, label = 'Interquartile Range') 

plt.xticks(X_axis, X) 
plt.xlabel("Languages") 
plt.ylabel("Statistics of MSE Values") 
plt.title("Statistics of MSE Values for Various Languages") 
plt.legend() 
plt.show() 




