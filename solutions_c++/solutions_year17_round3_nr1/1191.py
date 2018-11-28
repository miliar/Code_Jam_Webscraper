//
//  main.cpp
//  Ample Syrup
//
//  Created by Jiao Liu on 17-4-30.
//  Copyright (c) 2017年 Jiao Liu. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;
struct cake {
    double r,h;
};

bool operator ==(cake x, cake y)
{
    return x.h = y.h && x.r == y.r;
}

bool operator <(cake x, cake y)
{
//    if ((x.r * x.r + 2 * x.r * x.h) == (y.r * y.r + 2 * y.h * y.r)) {
//        return x.r > y.r;
//    }
//    else
//    {
//        return (x.r * x.r + 2 * x.r * x.h) > (y.r * y.r + 2 * y.h * y.r);
//    }
    return x.r > y.r;
}

int K,N;
vector<cake> panCakes;
double pi = 3.14159265359;

long double subSum(int index)
{
    long double sum = 0;
    double rad = panCakes[index].r;
    double hei = panCakes[index].h;
    sum += pi * rad * rad;
    sum += 2 * pi * rad * hei;
    vector<long double> temp;
    for (int i = index + 1; i < N; i++) {
        rad = panCakes[i].r;
        hei = panCakes[i].h;
        temp.push_back(2 * pi * rad * hei);
    }
    sort(temp.begin(), temp.end());
    reverse(temp.begin(), temp.end());
    for (int i = 0; i < K - 1; i++) {
        sum += temp[i];
    }
    return sum;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/liujiao1988/Desktop/Projects/Ample Syrup/A-large.in", "r", stdin);
    freopen("/Users/liujiao1988/Desktop/Projects/Ample Syrup/A-large.out", "w", stdout);
    int T;
    cin>>T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ",i);
        cin>>N>>K;
        panCakes.clear();
        for (int j = 0; j < N; j++) {
            cake p;
            cin>>p.r>>p.h;
            panCakes.push_back(p);
        }
        sort(panCakes.begin(), panCakes.end());
        long double maxSum = 0;
        for (int p = 0; p <= N - K; p++) {
            maxSum = max(maxSum, subSum(p));
        }
        printf("%.8Lf\n",maxSum);
    }
    return 0;
}

