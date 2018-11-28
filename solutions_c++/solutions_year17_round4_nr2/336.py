//
//  main.cpp
//  B
//
//  Created by 黄宇凡 on 2017/5/13.
//  Copyright © 2017年 黄宇凡. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

int T;
int N;
int M;
int P[1005],B[1005];
int cnt[1005],num[1005];
int pre[1005];

int main(int argc, const char * argv[]) {
    freopen("B-large.in","r",stdin);
    freopen("B-large-out.txt","w",stdout);
    int T;
    cin >> T;
    int cas = 0;
    while(T--){
        int c;
        memset(num,0,sizeof(num));
        memset(cnt,0,sizeof(cnt));
        cin >> N >> c >> M;
        for(int i = 1;i <= M;i++){
            scanf("%d%d",&P[i],&B[i]);
            cnt[B[i]]++;
            num[P[i]]++;
        }
        int ans = 0;
        for(int i = 1;i <= c;i++){
            ans = max(cnt[i],ans);
        }
        int now = 0;
        for(int i = 1;i <= N;i++){
            now += num[i];
            ans = max(ans,(now + i - 1) / i);
        }
        int ret = 0;
        for(int i = 1;i <= N;i++){
            ret += max(0,num[i] - ans);
        }
        printf("Case #%d: %d %d\n",++cas,ans,ret);
    }
    return 0;
}
