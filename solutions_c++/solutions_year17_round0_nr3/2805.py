//
//  main.cpp
//  FHC_Pattern
//
//  Created by Andriy Medvid on 11.01.15.
//  Copyright (c) 2015 Andriy Medvid. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
#include <memory.h>

using namespace std;

#define MAX_NUM 1000000000

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/C-small-2-attempt0.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/C-small-2-attempt0.out")

#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/C-large.in")
#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/C-large.out")

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/C-test.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/C-test.out")

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

long long n, k;

void In() {
    cin >> n >> k;
}

long long num;

void Out() {
    cout << num/2 << " " << (num - 1)/2;
}

void iteration() {
    long long pow = 0;
    long long kcopy = k;
    while (kcopy > 1) {
        kcopy /= 2;
        pow++;
    }
    
    long long one = 1;
    long long powered = one << pow;
    
    long long left = n - powered;
    
    long long full = left / powered;
    long long rest = left % powered;
    
    if(rest >= k - powered)
        num = full + 1;
    else
        num = full;
}

int main(int argc, const char * argv[]) {
    
    freopen(IN_NAME, "r", stdin);
    freopen(OUT_NAME, "w", stdout);
    
    int T;
    
    cin >> T;
    
    for(int tIter = 0; tIter < T; tIter++) {
        
        In();
        
        OutCase(tIter);
        
        iteration();
        
        Out();
        
        cout << endl;
    }
    
    return 0;
}


