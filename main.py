
import pandas as pd
import csv


# import date , time and sensor data from CGMData.csv file
CGM_data = pd.read_csv('CGMData.csv', usecols=['Date','Time','Sensor Glucose (mg/dL)'], low_memory=True)
#print(CGM_data.iloc[0]['Date'])
#print(CGM_data.iloc[0]['Time'])
#print(CGM_data.iloc[0]['Sensor Glucose (mg/dL)'])
# import date , time and alarm from InsulinData.csv file
Insulin_data = pd.read_csv('InsulinData.csv', usecols=['Date', 'Time', 'Alarm'], low_memory=True)
#print(Insulin_data.iloc[0]['Date'])
#print(Insulin_data.iloc[0]['Time'])
#print(Insulin_data.iloc[0]['Alarm'])

# read Date and Sensor Data from CGMData.csv
Count_CGM = pd.read_csv('CGMData.csv', usecols=['Index','Date','Time', 'Sensor Glucose (mg/dL)'], low_memory=True)
# remove the sensor data where the data is nan
CGM_data_without_nan = Count_CGM[~Count_CGM['Sensor Glucose (mg/dL)'].isnull()]
#print(CGM_data_without_nan.groupby('Date'))
# count the number for each date where data is present
Count_CGM = CGM_data_without_nan.groupby('Date').count()
# filter the dates where data available is greater than 80% of 288
Count_CGM = Count_CGM[Count_CGM['Sensor Glucose (mg/dL)'] > 230]
Date_considered = Count_CGM.to_csv('ImpDate.csv')
Date_imp = pd.read_csv('ImpDate.csv', usecols=['Date', 'Sensor Glucose (mg/dL)'], low_memory=True)
# print(CGM_data_without_nan)
CGM_data_without_nan = CGM_data_without_nan[CGM_data_without_nan['Date'].isin(Date_imp['Date'])]
# print(CGM_data_without_nan)
# remove the unwanted data from the main df

# print(CGM_data_without_nan.iloc[0]['Time'])
# print(Date_imp.iloc[1]['Date'])

'''for i in range(0, len(CGM_data_without_nan['Date'])):
    count = 0
    for j in range(0, len(Date_imp['Date'])):
        if CGM_data_without_nan.iloc[i]['Date'] != Date_imp.iloc[j]['Date']:
            count = count + 1
    if count == 165:
        index = CGM_data_without_nan.iloc[i]['Index']
        CGM_data_without_nan = CGM_data_without_nan.drop(index)
print(CGM_data_without_nan)'''
#print(Date_imp.iloc[0]['Date'])

# placeholders
AUTO_Start_Date = "1/21/2017"
AUTO_Start_Time = "02:02:02"
# check when the auto mode starts
#print(len(Insulin_data['Alarm']))
for i in range(1, len(Insulin_data['Alarm'])):
    if Insulin_data.iloc[len(Insulin_data['Alarm'])-i]['Alarm'] == "AUTO MODE ACTIVE PLGM OFF":
        AUTO_Start_Date = Insulin_data.iloc[len(Insulin_data['Alarm'])-i]['Date']
        AUTO_Start_Time = Insulin_data.iloc[len(Insulin_data['Alarm'])-i]['Time']
        break

AUTO_Start_Date_Time = pd.to_datetime(AUTO_Start_Date+' '+AUTO_Start_Time)
# print(AUTO_Start_Date)
# print(AUTO_Start_Time)
# print(AUTO_Start_Date_Time)

