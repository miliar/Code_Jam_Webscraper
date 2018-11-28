//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by Jiao Liu on 17-4-8.
//  Copyright (c) 2017年 Jiao Liu. All rights reserved.
//

#include <iostream>

using namespace std;

long findFirstBlank(string s)
{
    long index = s.length();
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '-') {
            index = i;
            break;
        }
    }
    return index;
}

int minFlip(string s, int k)
{
    int num = 0;
    long p = findFirstBlank(s);
    while (s.length() - p >= k) {
        for (long i = p; i < p + k; i++) {
            if (s[i] == '+') {
                s[i] = '-';
            }
            else
            {
                s[i] = '+';
            }
        }
        p = findFirstBlank(s);
        num++;
    }
    if (p == s.length()) {
        return num;
    }
    return -1;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/liujiao1988/Desktop/Projects/Oversized Pancake Flipper/A-large.in", "r", stdin);
    freopen("/Users/liujiao1988/Desktop/Projects/Oversized Pancake Flipper/A-large.out", "w", stdout);
    int T,K;
    string S;
    cin>>T;
    for (int i = 1; i <= T; i++) {
        cin>>S>>K;
        printf("Case #%d: ",i);
        int flip = minFlip(S,K);
        if (flip == -1) {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<flip<<endl;
        }
    }
    return 0;
}

