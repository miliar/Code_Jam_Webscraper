//
//  main.cpp
//  Bathroom Stalls
//
//  Created by Jiao Liu on 17-4-8.
//  Copyright (c) 2017年 Jiao Liu. All rights reserved.
//

#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, const char * argv[])
{
    freopen("/Users/liujiao1988/Desktop/Projects/Bathroom Stalls/C-small-2-attempt0.in", "r", stdin);
    freopen("/Users/liujiao1988/Desktop/Projects/Bathroom Stalls/C-small-2-attempt0.out", "w", stdout);
    int T;
    cin>>T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ",i);
        long long N,K;
        cin>>N>>K;
        long long deep = log2(N)+1;
        long long step = log2(K)+1;
        long long maxLR,minLR;
        if (deep == step) {
            maxLR = minLR = 0;
        }
        else
        {
            long long p = powl(2, step);
            long long q = powl(2, step-1);
            long long mean = (N - p + 1) / p;
            long long remain = (N - p + 1) % p;
            if (remain <= q) {
                if (remain >= K - q + 1) {
                    maxLR = mean + 1;
                    minLR = mean;
                }
                else
                {
                    maxLR = minLR = mean;
                }
            }
            else
            {
                if (remain - q < K - q + 1) {
                    maxLR = mean + 1;
                    minLR = mean;
                }
                else
                {
                    maxLR = minLR = mean + 1;
                }
            }
        }
        cout<<maxLR<<" "<<minLR<<endl;
    }
    return 0;
}

