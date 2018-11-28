//
//  main.cpp
//  A
//
//  Created by 黄宇凡 on 2017/5/13.
//  Copyright © 2017年 黄宇凡. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int T;
int N;
int G[105],P;
int num[5];

int main(int argc, const char * argv[]) {
    freopen("A-large.in","r",stdin);
    freopen("A-larege-out.txt","w",stdout);
    cin >> T;
    int cas = 0;
    while(T--){
        cin >> N >> P;
        memset(num,0,sizeof(num));
        for(int i = 1;i <= N;i++){
            scanf("%d",&G[i]);
            G[i] = G[i] % P;
            num[G[i]]++;
        }
        int ans = 0;
        if(P == 2){
            ans = num[0] + (num[1] + 1) / 2;
        }else if(P == 3){
            ans = num[0];
            int t = min(num[1],num[2]);
            num[1] -= t;
            num[2] -= t;
            ans += t;
            ans += (num[1] + 2) / 3 + (num[2] + 2) / 3;
        }else if(P == 4){
            ans = num[0];
            int t = min(num[1],num[3]);
            ans += t;
            num[1] -= t;
            num[3] -= t;
           // int tt = num[2] / 2;
           // ans += tt;
            if(num[1] == 0) swap(num[1],num[3]);
           // num[2] -= tt * 2;
            int xx = min(num[1] / 2,num[2]);
            num[1] -= xx * 2;
            num[2] -= xx;
            ans += xx;
            ans += num[1] / 4;
            num[1] %= 4;
            ans += (num[2] / 2);
            num[2] %= 2;
            if(num[1] + num[2] > 0) ans++;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
