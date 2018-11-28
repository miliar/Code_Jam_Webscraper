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

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1B/A-small-attempt1.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1B/A-small-attempt1.out")

#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1B/A-large.in")
#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1B/A-large.out")

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1B/A-test.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/1B/A-test.out")

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

int destination, n;

int speeds[1010];
int positions[1010];
long double minSpeed;

void In() {
    cin >> destination >> n;
    
    for(int i = 0; i < n; i++)
        cin >> positions[i] >> speeds[i];
}

void Out() {
    printf("%.7Lf", minSpeed);
}

void iteration() {
    minSpeed = -1;
    
    for(int i = 0; i < n; i++) {
        long double time = (destination - positions[i]) / (long double)speeds[i];
        long double speed = destination / time;
        if(minSpeed < 0 || speed < minSpeed)
            minSpeed = speed;
    }
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


