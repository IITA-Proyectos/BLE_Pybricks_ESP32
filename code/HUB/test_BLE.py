from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub(broadcast_channel=4, observe_channels=[5])

sensor_distancia = UltrasonicSensor(Port.F)
sensor_tacto = ForceSensor(Port.A)

while True:
    sensor_value_distance = sensor_distancia.distance() # Leo el valor del sensor de distancia
    sensor_value_touch = sensor_tacto.pressed(force=3)
    data_send = [sensor_value_distance, sensor_value_touch] # lo almaceno en una lista
    hub.ble.broadcast(data_send) # comando para enviarlo 
    print(f"Enviado {data_send}")

    data_get = hub.ble.observe(5)
    if data_get != None:
        mensaje, pi, counter = data_get
        print(f"Recibido: {data_get}")
    wait(10)


