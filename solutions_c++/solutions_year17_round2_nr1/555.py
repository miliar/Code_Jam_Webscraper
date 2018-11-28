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

ifstream in("/Users/didi/Desktop/roundB/roundB/A-large.in");
ofstream out("/Users/didi/Desktop/roundB/roundB/A-large.out");

void solve(int test){
    out << "Case #" << test << ": ";
    long long D, N;
    in >> D >> N;
    long long K[1010];
    long long S[1010];
    for (int i=0; i<N; i++) in >> K[i] >> S[i];
    double T = 0;
    for (int i=0; i<N; i++){
        double now = 1.0*(D-K[i])/S[i];
        T = max(T, now);
    }
    double ans = 1.0*D/T;
    out << fixed << setprecision(6) << ans << endl;
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
