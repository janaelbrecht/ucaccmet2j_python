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
with open ('precipitation.json', 'r') as file: 
    precipitation = json.load(file)
    for measurement in precipitation:
        month=int(str(measurement["date"][5:7]))
        if measurement["station"] == Seattle_code:
            precip_Seattle[measurement["date"]] = {
                'month' : month,
                'precipitation': int(measurement["value"])
            }
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
with open ('Seattle_rain_permonth.json', 'w') as file:
    json.dump(precip_monthly, file, indent=4)

#Calculate the sum of the precipitation over the whole year
total_precip_year = sum(precip_monthly)
print(f'The total precipitation in Seatlle this year was {total_precip_year}') 

#Calculate the relative precipitation per month
# (percentage compared to the precipitation over the whole year)

#creating a list with 12 elements 
relative_precipitation = [0]*12

#making each element of the list correspond to relative precipitation in a month
for i in range (12):
    relative_precipitation[i] = precip_monthly[i]/total_precip_year

#to check if it all 'adds up' 
print(sum(relative_precipitation))
print(relative_precipitation)


#Rewrite your code so that it calculates all the above for each location
stationcodes = {}
with open ('stations.csv') as file:
    next(file)
    for line in file:
        Location, State, Station = line.split(',')
        stationcodes[Station.strip()] = {
            'State' : State.strip(),
            'Location' : Location.strip(),
            'Monthly prec': [0]*12
        }
print(stationcodes)

with open ('precipitation.json', 'r') as file: 
    precipitation = json.load(file)
    for measurement in precipitation:
        month=int(str(measurement["date"][5:7]))-1
        stationcodes[measurement["station"]]['Monthly prec'][month]+=measurement["value"]

print(stationcodes)

relative_prec = [0]*12 
for station in stationcodes: 
    stationcodes[station]['Sum prec']=sum(stationcodes[station]['Monthly prec'])
    stationcodes[station]['Relative prec']=relative_prec
    stationcodes[station]['Relative prec'][month]=stationcodes[station]['Monthly prec'][month]/sum(stationcodes[station]['Monthly prec'])
    

print(stationcodes)

'''
precip_per_location = {}
precip_monthly = [0,0,0,0,0,0,0,0,0,0,0,0]






with open ('precipitation.json', 'r') as file: 
    precipitation = json.load(file)
    for measurement in precipitation:
        month=int(str(measurement["date"][5:7]))
        value=measurement["value"]
        precip_monthly[month-1]+= measurement["value"]
            if measurement["station"] not in precip_per_location:
                precip_per_location[measurement["station"]] = {
                'precip per month': precip_monthly
                }
            else:
                pass 

print(precip_per_location)


total_precip_year = sum(precip_monthly)
print(f'The total precipitation in Seatlle this year was {total_precip_year}') 


relative_precipitation = [0]*12
for i in range (12):
    relative_precipitation[i] = precip_monthly[i]/total_precip_year
print(sum(relative_precipitation))
print(relative_precipitation)
'''