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

ifstream in("/Users/daisy/Documents/GCJ/GCJinput/B-large.in");
ofstream out("/Users/daisy/Documents/GCJ/GCJoutput/BL.out");

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

void solveB(int number){
    string N;
    in >> N;
    int i, RB = -1, RL = -1;
    for (i = 0; i < N.length()-1; i ++) {
        if (N[i] < N[i+1]) {
            RB = i;
        }
        else if(N[i] > N[i+1]){
            RL = i;
            break;
        }
    }
    out << "Case #" << number << ": ";
    if (N.length() == 1){
        out << N << endl;
        return;
    }
    if (RL < 0){
        out << N << endl;
        return;
    }
    if (RB >= 0) {
        for (i = 0; i <= RB; i ++) {
            out << N[i];
        }
        out << char(N[RB+1]-1);
        for (i = RB+2; i < N.length(); i ++) {
            out << '9';
        }
        out << endl;
        return;
    }
    if (N[0]!='1') {
        out << char(N[0]-1);
    }
    for (i = 1; i < N.length(); i ++) {
        out << '9';
    }
    out << endl;
    return;
    
}
int main(){
    int T, t;
    in >> T;
    for (t = 1; t <= T; t ++) {
        solveB(t);
    }
    in.close();
    out.close();
    return 0;
}