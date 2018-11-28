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

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/B-small-attempt0.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/B-small-attempt0.out")

#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/B-large.in")
#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/B-large.out")

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/B-test.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ_2017/Qual/B-test.out")

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

char number[20];

void In() {
    scanf("%s", number);
}

void Out() {
    int i = 0;
    while (number[i] == '0') {
        i++;
    }
    while(number[i])
    {
        cout << number[i];
        i++;
    }
}

void iteration() {
    
    for(int i = 0; number[i] != 0 && number[i+1] != 0; i++)
        if(number[i+1] < number[i]) {
            while(i > 0 && number[i] == number[i-1])
                i--;
            number[i]--;
            
            for(int j = i+1; number[j] != 0; j++)
                number[j] = '9';
            break;
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


