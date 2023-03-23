import csv
import statistics

FILE_NUM = 6
rows_0 = ""
rows_1 = ""
rows_2 = ""
rows_3 = ""

prediction_all = []

for i in range(FILE_NUM):
  with open('prediction_'+str(i)+'.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    rows = list(rows)
    prediction_all.append(rows)

################## write #######################
print("write csv")
with open('prediction_voted.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)

  writer.writerow(prediction_all[0][0])
  
  for i in range(1, len(prediction_all[0])):
    test_list = []
    for j in range(FILE_NUM):
      test_list.append(int(prediction_all[j][i][1]))
    try:
      value = statistics.mode(test_list)
    except:
      value = prediction_all[0][i][1]
    writer.writerow([i-1, value])
