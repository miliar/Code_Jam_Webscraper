//
//  main.cpp
//  test
//
//  Created by 商占仝 on 2017/3/22.
//  Copyright © 2017年 bytedance. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

typedef long long LL;

//const int maxn = 1005;

LL n, k;

int main(){
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, cases = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%lld%lld", &n, &k);
        LL cnt = 1;
        int col;
        for(col = 1; ; ++col, cnt <<= 1ll){
            if(k <= cnt) break;
            k -= cnt;
        }
        n -= (1ll << (col - 1)) - 1;
        LL tot = 1ll << (col - 1);
        LL X = n / tot;
        LL Y = X + 1;
        LL ans;
        if(Y * k + X * (tot - k) > n) ans = X - 1;
        else ans = Y - 1;
        
        printf("Case #%d: %lld %lld\n", ++cases, ans - (ans >> 1), ans >> 1);
    }
    return 0;
}
