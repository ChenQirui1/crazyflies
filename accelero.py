import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

logfile = open('log.csv', 'w')

URI = 'radio://0/80/250K'

def movement(Mr_Gi, Isaac, Don, Qirui, Time):
    for _ in range(Time):
        cf.commander.send_hover_setpoint(Mr_Gi, Isaac, Don, Qirui)
        for log_entry in logger:
            timestamp = log_entry[0]
            data = log_entry[1]
            logconf_name = log_entry[2]
            print('[%d][%s]: %s' % (timestamp, logconf_name, data))
            count = 1
            line = ""
            for key, value in data.items():
                if count % 3 != 0:
                    line += str(value) + ","
                else:
                    line += str(value) + "\n"
                    logfile.write(line)
                    line = ""
                count += 1
            if time.time() > endTime:
                break
        time.sleep(0.1)

def movementstart(Mr_Gi, Isaac, Don, Qirui, Time):

    for y in range(Time):
        cf.commander.send_hover_setpoint(Mr_Gi, Isaac, Don, y/Qirui)

        for log_entry in logger:
            timestamp = log_entry[0]
            data = log_entry[1]
            logconf_name = log_entry[2]
            print('[%d][%s]: %s' % (timestamp, logconf_name, data))
            count = 1
            line = ""
            for key, value in data.items():
                if count % 3 != 0:
                    line += str(value) + ","
                else:
                    line += str(value) + "\n"
                    logfile.write(line)
                    line = ""
                count += 1
            if time.time() > endTime:
                break
        time.sleep(0.1)

def movementend(Mr_Gi, Isaac, Don, Qirui, Time):

    for _ in range(Time):
        cf.commander.send_hover_setpoint(Mr_Gi, Isaac, Don, Qirui/y)

        for log_entry in logger:
            timestamp = log_entry[0]
            data = log_entry[1]
            logconf_name = log_entry[2]
            print('[%d][%s]: %s' % (timestamp, logconf_name, data))
            count = 1
            line = ""
            for key, value in data.items():
                if count % 3 != 0:
                    line += str(value) + ","
                else:
                    line += str(value) + "\n"
                    logfile.write(line)
                    line = ""
                count += 1
            if time.time() > endTime:
                break
        time.sleep(0.1)

def logacc(logger):
    for log_entry in logger:

        timestamp = log_entry[0]
        data = log_entry[1]
        logconf_name = log_entry[2]

        print('[%d][%s]: %s' % (timestamp, logconf_name, data))

if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    # Scan for Crazyflies and use the first one found
    print('Scanning interfaces for Crazyflies...')
    available = cflib.crtp.scan_interfaces()
    print('Crazyflies found:')
    for i in available:
        print(i[0])

    if len(available) == 0:
        print('No Crazyflies found, cannot run example')
    else:
        lg_acc = LogConfig(name='Acelerometer', period_in_ms=100)
        lg_acc.add_variable('acc.z', 'float')
        lg_acc.add_variable('acc.x', 'float')
        lg_acc.add_variable('acc.y', 'float')
        with SyncCrazyflie(available[0][0], cf = Crazyflie(rw_cache='./cache')) as scf:
            with SyncLogger(scf, lg_acc) as logger:
                endTime = time.time() + 1
                cf.param.set_value('kalman.resetEstimation', '1')
                time.sleep(0.1)
                cf.param.set_value('kalman.resetEstimation', '0')
                time.sleep(2)

                movement(0, 0, 0, 0.3, 10)
                movement(0.5, 0, 0 , 0.3, 50)
                    
logfile.close()

            







"""if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    p1 = multiprocessing.Process(target = logacc, args = (URI,))
    p2 = multiprocessing.Process(target = movement, args = (URI,))

    p1.start()
    p1.join()
"""
"""
# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)
URI = 'radio://0/77/250K'
logfile = open('log.txt', 'w')
time.sleep(2)

if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)
    # Scan for Crazyflies and use the first one found
    print('Scanning interfaces for Crazyflies...')
    available = cflib.crtp.scan_interfaces()
    print('Crazyflies found:')
    for i in available:
        print(i[0])

    if len(available) == 0:
        print('No Crazyflies found, cannot run example')
    # Initialize the low-level drivers (don't list the debug drivers)
    else:
        lg_stab = LogConfig(name='Stabilizer', period_in_ms=10)
        lg_stab.add_variable('acc.z', 'float')
        lg_stab.add_variable('acc.y', 'float')
        lg_stab.add_variable('acc.x', 'float')

    cf = Crazyflie(rw_cache='./cache')
    with SyncCrazyflie(available[0][0], cf=cf) as scf:
        with SyncLogger(cf, lg_stab) as logger:
            endTime = time.time() + 10

            for log_entry in logger:
                timestamp = log_entry[0]
                data = log_entry[1]
                logconf_name = log_entry[2]
                print('[%d][%s]: %s' % (timestamp, logconf_name, data))
                logfile.write(str(timestamp) + str(logconf_name) + str(data) +'\n')

                if time.time() > endTime:
                    break
    logfile.close()
"""
