import json
import math as m

def load_journal(f_name):
    f = open(f_name,);
    data = json.load(f)
    return data;

def compute_phi(fil, event):
    tt=0;
    tf=0;
    ff=0;
    ft=0;
    tc=0;
    fc=0;
    ct=0;
    cf=0;
    data = load_journal(fil)
    for instance in data:
        if (event in instance['events'] and instance['squirrel'] is True):
            tt= tt + 1;
        if (event in instance['events'] and instance['squirrel'] is False):
            tf= tf + 1;
        if (event not in instance['events'] and instance['squirrel'] is True):
            ft= ft + 1;
        if (event not in instance['events'] and instance['squirrel'] is False):
            ff= ff + 1;
        if (event in instance['events']):
            tc= tc + 1;
        if (event not in instance['events']):
            fc= fc + 1;
        if (instance['squirrel'] is True):
            ct= ct + 1;
        if (instance['squirrel'] is False):
            cf= cf + 1;
    phi = (tt*ff - tf*ft)/m.sqrt(tc*fc*ct*cf);          
    return phi;


def compute_correlations(str):
    dict_phi = {};
    elements = load_journal(str);
    e_list =[]
    for event in elements:
        for e in event['events']:
            e_list.append(e);
    e_list = list(dict.fromkeys(e_list));
    for unique_e in e_list:
       phi =  compute_phi(str, unique_e);
       dict_phi[unique_e]= phi;
    return dict_phi;

def diagnose(str):
    maxim = float(-1);
    minim = float(1);
    dict = compute_correlations(str);
    for key in dict.keys():
        val =float(dict[key]);
        if(val>maxim):
            maxim =val;
            max_e = key;
        if(val<minim):
            minim =val;
            min_e = key;
    return (max_e, min_e);
