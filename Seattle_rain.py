import json
import csv

#making the stations.csv into a dictionary to find station code for Seattle. 
stations = {}
with open ('stations.csv') as file:
    next(file)
    for line in file:
        Location, State, Station = line.split(',')
        stations[Location] = {
            'state': State.strip(),
            'station': Station.strip()
        }
Seattle_code = stations["Seattle"]["station"]
print(f'The station code for Seattle is {Seattle_code}.')

#selecting the measurements for Seattle 
precip_Seattle = {}
dates = []
with open ('precipitation.json', 'r') as file: 
    precipitation = json.load(file)
    for measurement in precipitation:
        month=int(str(measurement["date"][5:7]))
        if measurement["station"] == Seattle_code:
            precip_Seattle[measurement["date"]] = {
                'month' : month,
                'precipitation': int(measurement["value"])
            }
        else:
            pass 
#print(precip_Seattle)


#Sum all the measurements for that location for each month
#Create an empty list
precip_monthly = [0,0,0,0,0,0,0,0,0,0,0,0]

for date in precip_Seattle:
    for i in range(12):
        if precip_Seattle[date]['month'] == i+1: 
            #i+1 since positions start counting at 0, but months at 1
            #at the percipitation of each measurement to the right month:
            precip_monthly[i]+= precip_Seattle[date]['precipitation']
        else:
            pass 

print(precip_monthly)

#This was the less efficient way, but I used it to check whether I got the right values
'''
percip_jan, percip_feb, percip_mar, percip_apr, percip_may, percip_jun, percip_jul, percip_aug, percip_sep, percip_oct, percip_nov, percip_dec = (0,0,0,0,0,0,0,0,0,0,0,0)
#for each measurement, add precipitation to the total of the right month: 
for date in precip_Seattle: #could also have put .values()
    if precip_Seattle[date]['month'] == 1:
        percip_jan += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 2:
        percip_feb += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 3:
        percip_mar += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 4:
        percip_apr += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 5:
        percip_may += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 6:
        percip_jun += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 7:
        percip_jul += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 8:
        percip_aug += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 9:
        percip_sep += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 10:
        percip_oct += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 11:
        percip_nov += precip_Seattle[date]['precipitation']
    elif precip_Seattle[date]['month'] == 12:
        percip_dec += precip_Seattle[date]['precipitation']
    else:
        pass

#making all the months into one list: 
precip_monthly = [percip_jan, percip_feb, percip_mar, percip_apr, percip_may, percip_jun, percip_jul, percip_aug, percip_sep, percip_oct, percip_nov, percip_dec]
print(precip_monthly)
'''

#save as json
with open ('Seattle_rain.json', 'w') as file: 
    json.dump(precip_Seattle, file, indent=4)