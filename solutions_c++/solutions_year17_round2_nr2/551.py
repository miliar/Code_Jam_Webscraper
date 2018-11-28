//
//  main.cpp
//  roundB
//
//  Created by didi on 2017/4/22.
//  Copyright © 2017年 didi. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <math.h>
#include <iomanip>
using namespace std;

ifstream in("/Users/didi/Desktop/roundB/roundB/B-small-attempt0.in");
ofstream out("/Users/didi/Desktop/roundB/roundB/B-small-attempt0.out");

void swap(int *a, int *b){
    int t=*a;
    *a=*b;
    *b=t;
}

char get_char(int c){
    char ret;
    switch (c) {
        case 0:
            ret = 'R';
            break;
        case 1:
            ret = 'Y';
            break;
        case 2:
            ret = 'B';
            break;
        default:
            ret = '\0';
            break;
    }
    return ret;
}

void solve(int test){
    out << "Case #" << test << ": ";
    int N;
    int color[6];
    in >> N;
    for (int i=0; i<6; i++) in >> color[i];
    int small_color[3];
    small_color[0] = color[0];
    small_color[1] = color[2];
    small_color[2] = color[4];
    int ind[3];
    for (int i=0; i<3; i++) ind[i] = i;
    for (int i=0; i<3; i++){
        for (int j=i+1; j<3; j++){
            if (small_color[ind[i]] < small_color[ind[j]]) swap(ind+i, ind+j);
        }
    }
    if (small_color[ind[0]] > small_color[ind[1]] + small_color[ind[2]]){
        out << "IMPOSSIBLE" << endl;
        return;
    }
    int cnt = 0;
    int need = small_color[ind[1]] + small_color[ind[2]] - small_color[ind[0]];
    for (int i=0; i<small_color[ind[0]]; i++){
        out << get_char(ind[0]);
        cnt++;
        if (cnt <= small_color[ind[1]]){
            out << get_char(ind[1]);
            if (cnt <= need)
                out << get_char(ind[2]);
        }else{
            out << get_char(ind[2]);
        }
    }
    out << endl;
}


int main(int argc, const char * argv[]) {
    int test = 0,T;
    in >> T;
    while (test++<T){
        solve(test);
    }
    in.close();
    out.close();
    return 0;
}
