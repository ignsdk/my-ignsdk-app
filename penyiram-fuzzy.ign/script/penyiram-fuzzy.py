# menggunakan cara perhitungan COG dari skripsi kang firdaus
import random
import os
import time
import sys

def suhu_membership(suhu):
    suhu_dict = {}
    temp = 0
    
    # Cold : -10 to 0 tetap, 0 to 3 turun
    if suhu < -10 or suhu > 3:
        suhu_dict.update({'cold':0})
    elif -10 <= suhu <= 0:
        suhu_dict.update({'cold':1.0})
    elif 0 < suhu <= 3:
        temp = -(suhu-3.0)/( 3.0 - 0)
        suhu_dict.update({'cold':temp})
        
    # Cool : 0 to 3 naik, 3 to 12 tetap, 12 to 15 turun
    if suhu < 0 or suhu > 15:
        suhu_dict.update({'cool':0})
    elif 0 <= suhu < 3:
        temp = (suhu - 0) / (3.0 - 0)
        suhu_dict.update({'cool':temp})
    elif 3 <= suhu <= 12:
        suhu_dict.update({'cool':1.0})
    elif 12 < suhu <= 15:
        temp = -(suhu-15.0)/( 15.0 - 12.0)
        suhu_dict.update({'cold':temp})
        
    # Normal : 12 to 15 naik, 15 to 24 tetap, 24 to 27 turun
    if suhu < 12 or suhu > 27:
        suhu_dict.update({'normal':0})
    elif 12 <= suhu < 15:
        temp = (suhu - 12.0) / (15.0 - 12.0)
        suhu_dict.update({'normal':temp})
    elif 15 <= suhu <= 24:
        suhu_dict.update({'normal':1.0})
    elif 24 < suhu <= 27:
        temp = -(suhu-27.0)/( 27.0 - 24.0)
        suhu_dict.update({'normal':temp})
        
    # Warm : 24 to 27 naik, 27 to 36 tetap, 36 to 39 turun
    if suhu < 24 or suhu > 39:
        suhu_dict.update({'warm':0})
    elif 24 <= suhu < 27:
        temp = (suhu - 24.0) / (27.0 - 24.0)
        suhu_dict.update({'warm':temp})
    elif 27 <= suhu <= 36:
        suhu_dict.update({'warm':1.0})
    elif 36 < suhu <= 39:
        temp = -(suhu-39.0)/( 39.0 - 36.0)
        suhu_dict.update({'warm':temp})
        
    # Hot : 36 to 39 naik, 39 to 50 tetap
    if suhu < 36 or suhu > 50:
        suhu_dict.update({'hot':0})
    elif 36 <= suhu < 39:
        temp = (suhu - 36.0) / (39.0 - 36.0)
        suhu_dict.update({'hot':temp})
    elif 39 <= suhu <= 50:
        suhu_dict.update({'hot':1.0})
    
    return suhu_dict
    

def lembab_membership(lembab):
    lembab_dict = {}
    temp = 0
    
    # Dry : 0 to 10 tetap, 10 to 20 turun
    if lembab < 0 or lembab > 20:
        lembab_dict.update({'dry':0})
    elif 0 <= lembab <= 10:
        lembab_dict.update({'dry':1.0})
    elif 10 < lembab <= 20:
        temp = -(lembab-20.0)/( 20.0 - 10.0)
        lembab_dict.update({'dry':temp})
        
    # Moist : 10 to 20 naik, 20 to 40 tetap, 40 to 50 turun
    if lembab < 10 or lembab > 50:
        lembab_dict.update({'moist':0})
    elif 10 <= lembab < 20:
        temp = (lembab - 10.0) / (20.0 - 10.0)
        lembab_dict.update({'moist':temp})
    elif 20 <= lembab <= 40:
        lembab_dict.update({'moist':1.0})
    elif 40 < lembab <= 50:
        temp = -(lembab-50.0)/( 50.0 - 40.0)
        lembab_dict.update({'moist':temp})
    
    # Wet : 40 to 50 naik, 50 to 70 tetap
    if lembab < 40 or lembab > 70:
        lembab_dict.update({'wet':0})
    elif 40 <= lembab < 50:
        temp = (lembab - 40.0) / (50.0 - 40.0)
        lembab_dict.update({'wet':temp})
    elif 50 <= lembab <= 70:
        lembab_dict.update({'wet':1.0})
    
    return lembab_dict

def zero_attribute_delimiter(data_dict):
    temp_dict = {}
    for key in data_dict:
        if data_dict[key] != 0:
            temp_dict.update({key:data_dict[key]})
    
    return temp_dict
    
