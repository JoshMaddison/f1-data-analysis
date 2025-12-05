
import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt

#To increase the speed of loading for data:
fastf1.Cache.enable_cache('cache')

#Getting a formula 1 session, 2021 Silverstone Qualifying was chose:
session = fastf1.get_session(2021, 'Silverstone', 'Q')
session.load()

#Chose to compare Verstappen to Hamilton
lap1 = session.laps.pick_drivers('VER').pick_fastest()
lap2 = session.laps.pick_drivers('HAM').pick_fastest()

#Telemetry
tel1 = lap1.get_telemetry()
tel2 = lap2.get_telemetry()

#Plotting
plt.figure(figsize=(12, 5))
plt.plot(tel1['Distance'], tel1['Speed'], label='VER Speed')
plt.plot(tel2['Distance'], tel2['Speed'], label='HAM Speed')

plt.title("Speed Trace Comparison - Ham vs VER")
plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.legend()
plt.grid(True)
plt.show()