# Metrics to be extracted and groupby with count
CGM_data_hyperglycemia = CGM_data_without_nan[CGM_data_without_nan['Sensor Glucose (mg/dL)'] > 180]
CGM_data_hyperglycemia['DateTime'] = pd.to_datetime(CGM_data_hyperglycemia['Date']+' '+CGM_data_hyperglycemia['Time'])
CGM_data_hyperglycemia['Time1'] = pd.to_datetime(CGM_data_hyperglycemia['Time'])
# print(CGM_data_hyperglycemia.Time1.dt.time.head())
# print(CGM_data_hyperglycemia.Date.str.slice(-4).astype(int))
# hyperglycemia = CGM_data_hyperglycemia.to_csv('hyperglycemia.csv')
CGM_data_hyperglycemia_critical = CGM_data_without_nan[CGM_data_without_nan['Sensor Glucose (mg/dL)'] > 250]
CGM_data_hyperglycemia_critical['DateTime'] = pd.to_datetime(CGM_data_hyperglycemia_critical['Date']+' '+CGM_data_hyperglycemia_critical['Time'])
CGM_data_hyperglycemia_critical['Time1'] = pd.to_datetime(CGM_data_hyperglycemia_critical['Time'])
# hyperglycemia_critical = CGM_data_hyperglycemia_critical.to_csv('hyperglycemia_critical.csv')
CGM_data_70_180 = CGM_data_without_nan[CGM_data_without_nan['Sensor Glucose (mg/dL)'].ge(70)]
CGM_data_70_180 = CGM_data_70_180[CGM_data_70_180['Sensor Glucose (mg/dL)'].le(180)]
CGM_data_70_180['DateTime'] = pd.to_datetime(CGM_data_70_180['Date']+' '+CGM_data_70_180['Time'])
CGM_data_70_180['Time1'] = pd.to_datetime(CGM_data_70_180['Time'])
# range70_180 = CGM_data_70_180.to_csv('70_180.csv')
CGM_data_70_150 = CGM_data_without_nan[CGM_data_without_nan['Sensor Glucose (mg/dL)'].ge(70)]
CGM_data_70_150 = CGM_data_70_150[CGM_data_70_150['Sensor Glucose (mg/dL)'].le(150)]
CGM_data_70_150['DateTime'] = pd.to_datetime(CGM_data_70_150['Date']+' '+CGM_data_70_150['Time'])
CGM_data_70_150['Time1'] = pd.to_datetime(CGM_data_70_150['Time'])
# range70_150 = CGM_data_70_150.to_csv('70_150.csv')
CGM_data_hypoglycemia1 = CGM_data_without_nan[CGM_data_without_nan['Sensor Glucose (mg/dL)'] < 70]
CGM_data_hypoglycemia1['DateTime'] = pd.to_datetime(CGM_data_hypoglycemia1['Date']+' '+CGM_data_hypoglycemia1['Time'])
CGM_data_hypoglycemia1['Time1'] = pd.to_datetime(CGM_data_hypoglycemia1['Time'])
# hypoglycemia1= CGM_data_hypoglycemia1.to_csv('hypoglycemia1.csv')
CGM_data_hypoglycemia2 = CGM_data_without_nan[CGM_data_without_nan['Sensor Glucose (mg/dL)'] < 54]
CGM_data_hypoglycemia2['DateTime'] = pd.to_datetime(CGM_data_hypoglycemia2['Date']+' '+CGM_data_hypoglycemia2['Time'])
CGM_data_hypoglycemia2['Time1'] = pd.to_datetime(CGM_data_hypoglycemia2['Time'])
# hypoglycemia2= CGM_data_hypoglycemia2.to_csv('hypoglycemia2.csv')

