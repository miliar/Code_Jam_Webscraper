//
//  main.cpp
//  Core Training
//
//  Created by Jiao Liu on 17-4-30.
//  Copyright (c) 2017年 Jiao Liu. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;
int N,K;
long double U;
vector<long double>group;

void updateGroup()
{
    if (U < 1e-8) {
        return;
    }
    sort(group.begin(), group.end());
    long double minV = group[0];
    int numM = 1;
    long double next = 1;
    for (int i = 1; i < group.size(); i++) {
        if (group[i] == minV) {
            numM ++;
        }
        else
        {
            next = group[i];
            break;
        }
    }
    
    if ((next-minV) * numM > U) {
        long double value = U / numM;
        for (int i = 0; i < numM; i++) {
            group[i] += value;
        }
        U = 0;
    }
    else
    {
        for (int i = 0; i < numM; i++) {
            group[i] = next;
        }
        U -= (next-minV) * numM;
        updateGroup();
    }
}

int main(int argc, const char * argv[])
{
    freopen("/Users/liujiao1988/Desktop/Projects/Core Training/C-small-1-attempt0.in", "r", stdin);
    freopen("/Users/liujiao1988/Desktop/Projects/Core Training/C-small-1-attempt0.out", "w", stdout);
    int T;
    cin>>T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ",i);
        cin>>N>>K>>U;
        group.clear();
        for (int j = 0; j < N; j++) {
            long double p;
            cin>>p;
            group.push_back(p);
        }
        updateGroup();
        long double aip = 1;
        for (int j = 0; j < N; j++) {
            aip *= group[j];
        }
        printf("%.8Lf\n", aip);
    }
    return 0;
}

