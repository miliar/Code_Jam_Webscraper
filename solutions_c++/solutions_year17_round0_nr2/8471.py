/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: UTENTE
 *
 * Created on 8 aprile 2017, 11.53
 */

#include <cstdlib>
#include<iostream>
#include<fstream>
#include <string>
#include <string.h>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    
    int ntot, i, sent, lenght;
    
    unsigned long long int n,j,k,tmp,tmp2,tmp3,max;
    
    ifstream in("input.txt");
    ofstream out("output.txt");
    
    in>>ntot;
    
    for(i=1;i<=ntot;i++){
        in>>n;
        if ( n<10){
            out<<"CASE #"<<i<<": "<<n<<endl;
            continue;
        }
        max = 9;
        for(j=n;j>0;j--){
            sent = 0;
            tmp=j;
            tmp2 = 9;
            while(tmp>0){
                tmp3=tmp2;
                tmp2 = tmp%10;
                tmp /= 10;
                if(tmp3<tmp2){
                    sent=1;
                    break;
                }
            }
            if(sent==0){
                max=j;
                out<<"CASE #"<<i<<": "<<max<<endl;
                break;
            }
        }
    }

    return 0;
}

