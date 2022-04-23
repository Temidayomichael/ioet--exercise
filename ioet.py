import re
from unittest import result


data = open('data.txt', 'r')

weekdaysPayPerHr = {
    'A': {
        'pay': 25,
        'startTime': 0,
        'endTime': 9,
    },
    'B': {
        'pay': 15,
        'startTime': 9,
        'endTime': 18,
    },
    'C': {
        'pay': 20,
        'startTime': 18,
        'endTime': 24,
    },
}
weekendPayPerHr = {
    'A': {
        'pay': 30,
        'startTime': 0,
        'endTime': 9,
    },
    'B': {
        'pay': 20,
        'startTime': 9,
        'endTime': 18,
    },
    'C': {
        'pay': 25,
        'startTime': 18,
        'endTime': 24,
    },
}


def calculateSalary(startTime, endTime, payPerHr):
    hrsWorkedA = hrsWorkedB = hrsWorkedC = 0
    startTime = int(startTime.split(
        ':')[0]) + (int(startTime.split(':')[1]) / 60)
    endTime = int(endTime.split(':')[0]) + \
        (int(endTime.split(':')[1]) / 60)

    if (startTime <= payPerHr['A']['endTime']):
        if (endTime <= payPerHr['A']['endTime']):
            hrsWorkedA = endTime - startTime
        elif (endTime <= payPerHr['B']['endTime']):
            hrsWorkedA = payPerHr['A']['endTime'] - startTime
            hrsWorkedB = endTime - payPerHr['B']['startTime']
        elif (endTime <= payPerHr['C']['endTime']):
            hrsWorkedA = payPerHr['A']['endTime'] - startTime
            hrsWorkedB = payPerHr['B']['endTime'] - payPerHr['B']['startTime']
            hrsWorkedC = endTime - payPerHr['C']['startTime']
    elif (startTime <= payPerHr['B']['endTime']):
        if (endTime <= payPerHr['B']['endTime']):
            hrsWorkedB = endTime - startTime
        elif (endTime <= payPerHr['C']['endTime']):
            hrsWorkedB = payPerHr['B']['endTime'] - payPerHr['B']['startTime']
            hrsWorkedC = endTime - payPerHr['C']['startTime']
    elif (startTime <= payPerHr['C']['endTime']):
        if (endTime <= payPerHr['C']['endTime']):
            hrsWorkedC = endTime - startTime
    else:
        return 0
    result = (hrsWorkedA * payPerHr['A']['pay']) + (hrsWorkedB *
                                                    payPerHr['B']['pay']) + (hrsWorkedC * payPerHr['C']['pay'])
    return round(result)


# calulating the salary for each employee
for line in data:
    totalSalary = 0

    if not re.match("^[a-zA-Z]+=((MO|TU|WE|TH|FR|SA|SU)(([0-1]?[0-9]|2[0-3]):[0-5][0-9])-(([0-1]?[0-9]|2[0-3]):[0-5][0-9]),?)+$", line):
        print("Invalid input format in: " + line)
    else:
        line = line.split('=')
        empName = line[0]
        schedule = line[1]

        for day in schedule.split(','):
            workedHrs = day[2:].split('-')
            dayName = day[:2]
            startTime = workedHrs[0]
            endTime = workedHrs[1]
            payPerHr = weekdaysPayPerHr if dayName in [
                'MO', 'TU', 'WE', 'TH', 'FR'] else weekendPayPerHr
            totalSalary += calculateSalary(startTime, endTime, payPerHr)
        print('The amount to pay '+empName +
              ' is: '+str((totalSalary))+' USD')

# Closing files
data.close()
