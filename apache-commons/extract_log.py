import fileinput
import time
import os
import sys

target_file = 'full.log'
init_flag = True  
time_kick = 1800

record_count = 0

def record_logs(time_count = 0, log_names = "reduced.log"):

    print("Frequency is: " + time_count + " seconds")
    log_names += "_reduced.log"
    print("log name is: " + log_names)

    time_kick = int(time_count)

    while True:

        if not os.path.exists(target_file):
            time.sleep(time_kick)
            continue

        try:
            ticks = time.time()
            if init_flag:
                f_w = open(log_names, 'w')
                with open(target_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    last_line = lines[-1]
                    f_w.write(ticks + " " + last_line + "\n")
                    record_count += 1

                init_flag = False
            else:
                f_w = open(log_names, 'a')
                with open(target_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    last_line = lines[-1]
                    f_w.write(ticks + " " + last_line + "\n")
                    record_count += 1

            f_w.close()
        except:
            pass

        time.sleep(time_kick)

record_logs(sys.argv[1],sys.argv[2])
