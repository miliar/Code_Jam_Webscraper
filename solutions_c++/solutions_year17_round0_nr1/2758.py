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

#define MAX_LEN 1002

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/A-small-attempt0.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/A-small-attempt0.out")

#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/A-large.in")
#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/A-large.out")

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/A-test.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/A-test.out")

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

int k;
char cakes[MAX_LEN];

int moves[MAX_LEN];

int movesCount = 0;

void In() {
    scanf("%s", cakes);
    cin >> k;
}

void Out() {
    if(movesCount < 0)
        cout << "IMPOSSIBLE";
    else
        cout << movesCount;
}

int cakesLength() {
    for(int i = 0; i < MAX_LEN; i++)
        if(cakes[i] == 0)
            return i;
    return 0;
}

void iteration() {
    memset(moves, 0, MAX_LEN*sizeof(int));
    movesCount = 0;
    
    int length = cakesLength();
    
    for(int i = 0; i <= length - k; i++)
        if(((moves[i]&1) == 1 && cakes[i] == '+') ||
           ((moves[i]&1) == 0 && cakes[i] == '-')) {
            for(int j = i; j < i + k; j++)
                moves[j] ++;
            movesCount++;
        }
    
    for(int i = length - k + 1; i < length; i++)
        if(((moves[i]&1) == 1 && cakes[i] == '+') ||
           ((moves[i]&1) == 0 && cakes[i] == '-')){
            movesCount = -1;
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


