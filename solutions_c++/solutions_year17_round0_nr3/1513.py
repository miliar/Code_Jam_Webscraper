//
//  main.cpp
//  gcj_Qualification
//
//  Created by didi on 2017/4/8.
//  Copyright © 2017年 didi. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ifstream in("/Users/didi/Desktop/gcj_Qualification/gcj_Qualification/C-large.in");
ofstream out("/Users/didi/Desktop/gcj_Qualification/gcj_Qualification/C-large.out");

void solve(int test){
    out << "Case #" << test << ": ";
    long long N,K;
    in >> N >> K;
    long long base = 1;
    long long now = N;
    long long min = 1, max =0;
    while (base < K){
        if (now % 2 == 1){
            long long min_t = min * 2 + max;
            long long max_t = max;
            min = min_t;
            max = max_t;
            now /= 2;
        }else{
            long long min_t = min;
            long long max_t = min + max * 2;
            min = min_t;
            max = max_t;
            now = (now - 1) / 2;
        }
        base = base * 2 + 1;
    }
    base = (base - 1) / 2;
    K -= base;
    long long ans;
    if (K <= max)
        ans = now + 1;
    else
        ans = now;
    long long l,r;
    if (ans % 2 == 1){
        l = ans / 2;
        r = ans / 2;
    }else{
        l = ans / 2;
        r = l - 1;
    }
    out << l << " " << r << endl;
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
