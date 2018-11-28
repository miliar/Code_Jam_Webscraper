//
//  main.cpp
//  Cruise Control
//
//  Created by Jiao Liu on 17-4-23.
//  Copyright (c) 2017年 Jiao Liu. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[])
{
    freopen("/Users/liujiao1988/Desktop/Projects/Cruise Control/A-large.in", "r", stdin);
    freopen("/Users/liujiao1988/Desktop/Projects/Cruise Control/A-large.out", "w", stdout);
    int T;
    cin>>T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ",i);
        double D,N;
        cin>>D>>N;
        float time = 0;
        for (int j = 0; j < N; j++) {
            double k,s;
            cin>>k>>s;
            if ((D-k) / s > time) {
                time = (D-k)/s;
            }
        }
        printf("%.8f\n",D/time);
    }
    return 0;
}

