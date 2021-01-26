import sys
import os.path

class BatteryPower:
    self.resistance = 0.055

    #based on BATTERY_AGGREGATE_VC data which has voltage + current out of battery pack
    #unsure how to include the BATTERY_VT, which includes voltage + temperature out of one module?
    def get_power(self, current, voltage):
        return current * voltage