'''
Author: Diptangshu
Date: 27-11-22
Purpose: To keep track of attendence during college and school days
'''

import time


def percentage(dict1, dict2):
    '''function to return a dictionary containing the subjects and the attendence percentage'''
    return {k: dict2[k]/dict1[k]*100 for k, v in dict1.items()}


def countdays(dict1, dict2):
    '''function to calculate the number of days that can be skipped or the number of days that the student has to be present more in the class in order to secure 75% attendence'''
    cdict1 = dict1.copy()
    cdict2 = dict2.copy()
    dict3 = {}
    while(1):
        for k, v in percentage(cdict1, cdict2).items():
            if v >= 75:
                if v == 75:
                    dict3[k] = cdict1[k] - \
                        dict1[k] if cdict2[k] == dict2[k] else dict1[k]-cdict1[k]
                else:
                    cdict1[k] += 1
                    if percentage(cdict1, cdict2)[k] < 75:
                        cdict1[k] -= 1
                        dict3[k] = cdict1[k]-dict1[k]
            else:
                cdict1[k] += 1
                cdict2[k] += 1
        if dict3.keys() == dict1.keys():
            return dict3


if __name__ == '__main__':

    # your current total and present days dict (subjects and dates can be edited accordingly)
    # Total = {'ece101': 32, 'cs101': 34, 'ch101': 30, 'ce102': 24, 'ma101': 38, 'ec111': 9, 'ch111': 8, 'cs111': 10, 'me111': 10}
    # My_att = {'ece101': 26, 'cs101': 25, 'ch101': 24, 'ce102': 17, 'ma101': 29, 'ec111': 7, 'ch111': 8, 'cs111': 9, 'me111': 9}

    while(True):
        for keys, values in Total.items():
            while(1):
                info = input(f'{keys} : ').split(' ')
                # code to read and function according to OFF and OFF ALL
                if info[0] == 'OFF' or info[0] == 'OFFALL':
                    Total[keys] -= 1
                    break
                else:
                    if info[0] == 'A':  # absent input
                        # if info.count('A') > 1:
                        #     Total[keys] += (info.count('A')-1)
                        break
                    elif info[0] == 'P':  # present input
                        # if info.count('P') > 1:
                        #     Total[keys] += (info.count('P')-1)
                        #     My_att[keys] += (info.count('P')-1)
                        My_att[keys] += 1
                        break
                    else:
                        # error rehandling (without using try except exception)
                        print(
                            "Error : Only 'A', 'P', 'OFF' and 'OFFALL' are allowed as inputs")
            Total[keys] += 1
            # once OFFALL command entered, the rest of the subjects below it  will automatically be taken as OFF
            if info[0] == 'OFFALL':
                break
        # creating a dict 'percent' using the percentage func
        percent = percentage(Total, My_att)

        # --------------------using file handling to keep the record of attendence--------------------
        with open('C:\\Nayan\\Attendence\\attendence.txt', 'w') as f:
            f.write(
                f'Latest entry date : {time.asctime(time.localtime())}\n\nTotal Days : {Total}\n\nPresent : {My_att}\n\nAttendence Percentage : {percent}\n\n')
            for keys, values in percent.items():
                if values <= 75:
                    f.write(f"\nWARNING : {keys} HAS CRITICAL ATTENDENCE\n\n")
            f.write(
                f"\nNo. of Days that can be missed or to be recovered : {countdays(Total, My_att)}")
            f.close()

        # ------------------------printing into console---------------------

        # print(f'Total Days : {Total}\nPresent : {My_att}\nAttendence Percentage : {percent}\n')
        # for keys, values in percent.items():
        #     if values <= 75:
        #         print(f"\nWARNING : {keys} HAS CRITICAL ATTENDENCE\n\n")
        # print(f"No. of Days that can be missed or to be recovered{countdays(Total, My_att)}")

        # --------------------------------while loop continuation-----------------------------
        # (for checking purpose: to take only one input and then end the program)
        # break
        # time.sleep(24*60).....to run the program forever with 24 hours interval
