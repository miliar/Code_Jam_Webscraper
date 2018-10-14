#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:09:35 2017

@author: Jacobo
"""



def main():
    res=open('./large1.sol','w')
        
    route='./A-large.in'
    #route='./1.test'
    with open(route,'r') as file:
        lines=file.readlines()
        nombre=int(lines[0])
        i=1
        case=1
        while i < len(lines):
            ligne=lines[i].split(' ')
            distance=int(ligne[0])
            chevaux=int(ligne[1])
            i+=1
            maxspeed=0
            for j in range(chevaux):
                lignecheval=lines[i+j].split(' ')
                position=int(lignecheval[0])
                vitesse=int(lignecheval[1])
                tempscheval=(distance-position)/vitesse
                if tempscheval>maxspeed:
                    maxspeed=tempscheval
            i+=chevaux
            vitesse=distance/maxspeed
            aecrire='Case #'+str(case)+': '+str("{:10.6f}".format(vitesse))+'\n'
            case+=1
            res.write(aecrire)
            
            
    res.close()