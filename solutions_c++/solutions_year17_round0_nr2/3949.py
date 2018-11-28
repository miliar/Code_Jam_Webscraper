//
//  main.cpp
//  Tidy Numbers
//
//  Created by Jiao Liu on 17-4-8.
//  Copyright (c) 2017年 Jiao Liu. All rights reserved.
//

#include <iostream>

using namespace std;
int up[20],low[20];

void outputMax(string num)
{
    low[0] = 0;
    long len = num.length();
    for (int i = 0; i < len; i++) {
        up[i] = low[i+1] = num[i] - '0';
    }
    long switchIndex = len;
    for (int i = 0; i < len; i++) {
        if (up[i] < low[i]) {
            switchIndex = i;
            break;
        }
    }
    if (switchIndex < len) {
        for (long i = switchIndex; i < len; i++) {
            up[i] = 9;
        }
        for (long i = switchIndex - 1; i >= 0; i--) {
            if (up[i] - 1 >= low[i]) {
                up[i] -= 1;
                break;
            }
            up[i] = 9;
        }
    }
    
    if (up[0] > 0) {
        cout<<up[0];
    }
    for (int i = 1; i < len; i++) {
        cout<<up[i];
    }
    cout<<endl;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/liujiao1988/Desktop/Projects/Tidy Numbers/B-large.in", "r", stdin);
    freopen("/Users/liujiao1988/Desktop/Projects/Tidy Numbers/B-large.out", "w", stdout);
    int T;
    cin>>T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ",i);
        string num;
        cin>>num;
        outputMax(num);
    }
    return 0;
}