hyperglycemia_manual_overnight=0
hyperglycemia_manual_day=0
hyperglycemia_manual_wholeday=0
hyperglycemia_auto_overnight=0
hyperglycemia_auto_day=0
hyperglycemia_auto_wholeday=0
DayStartTime = pd.to_datetime('06:00:00')
DayEndTime = pd.to_datetime('23:59:59')
OvernightStartTime = pd.to_datetime('00:00:00')
OvernightEndTime = pd.to_datetime('05:59:59')
# print(len(CGM_data_hyperglycemia['Sensor Glucose (mg/dL)'])) b
# for hyperglycemia
for i in range(0, len(CGM_data_hyperglycemia['Sensor Glucose (mg/dL)'])):
    if CGM_data_hyperglycemia.iloc[i]['DateTime'] > AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_hyperglycemia.iloc[i]['Time1'] <= OvernightEndTime:
        hyperglycemia_auto_wholeday = hyperglycemia_auto_wholeday+1
        hyperglycemia_auto_overnight = hyperglycemia_auto_overnight+1
    if CGM_data_hyperglycemia.iloc[i]['DateTime'] > AUTO_Start_Date_Time and DayStartTime <= CGM_data_hyperglycemia.iloc[i]['Time1'] <= DayEndTime:
        hyperglycemia_auto_wholeday = hyperglycemia_auto_wholeday+1
        hyperglycemia_auto_day = hyperglycemia_auto_day+1
    if CGM_data_hyperglycemia.iloc[i]['DateTime'] < AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_hyperglycemia.iloc[i]['Time1'] <= OvernightEndTime:
        hyperglycemia_manual_wholeday = hyperglycemia_manual_wholeday+1
        hyperglycemia_manual_overnight = hyperglycemia_manual_overnight+1
    if CGM_data_hyperglycemia.iloc[i]['DateTime'] < AUTO_Start_Date_Time and DayStartTime <= CGM_data_hyperglycemia.iloc[i]['Time1'] <= DayEndTime:
        hyperglycemia_manual_wholeday = hyperglycemia_manual_wholeday+1
        hyperglycemia_manual_day = hyperglycemia_manual_day+1

hyperglycemia_auto_wholeday = (hyperglycemia_auto_wholeday*100)/(288*len(Date_imp['Date']))
hyperglycemia_auto_overnight = (hyperglycemia_auto_overnight*100)/(288*len(Date_imp['Date']))
hyperglycemia_auto_day = (hyperglycemia_auto_day*100)/(288*len(Date_imp['Date']))
hyperglycemia_manual_wholeday = (hyperglycemia_manual_wholeday*100)/(288*len(Date_imp['Date']))
hyperglycemia_manual_overnight = (hyperglycemia_manual_overnight*100)/(288*len(Date_imp['Date']))
hyperglycemia_manual_day = (hyperglycemia_manual_day*100)/(288*len(Date_imp['Date']))

'''print(hyperglycemia_auto_wholeday)
print(hyperglycemia_auto_overnight)
print(hyperglycemia_auto_day)
print(hyperglycemia_manual_wholeday)
print(hyperglycemia_manual_overnight)
print(hyperglycemia_manual_day)'''

# for 70-180

a_manual_overnight=0
a_manual_day=0
a_manual_wholeday=0
a_auto_overnight=0
a_auto_day=0
a_auto_wholeday=0

for i in range(0, len(CGM_data_70_180['Sensor Glucose (mg/dL)'])):
    if CGM_data_70_180.iloc[i]['DateTime'] > AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_70_180.iloc[i]['Time1'] <= OvernightEndTime:
        a_auto_wholeday = a_auto_wholeday+1
        a_auto_overnight = a_auto_overnight+1
    if CGM_data_70_180.iloc[i]['DateTime'] > AUTO_Start_Date_Time and DayStartTime <= CGM_data_70_180.iloc[i]['Time1'] <= DayEndTime:
        a_auto_wholeday = a_auto_wholeday+1
        a_auto_day = a_auto_day+1
    if CGM_data_70_180.iloc[i]['DateTime'] < AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_70_180.iloc[i]['Time1'] <= OvernightEndTime:
        a_manual_wholeday = a_manual_wholeday+1
        a_manual_overnight = a_manual_overnight+1
    if CGM_data_70_180.iloc[i]['DateTime'] < AUTO_Start_Date_Time and DayStartTime <= CGM_data_70_180.iloc[i]['Time1'] <= DayEndTime:
        a_manual_wholeday = a_manual_wholeday+1
        a_manual_day = a_manual_day+1

a_auto_wholeday = (a_auto_wholeday*100)/(288*len(Date_imp['Date']))
a_auto_overnight = (a_auto_overnight*100)/(288*len(Date_imp['Date']))
a_auto_day = (a_auto_day*100)/(288*len(Date_imp['Date']))
a_manual_wholeday = (a_manual_wholeday*100)/(288*len(Date_imp['Date']))
a_manual_overnight = (a_manual_overnight*100)/(288*len(Date_imp['Date']))
a_manual_day = (a_manual_day*100)/(288*len(Date_imp['Date']))
'''print('70-180')
print(a_auto_wholeday)
print(a_auto_overnight)
print(a_auto_day)
print(a_manual_wholeday)
print(a_manual_overnight)
print(a_manual_day)'''


