from ctypes.wintypes import DOUBLE, FLOAT


buildingNumber = int(input('Building number is:'))
electricalBoxes = int(input('Number of electrical boxes is:'))


buildingSum = FLOAT(125 * buildingNumber)
boxSum = FLOAT(51 * electricalBoxes)
totalRev_2 = (buildingSum.value + boxSum.value)

print(f'Total revenue is: ${totalRev_2:.2f}.')



