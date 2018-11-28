//
//  Created by TaoSama on 2017-04-08
//  Copyright (c) 2016 TaoSama. All rights reserved.
//
#pragma comment(linker, "/STACK:102400000,102400000")
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <set>
#include <vector>

using namespace std;
#define pr(x) cerr << #x << " = " << x << "  "
#define prln(x) cerr << #x << " = " << x << endl
const int N = 1e5 + 10, INF = 0x3f3f3f3f, MOD = 1e9 + 7;

int n, k;
int f[N];
char s[N];

int main() {

   freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t; scanf("%d", &t);
    while(t--) {
        scanf("%s%d", s, &k);
        n = strlen(s);

        int sum = 0, ans = 0;
        for(int i=0;i<n;i++){
            if(s[i]=='-') f[i]=0;
            else f[i]=1;
        }
        for(int i=0;i<n-k+1;i++){
            if(f[i]==0){
                for(int j=0;j<k;j++) f[i+j]=!f[i+j];
                ans++;
            }
        }
        for(int i=0;i<n;i++) if(f[i]==0) ans=-1;
        static int kase = 0;
        printf("Case #%d: ", ++kase);
        if(ans == -1) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }

    return 0;
}
