//
//  main.cpp
//  17_round_1C_B
//
//
//
//

#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    freopen("B-large.in.txt", "r", stdin);
    freopen("B-large.out.txt", "w", stdout);
    int t, a, b, at, bt, ans;
    pair<pair<int, int>, bool> activity[205];
    pair<int, int> interval[205];
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        at=bt=720;
        ans=0;
        scanf("%d %d", &a, &b);
        for(int j=0; j<a; j++){
            scanf("%d %d", &activity[j].first.first, &activity[j].first.second);
            activity[j].second=0;
            bt-=(activity[j].first.second-activity[j].first.first);
        }
        for(int j=a; j<a+b; j++){
            scanf("%d %d", &activity[j].first.first, &activity[j].first.second);
            activity[j].second=1;
            at-=(activity[j].first.second-activity[j].first.first);
        }
        sort(activity, activity+a+b);
        activity[a+b]=activity[0];
        activity[a+b].first.first+=1440;
        for(int j=0; j<a+b; j++){
            interval[j].first=((activity[j].second+activity[j+1].second)*2)%3;
            interval[j].second=activity[j+1].first.first-activity[j].first.second;
        }
        sort(interval, interval+a+b);
        for(int j=0; j<a+b; j++){
            if(interval[j].first==0){
                if(bt>=interval[j].second) bt-=interval[j].second;
                else{
                    ans+=2;
                    interval[j].second-=bt;
                    bt=0;
                    at-=interval[j].second;
                }
            }else if(interval[j].first==1){
                if(at>=interval[j].second) at-=interval[j].second;
                else{
                    ans+=2;
                    interval[j].second-=at;
                    at=0;
                    bt-=interval[j].second;
                }
            }else ans+=1;
        }
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
