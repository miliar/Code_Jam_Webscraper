/*#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
#include<stdio.h>
#include<string.h>
#include<map>
#include<set>*/

#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define per(i,a,b) for (int i=(b);i>=(a);i--)
#define fi first
#define se second
#define all(x) (x).begin(),(x).end()
#define SZ(x) ((int)x.size())
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;
//head

//int n, m;
char cake[30][30];

#define rr (r + rb)
#define cc (c + cb)
#define ii (i + rb)
#define jj (j + cb)
void solve(int rb, int cb, int n, int m){
    int r, c;
    for (r = 1; r <= n; r++){
        for (c = 1; c <= m; c++){
            if (cake[rr][cc] != '?') break;
        }
        c = min(c, m);
        if (cake[rr][cc] != '?') break;
    }
    char tmp = cake[rr][cc];
    while (c < m){
        bool ok = 1;
        rep(i, 1, r)
            if (cake[ii][cc + 1] != '?') ok = 0;
        if (!ok) break;
        c++;
    }
    while (r < n){
        bool ok = 1;
        rep(j, 1, c)
            if (cake[rr + 1][jj] != '?') ok = 0;
        if (!ok) break;
        r++;
    }
    rep(i, 1, r)
    rep(j, 1, c)
        cake[ii][jj] = tmp;
    if (c < m) solve(rb, cb + c, r, m - c);
    if (r < n) solve(rb + r, cb, n - r, m);
}
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, tcase = 0;
    cin>>T;
    while (T--){
        int n, m;
        scanf("%d%d", &n, &m);
        rep(i, 1, n){
            scanf("%s", cake[i] + 1);
        }
        solve(0, 0, n, m);
        printf("Case #%d:\n", ++tcase);
        rep(i, 1, n){
            cout<<(cake[i] + 1)<<endl;
        }
    }
    return 0;
}