# for hyperglycemia critical

hyperglycemia_critical_manual_overnight=0
hyperglycemia_critical_manual_day=0
hyperglycemia_critical_manual_wholeday=0
hyperglycemia_critical_auto_overnight=0
hyperglycemia_critical_auto_day=0
hyperglycemia_critical_auto_wholeday=0

for i in range(0, len(CGM_data_hyperglycemia_critical['Sensor Glucose (mg/dL)'])):
    if CGM_data_hyperglycemia_critical.iloc[i]['DateTime'] > AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_hyperglycemia_critical.iloc[i]['Time1'] <= OvernightEndTime:
        hyperglycemia_critical_auto_wholeday = hyperglycemia_critical_auto_wholeday+1
        hyperglycemia_critical_auto_overnight = hyperglycemia_critical_auto_overnight+1
    if CGM_data_hyperglycemia_critical.iloc[i]['DateTime'] > AUTO_Start_Date_Time and DayStartTime <= CGM_data_hyperglycemia_critical.iloc[i]['Time1'] <= DayEndTime:
        hyperglycemia_critical_auto_wholeday = hyperglycemia_critical_auto_wholeday+1
        hyperglycemia_critical_auto_day = hyperglycemia_critical_auto_day+1
    if CGM_data_hyperglycemia_critical.iloc[i]['DateTime'] < AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_hyperglycemia_critical.iloc[i]['Time1'] <= OvernightEndTime:
        hyperglycemia_critical_manual_wholeday = hyperglycemia_critical_manual_wholeday+1
        hyperglycemia_critical_manual_overnight = hyperglycemia_critical_manual_overnight+1
    if CGM_data_hyperglycemia_critical.iloc[i]['DateTime'] < AUTO_Start_Date_Time and DayStartTime <= CGM_data_hyperglycemia_critical.iloc[i]['Time1'] <= DayEndTime:
        hyperglycemia_critical_manual_wholeday = hyperglycemia_critical_manual_wholeday+1
        hyperglycemia_critical_manual_day = hyperglycemia_critical_manual_day+1

hyperglycemia_critical_auto_wholeday = (hyperglycemia_critical_auto_wholeday*100)/(288*len(Date_imp['Date']))
hyperglycemia_critical_auto_overnight = (hyperglycemia_critical_auto_overnight*100)/(288*len(Date_imp['Date']))
hyperglycemia_critical_auto_day = (hyperglycemia_critical_auto_day*100)/(288*len(Date_imp['Date']))
hyperglycemia_critical_manual_wholeday = (hyperglycemia_critical_manual_wholeday*100)/(288*len(Date_imp['Date']))
hyperglycemia_critical_manual_overnight = (hyperglycemia_critical_manual_overnight*100)/(288*len(Date_imp['Date']))
hyperglycemia_critical_manual_day = (hyperglycemia_critical_manual_day*100)/(288*len(Date_imp['Date']))
'''print('Hypercritical')
print(hyperglycemia_critical_auto_wholeday)
print(hyperglycemia_critical_auto_overnight)
print(hyperglycemia_critical_auto_day)
print(hyperglycemia_critical_manual_wholeday)
print(hyperglycemia_critical_manual_overnight)
print(hyperglycemia_critical_manual_day)'''

# for 70-150

b_manual_overnight=0
b_manual_day=0
b_manual_wholeday=0
b_auto_overnight=0
b_auto_day=0
b_auto_wholeday=0

