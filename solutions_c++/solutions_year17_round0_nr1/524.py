/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: bernardo
 *
 * Created on April 7, 2017, 11:33 PM
 */

#include <cstdlib>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>
#include <string>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int T; cin>>T;
    for(int t=0;t<T;t++) {
       
        string oven;
        cin>>oven;
        int k; 
        cin>>k;
        int N=oven.size();
        int flips = 0;
        for(int i=0;i<N-k+1;i++) {
            if(oven[i]=='-') {
                //flip position i
                flips++;
                for(int j=i;j<i+k;j++) {
                    if(oven[j]=='-') {
                        oven[j]='+';
                    }
                    else {
                        oven[j]='-';
                    }
                }
                
            }
        }
        bool good = true;
        for(int i=0;i<k;i++) {
            if(oven[N -1-i]=='-') {
                good = false;
            }
        }
        if(good) {            
            cout<<"Case #"<<t+1<<": "<<flips<<endl;
        } else {
            cout<<"Case #"<<t+1<<": IMPOSSIBLE"<<endl;            
        }
        
        
        
    }
    return 0;
}

