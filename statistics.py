
import math

class EmailAlert:
    def __init__(self):
        self.emailSent = False


class LEDAlert:
    def __init__(self):
        self.ledGlows = False


class StatsAlerter:
    def __init__(self, maxThreshold, alerts):
        self.maxThreshold = maxThreshold
        self.alerts = alerts

    def checkAndAlert(self, numbers):
        computedStats = calculateStats(numbers)

        if computedStats["max"] > self.maxThreshold:
            self.alerts[0].emailSent = True
            self.alerts[1].ledGlows = True
  
def calculateStats(numbers):
    if(numbers != []):
            
        computedStats = {'min':min(numbers),'max':max(numbers),'avg':(sum(numbers)/len(numbers))}

    else:
        computedStats = {'min':math.nan,'max':math.nan, 'avg':math.nan}
   
    return computedStats
