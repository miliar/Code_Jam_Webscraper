/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: bernardo
 *
 * Created on April 7, 2017, 11:18 PM
 */

#include <cstdlib>
#include <unordered_map>
#include <list>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

/*
 * 
 */
long getNumber(const vector<int> & digits) {
    int base = 10;
    long factor = 1;
    int size = digits.size();
    long number = 0;
    for(int i=0;i<size;i++) {
        number+=digits[size-1-i]*factor;
        factor*=base;
    }
    return number;
}
long getTidy(long N) {    
    vector<int> digits;
    while(N!=0) {
        digits.push_back(N%10);        
        N/=10;
    }
    reverse(digits.begin(), digits.end());
    
    int size = digits.size();    
    for(int i=size-1;i>0;i--) {  
        if(digits[i]<digits[i-1]) {
            digits[i-1]--;
            for(int j=i;j<size;j++) {
                digits[j]=9;
            }
        }
    }
    return getNumber(digits);
}
int main(int argc, char** argv) {

    int T; cin>>T;
    
    for(int t=0;t<T;t++) {
        
        long N; 
        cin>>N;
        cout<<"Case #"<<t+1<<": "<<getTidy(N)<<endl;
    }
    return 0;
}

