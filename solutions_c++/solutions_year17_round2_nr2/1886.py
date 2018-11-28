//
//  main.cpp
//  Stable Neigh-bors
//
//  Created by Jiao Liu on 17-4-23.
//  Copyright (c) 2017年 Jiao Liu. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;
int N,R,O,Y,G,B,V;

int main(int argc, const char * argv[])
{
    freopen("/Users/liujiao1988/Desktop/Projects/Stable Neigh-bors/B-small-attempt1.in", "r", stdin);
    freopen("/Users/liujiao1988/Desktop/Projects/Stable Neigh-bors/B-small-attempt1.out", "w", stdout);
    int T;
    cin>>T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ",i);
        cin>>N>>R>>O>>Y>>G>>B>>V;
        pair<string, int>maxP;
        vector<pair<string, int>> tp;
        int ls = 0;
        if (R>Y) {
            maxP = make_pair("R", R);
            tp.push_back(make_pair("Y", Y));
            ls = Y;
        }
        else
        {
            maxP = make_pair("Y", Y);
            tp.push_back(make_pair("R", R));
            ls = R;
        }
        
        if (maxP.second > B) {
            tp.push_back(make_pair("B", B));
            ls += B;
        }
        else
        {
            tp.push_back(maxP);
            ls += maxP.second;
            maxP = make_pair("B", B);
        }
        
        if (maxP.second > ls) {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            vector<string> outS;
            for (int i = 0; i < maxP.second; i++) {
                outS.push_back(maxP.first);
            }
            for (int i = 0; i < tp[0].second; i++) {
                outS[i] = outS[i].append(tp[0].first);
            }
            for (int i = 0; i < tp[1].second; i++) {
                outS[maxP.second - 1 - i] = outS[maxP.second - 1 - i] .append(tp[1].first);
            }
            for (int i = 0; i < maxP.second; i++) {
                cout<<outS[i];
            }
            cout<<endl;
        }
        
    }
    return 0;
}