for i in range(0, len(CGM_data_70_150['Sensor Glucose (mg/dL)'])):
    if CGM_data_70_150.iloc[i]['DateTime'] > AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_70_150.iloc[i]['Time1'] <= OvernightEndTime:
        b_auto_wholeday = b_auto_wholeday+1
        b_auto_overnight = b_auto_overnight+1
    if CGM_data_70_150.iloc[i]['DateTime'] > AUTO_Start_Date_Time and DayStartTime <= CGM_data_70_150.iloc[i]['Time1'] <= DayEndTime:
        b_auto_wholeday = b_auto_wholeday+1
        b_auto_day = b_auto_day+1
    if CGM_data_70_150.iloc[i]['DateTime'] < AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_70_150.iloc[i]['Time1'] <= OvernightEndTime:
        b_manual_wholeday = b_manual_wholeday+1
        b_manual_overnight = b_manual_overnight+1
    if CGM_data_70_150.iloc[i]['DateTime'] < AUTO_Start_Date_Time and DayStartTime <= CGM_data_70_150.iloc[i]['Time1'] <= DayEndTime:
        b_manual_wholeday = b_manual_wholeday+1
        b_manual_day = b_manual_day+1

b_auto_wholeday = (b_auto_wholeday*100)/(288*len(Date_imp['Date']))
b_auto_overnight = (b_auto_overnight*100)/(288*len(Date_imp['Date']))
b_auto_day = (b_auto_day*100)/(288*len(Date_imp['Date']))
b_manual_wholeday = (b_manual_wholeday*100)/(288*len(Date_imp['Date']))
b_manual_overnight = (b_manual_overnight*100)/(288*len(Date_imp['Date']))
b_manual_day = (b_manual_day*100)/(288*len(Date_imp['Date']))
'''print('70-150')
print(b_auto_wholeday)
print(b_auto_overnight)
print(b_auto_day)
print(b_manual_wholeday)
print(b_manual_overnight)
print(b_manual_day)'''

# for hypo1

c_manual_overnight=0
c_manual_day=0
c_manual_wholeday=0
c_auto_overnight=0
c_auto_day=0
c_auto_wholeday=0

for i in range(0, len(CGM_data_hypoglycemia1['Sensor Glucose (mg/dL)'])):
    if CGM_data_hypoglycemia1.iloc[i]['DateTime'] > AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_hypoglycemia1.iloc[i]['Time1'] <= OvernightEndTime:
        c_auto_wholeday = c_auto_wholeday+1
        c_auto_overnight = c_auto_overnight+1
    if CGM_data_hypoglycemia1.iloc[i]['DateTime'] > AUTO_Start_Date_Time and DayStartTime <= CGM_data_hypoglycemia1.iloc[i]['Time1'] <= DayEndTime:
        c_auto_wholeday = c_auto_wholeday+1
        c_auto_day = c_auto_day+1
    if CGM_data_hypoglycemia1.iloc[i]['DateTime'] < AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_hypoglycemia1.iloc[i]['Time1'] <= OvernightEndTime:
        c_manual_wholeday = c_manual_wholeday+1
        c_manual_overnight = c_manual_overnight+1
    if CGM_data_hypoglycemia1.iloc[i]['DateTime'] < AUTO_Start_Date_Time and DayStartTime <= CGM_data_hypoglycemia1.iloc[i]['Time1'] <= DayEndTime:
        c_manual_wholeday = c_manual_wholeday+1
        c_manual_day = c_manual_day+1

c_auto_wholeday = (c_auto_wholeday*100)/(288*len(Date_imp['Date']))
c_auto_overnight = (c_auto_overnight*100)/(288*len(Date_imp['Date']))
c_auto_day = (c_auto_day*100)/(288*len(Date_imp['Date']))
c_manual_wholeday = (c_manual_wholeday*100)/(288*len(Date_imp['Date']))
c_manual_overnight = (c_manual_overnight*100)/(288*len(Date_imp['Date']))
c_manual_day = (c_manual_day*100)/(288*len(Date_imp['Date']))
'''print('hypo1')
print(c_auto_wholeday)
print(c_auto_overnight)
print(c_auto_day)
print(c_manual_wholeday)
print(c_manual_overnight)
print(c_manual_day)'''

# for hypo2

d_manual_overnight=0
d_manual_day=0
d_manual_wholeday=0
d_auto_overnight=0
d_auto_day=0
d_auto_wholeday=0

