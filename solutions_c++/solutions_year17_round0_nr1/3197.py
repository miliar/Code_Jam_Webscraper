//
//  2017_A.cpp
//  GCJ
//
//  Created by 陶源 on 4/8/17.
//  Copyright © 2017 daisynowhere. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ifstream in("/Users/daisy/Documents/GCJ/GCJinput/A-large.in");
ofstream out("/Users/daisy/Documents/GCJ/GCJoutput/AL.out");

void solveA(int number){
    string S;
    int i, K, times = 0;
    bool can = true;
    in >> S >> K;
    for (i = 0; i <= S.length() - K; i ++) {
        if (S[i]=='+') {
            continue;
        }
        else{
            for (int j = 0; j < K; j ++) {
                S[i+j] = (S[i+j]=='+')?'-':'+';
            }
            times ++;
        }
    }
    for (i = int(S.length()) - K; i < S.length(); i ++) {
        if(S[i]=='-'){
            can = false;
            break;
        }
    }
    out << "Case #" << number << ": ";
    if(can)
        out << times<< endl;
    else
        out << "IMPOSSIBLE" << endl;
}


int main(){
    int T, t;
    in >> T;
    for (t = 1; t <= T; t ++) {
        solveA(t);
    }
    in.close();
    out.close();
    return 0;
}