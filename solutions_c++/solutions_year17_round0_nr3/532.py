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
#include <set>
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

const int tab64[64] = {
    63,  0, 58,  1, 59, 47, 53,  2,
    60, 39, 48, 27, 54, 33, 42,  3,
    61, 51, 37, 40, 49, 18, 28, 20,
    55, 30, 34, 11, 43, 14, 22,  4,
    62, 57, 46, 52, 38, 26, 32, 41,
    50, 36, 17, 19, 29, 10, 13, 21,
    56, 45, 25, 31, 35, 16,  9, 12,
    44, 24, 15,  8, 23,  7,  6,  5};

int log2_64 (uint64_t value)
{
    value |= value >> 1;
    value |= value >> 2;
    value |= value >> 4;
    value |= value >> 8;
    value |= value >> 16;
    value |= value >> 32;
    return tab64[((uint64_t)((value - (value >> 1))*0x07EDD5E59A4E28C2)) >> 58];
}

int main(int argc, char** argv) {
    long T; cin>>T;
    for(long t=0;t<T;t++) {
        long N; 
        cin>>N;
        long K;
        cin>>K;
        //cout<<N<<" "<<K<<endl;
        //long l = log2(K)+1;
        long l = log2_64(K)+1;
        long twoToLminus1 = pow(2,l-1);
        long v = N / twoToLminus1;
        long L = N - twoToLminus1 +1;
        long P = K - twoToLminus1 +1 ;
        //cout<<N<<" "<<K<<" v:"<<v<<" l:"<<l<<" L:"<<L<<" P:"<<P<<endl;
        
        long b = v;
        long a = v-1;
        long d = pow(2, l-1);
        long c = L;
        
        long y = (d*a-c)/(a-b);
        long slot = b;
        if(P>y) {
            slot=a;
        }
        
        cout<<"Case #"<<t+1<<": "<<slot/2<<" "<<(slot-1)/2<<endl;   
        
        
    }
    return 0;
}

