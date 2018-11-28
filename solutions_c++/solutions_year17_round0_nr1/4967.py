/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: kevin
 *
 * Created on April 8, 2017, 3:21 PM
 */

#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <map>
#include <algorithm>

using namespace std;
int getFlips(string init, int k);

int main(int argc, char** argv) {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int num;
    cin >> num;
    for(int i = 0; i < num; i++){
        string init = "";
        int k = 0;
        cin>>init>>k;
        int ans = getFlips(init, k);
        if(ans == -1){
            cout<<"Case #" <<i + 1<<": "<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #" <<i + 1<<": "<<ans<<endl;
        }
    }
    return 0;
}

int getFlips(string init, int k){
    int size = init.length();
    int count = 0;
    for(int i = 0; i < size - k + 1; i++){
        if(init[i] == '-'){
            count++;
            for(int j = 0; j < k; j++){
                if(init[i + j] == '-'){
                    init[i + j] = '+';
                }
                else{
                    init[i + j] = '-';
                }
            }
        }
    }
    for(int i = 0; i < size; i++){
        if(init[i] == '-'){
            return -1;
        }
    }
    return count;
}