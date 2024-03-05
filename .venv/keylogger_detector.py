import subprocess
import sys

import psutil

t = 1
black_list = []
white_list = []

# removing the first argument from list of arguments
argumentList = sys.argv[1:]

while True:
    if t == 1:
        print("\nScanning in progress...")
    proc = subprocess.Popen('netstat -ano -p tcp | findStr "587 465 2525"', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    out, err = proc.communicate()

    output = out.decode()

    my_list = output.split(" ")
    #print(my_list)
    # PID will be the last number once split
    pid = my_list[-1]
    # obtain output from checking the application name of PID
    cmd_output = subprocess.getoutput(f'tasklist /fi "pid eq {pid}"')
    # to make finding process name easier, split cmd_output
    p_name = cmd_output.split()

    t += 1

    if "ESTABLISHED" in output:
        # delete empty array elements
        my_list = list(filter(None, my_list))
        # get the full IP address with port number from the last element from output
        port_num = my_list[-3]
        # split at the ':' to get port number at last index of array
        get_port = port_num.split(":")
        port = get_port[-1]

        # 13th element in p_name will always be application name
        p_name = p_name[13]
        p = psutil.Process(int(pid))

        if p_name not in white_list:
            print("KEYLOGGER DETECTED!")

            # terminate process if it exists in blacklist
            if p_name in black_list:
                p.kill()
                print("A programme that is in the blacklist is now running.\nThe process is terminated automatically..")
                t = 1
            # if process is not in whitelist, check if it should be
            elif p_name not in white_list:

                print("Pausing the application...\n")
                p.suspend()
                print("Applications' information has been discovered as being a threat....")
                print(f'Application name: {p_name}\n'
                      f'Process ID (PID): {pid}'
                      f'Trying to communicate on port {port}\n')
                selected = False

                while not selected:
                    safe = input("Whitelist this application? (Y/N): ").lower()

                    if safe == 'n':
                        print("Terminating the process...")
                        p.kill()
                        print("Adding to blacklist...")
                        black_list.append(p_name)
                        selected = True
                        t = 1

                    elif safe == 'y':
                        print("Resuming the process...")
                        p.resume()
                        print("Adding to the whitelist...")
                        white_list.append(p_name)
                        selected = True
                        t = 1

                    print("Whitelist:", white_list)
                    print("Blacklist:", black_list)