/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   LastWord.cpp
 * Author: kevin
 *
 * Created on February 14, 2017, 8:21 PM
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

bool isTidy(long long int num);
long long power(long long base, int pow);
/*
 * 
 */

int main(int argc, char** argv) {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int num;
    cin >> num;
    for(int i = 0; i < num; i++){
        long long int index = 0;
        cin >> index;
        if(isTidy(index)){
            cout<<"Case #" <<i + 1<< ": " <<index<<endl;
        }
        else{
            index /= 10;
            long long int count = 1;
            long long int ans = 9;
            while(!isTidy(index - 1)){
                index /= 10;
                //cout<<index<<endl;
                count++;
                //cout<<ans<<endl;
                long long thing = (9 * power(10, count - 1));
                //cout<<thing<<endl;
                ans += thing;
                //cout<<ans<<endl;
            }
            cout<<"Case #" <<i + 1<< ": " <<((index - 1) * power(10, count) + ans)<<endl;  
        }
    }
    return 0;
}

bool isTidy(long long int num){
    long long int index = num % 10;
    num /= 10;
    while(num > 0){
        if(index < num % 10){
            return false;
        }
        index = num % 10;
        num /= 10;
    }
    return true;
}

long long power(long long base, int pow){
    if(pow == 0){
        return 1;
    }
    if(pow == 1){
        return base;
    }
    if(pow % 2 == 0){
        return power(base, pow/2) * power(base, pow/2);
    }
    return base * power(base, pow/2) * power(base, pow/2);
}