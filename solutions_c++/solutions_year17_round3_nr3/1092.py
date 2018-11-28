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

#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1C/C-small-1-attempt0.in")
#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1C/C-small-1-attempt0.out")

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1C/C-large.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1C/C-large.out")

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1C/C-test.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1C/C-test.out")

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

int n, k;

double u, p[52];

double result;

void In() {
    cin >> n >> k >> u;
    
    for(int i = 0; i < n; i++)
        cin >> p[i];
}

void Out() {
}

void iteration() {
    
    sort(p, p+n);
    
    for(int i = 0; i < n; i++) {
        double goal = i < n-1 ? p[i+1] : 1;
        double needed = (i + 1) * (goal - p[i]);
        if(needed > u)
            needed = u;
        u -= needed;
        
        for(int j = 0; j <= i; j++)
            p[j] += needed / (i+1);
    }
    
    result = 1;
    for(int i = 0; i < n; i++) {
        result *= p[i];
    }
    
    printf("%.7f", result);
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