def duration_inference(data_suhu, data_lembab):
    duration_dict = {}
    long_choice = []
    medium_choice = []
    short_choice = []
    temp = 0
    
    # if suhu = COLD and lembab = DRY then durasi = LONG
    if data_suhu['cold'] and data_lembab['dry'] :
        temp = min(data_suhu['cold'], data_lembab['dry'])
        long_choice.append(temp)
        
    # if suhu = COOL and lembab = DRY then durasi = LONG
    if data_suhu['cool'] and data_lembab['dry'] :
        temp = min(data_suhu['cool'], data_lembab['dry'])
        long_choice.append(temp)
        
    # if suhu = NORMAL and lembab = DRY then durasi = LONG
    if data_suhu['normal'] and data_lembab['dry'] :
        temp = min(data_suhu['normal'], data_lembab['dry'])
        long_choice.append(temp)
        
    # if suhu = WARM and lembab = DRY then durasi = LONG
    if data_suhu['warm'] and data_lembab['dry'] :
        temp = min(data_suhu['warm'], data_lembab['dry'])
        long_choice.append(temp)
        
    # if suhu = HOT and lembab = DRY then durasi = LONG
    if data_suhu['hot'] and data_lembab['dry'] :
        temp = min(data_suhu['hot'], data_lembab['dry'])
        long_choice.append(temp)
        
    # if suhu = COLD and lembab = MOIST then durasi = LONG
    if data_suhu['cold'] and data_lembab['dry'] :
        temp = min(data_suhu['cold'], data_lembab['dry'])
        long_choice.append(temp)
        
    # if suhu = COOL and lembab = MOIST then durasi = MEDIUM
    if data_suhu['cool'] and data_lembab['moist'] :
        temp = min(data_suhu['cool'], data_lembab['moist'])
        medium_choice.append(temp)
        
    # if suhu = NORMAL and lembab = MOIST then durasi = MEDIUM
    if data_suhu['normal'] and data_lembab['moist'] :
        temp = min(data_suhu['normal'], data_lembab['moist'])
        medium_choice.append(temp)
        
    # if suhu = WARM and lembab = MOIST then durasi = MEDIUM
    if data_suhu['warm'] and data_lembab['moist'] :
        temp = min(data_suhu['warm'], data_lembab['moist'])
        medium_choice.append(temp)
        
    # if suhu = HOT and lembab = MOIST then durasi = MEDIUM
    if data_suhu['hot'] and data_lembab['moist'] :
        temp = min(data_suhu['hot'], data_lembab['moist'])
        medium_choice.append(temp)
        
    # if suhu = COLD and lembab = WET  then durasi = SHORT
    if data_suhu['cold'] and data_lembab['wet'] :
        temp = min(data_suhu['cold'], data_lembab['wet'])
        short_choice.append(temp)
        
    # if suhu = COOL and lembab = WET then durasi = SHORT
    if data_suhu['cold'] and data_lembab['wet'] :
        temp = min(data_suhu['cold'], data_lembab['wet'])
        short_choice.append(temp)
        
    # if suhu = NORMAL and lembab = WET then durasi = SHORT
    if data_suhu['normal'] and data_lembab['wet'] :
        temp = min(data_suhu['normal'], data_lembab['wet'])
        short_choice.append(temp)
        
    # if suhu = WARM and lembab = WET then durasi = SHORT
    if data_suhu['warm'] and data_lembab['wet'] :
        temp = min(data_suhu['warm'], data_lembab['wet'])
        short_choice.append(temp)
        
    # if suhu = HOT and lembab = WET then durasi = SHORT
    if data_suhu['hot'] and data_lembab['wet'] :
        temp = min(data_suhu['hot'], data_lembab['wet'])
        short_choice.append(temp)
        
    if len(long_choice) != 0:
        duration_dict.update({'long':max(long_choice)})
    else:
        duration_dict.update({'long':0})
    if len(medium_choice) != 0:
        duration_dict.update({'medium':max(medium_choice)})
    else:
        duration_dict.update({'medium':0})
    if len(short_choice) != 0:
        duration_dict.update({'short':max(short_choice)})
    else:
        duration_dict.update({'short':0})
        
    # rand_point = [24, 28, 32, 36, 40, 48, 60, 70, 80, 90]
    rand_point = []
    
    if duration_dict['short'] != 0:
        rand_point += range(0, 29, random.randint(1, 11))
    if duration_dict['medium'] != 0:
        rand_point += range(20, 49, random.randint(1, 11))
    if duration_dict['long'] != 0:
        rand_point += range(40, 91, random.randint(1, 11))
   
    # Short : 0  to 20 tetap, 20 to 28 turun
    short_point = []
    for point in rand_point:
        if point < 0 or point > 28:
            pass
        elif 0 <= point <= 20:
            short_point.append(point)
        elif 20 < point <= 28:
            short_point.append(point)
            
    # Medium : 20 to 28 naik, 28 to 40 tetap, 40 to 48 turun
    medium_point = []
    for point in rand_point:
        if point < 20 or point > 48:
            pass
        elif 20 <= point < 28:
            medium_point.append(point)
        elif 28 <= point <= 40:
            medium_point.append(point)
        elif 40 < point <= 48:
            medium_point.append(point)
    
    # Long : 40 to 48 naik, 48 to 90 tetap
    long_point = []
    for point in rand_point:
        if point < 40 or point > 90:
            pass
        elif 40 <= point < 48:
            long_point.append(point)
        elif 48 <= point <= 90:
            long_point.append(point)
    

    
    temp1 = (sum(short_point)) * duration_dict['short'] + (sum(medium_point)) * duration_dict['medium'] + (sum(long_point)) * duration_dict['long'] 
    temp2 = (len(short_point)) * duration_dict['short'] + (len(medium_point)) * duration_dict['medium'] + (len(long_point)) * duration_dict['long'] 
    output = temp1 / temp2
    
    return output

# parameter input dari luar sistem
suhu = int(sys.argv[2])
lembab = int(sys.argv[1])

# fuzzyfikasi
raw_data_suhu = suhu_membership(suhu)
raw_data_lembab = lembab_membership(lembab)

# inferensi
duration = duration_inference(raw_data_suhu, raw_data_lembab)
print 'duration : ', duration, ' menit'

