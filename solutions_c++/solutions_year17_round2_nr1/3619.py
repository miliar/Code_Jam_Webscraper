/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: kevin
 *
 * Created on April 22, 2017, 10:13 AM
 */

#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <map>
#include <algorithm>

using namespace std;

int main(int argc, char** argv) {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int num;
    cin >> num;
    for(int i = 0; i < num; i++){
        int distance, horses;
        float max = 0;
        cin>>distance>>horses;
        for(int j = 0; j < horses; j++){
            int start, speed;
            cin>>start>>speed;
            float time = float(distance-start)/speed;
            if(time > max){
                max = time;
            }
        }
        float ans = float(distance)/max;
        cout<<"Case #"<<i + 1<<": "<<fixed<<ans<<endl;
    }
    return 0;
}