for i in range(0, len(CGM_data_hypoglycemia2['Sensor Glucose (mg/dL)'])):
    if CGM_data_hypoglycemia2.iloc[i]['DateTime'] > AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_hypoglycemia2.iloc[i]['Time1'] <= OvernightEndTime:
        d_auto_wholeday = d_auto_wholeday+1
        d_auto_overnight = d_auto_overnight+1
    if CGM_data_hypoglycemia2.iloc[i]['DateTime'] > AUTO_Start_Date_Time and DayStartTime <= CGM_data_hypoglycemia2.iloc[i]['Time1'] <= DayEndTime:
        d_auto_wholeday = d_auto_wholeday+1
        d_auto_day = d_auto_day+1
    if CGM_data_hypoglycemia2.iloc[i]['DateTime'] < AUTO_Start_Date_Time and OvernightStartTime <= CGM_data_hypoglycemia2.iloc[i]['Time1'] <= OvernightEndTime:
        d_manual_wholeday = d_manual_wholeday+1
        d_manual_overnight = d_manual_overnight+1
    if CGM_data_hypoglycemia2.iloc[i]['DateTime'] < AUTO_Start_Date_Time and DayStartTime <= CGM_data_hypoglycemia2.iloc[i]['Time1'] <= DayEndTime:
        d_manual_wholeday = d_manual_wholeday+1
        d_manual_day = d_manual_day+1

d_auto_wholeday = (d_auto_wholeday*100)/(288*len(Date_imp['Date']))
d_auto_overnight = (d_auto_overnight*100)/(288*len(Date_imp['Date']))
d_auto_day = (d_auto_day*100)/(288*len(Date_imp['Date']))
d_manual_wholeday = (d_manual_wholeday*100)/(288*len(Date_imp['Date']))
d_manual_overnight = (d_manual_overnight*100)/(288*len(Date_imp['Date']))
d_manual_day = (d_manual_day*100)/(288*len(Date_imp['Date']))
'''print('hypo2')
print(d_auto_wholeday)
print(d_auto_overnight)
print(d_auto_day)
print(d_manual_wholeday)
print(d_manual_overnight)
print(d_manual_day)
print(hyperglycemia_auto_wholeday)'''
result1 = [hyperglycemia_manual_overnight,hyperglycemia_critical_manual_overnight,a_manual_overnight,b_manual_overnight,c_manual_overnight,d_manual_overnight,hyperglycemia_manual_day,hyperglycemia_critical_manual_day,a_manual_day,b_manual_day,c_manual_day,d_manual_day,hyperglycemia_manual_wholeday,hyperglycemia_critical_manual_wholeday,a_manual_wholeday,b_manual_wholeday,c_manual_wholeday,d_manual_wholeday]
result2 = [hyperglycemia_auto_overnight,hyperglycemia_critical_auto_overnight,a_auto_overnight,b_auto_overnight,c_auto_overnight,d_auto_overnight,hyperglycemia_auto_day,hyperglycemia_critical_auto_day,a_auto_day,b_auto_day,c_auto_day,d_auto_day,hyperglycemia_auto_wholeday,hyperglycemia_critical_auto_wholeday,a_auto_wholeday,b_auto_wholeday,c_auto_wholeday,d_auto_wholeday]
result=[[hyperglycemia_auto_overnight,hyperglycemia_critical_manual_overnight,a_manual_overnight,b_manual_overnight,c_manual_overnight,d_manual_overnight,hyperglycemia_manual_day,hyperglycemia_critical_manual_day,a_manual_day,b_manual_day,c_manual_day,d_manual_day,hyperglycemia_manual_wholeday,hyperglycemia_critical_manual_wholeday,a_manual_wholeday,b_manual_wholeday,c_manual_wholeday,d_manual_wholeday],[hyperglycemia_auto_overnight,hyperglycemia_critical_auto_overnight,a_auto_overnight,b_auto_overnight,c_auto_overnight,d_auto_overnight,hyperglycemia_auto_day,hyperglycemia_critical_auto_day,a_auto_day,b_auto_day,c_auto_day,d_auto_day,hyperglycemia_auto_wholeday,hyperglycemia_critical_auto_wholeday,a_auto_wholeday,b_auto_wholeday,c_auto_wholeday,d_auto_wholeday]]


filename='Results.csv'

with open(filename,'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(result1)
    csvwriter.writerow(result2)

















