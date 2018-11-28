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


int n, p;
int r[100], rr[100];
int q[100][100];

void solve(){
    rep(i, 1, n){
        q[i][0] = 1;
        rr[i] = r[i];
    }
    int ans = 0;
    while (1){
        bool bk = 0, ct = 0;
        rep(i, 1, n){
            int *t = q[i];
            while (t[0] <= p && t[t[0]] * 10 < rr[i] * 9)
                t[0]++;
            if (t[0] > p){
                bk = 1;
                break;
            }
        }
        if (bk) break;
        while (1){
            rep(i, 1, n){
                int *t = q[i];
                if (t[0] > p){
                    bk = 1;
                    break;
                }
                if (t[t[0]] * 10 > rr[i] * 11){
                    ct = 1;
                    break;
                }
            }
            if (bk || ct) break;
            ans++;
            rep(i, 1, n)
                q[i][0]++;
        }
        if (bk) break;
        if (ct){
            rep(i, 1, n)
                rr[i] += r[i];
            continue;
        }

    }
    printf("%d\n", ans);
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, Tcase = 0;
    cin>>T;
    while (T--){
        scanf("%d%d", &n, &p);
        rep(i, 1, n)
            scanf("%d", r + i);
        rep(i, 1, n){
            rep(j, 1, p){
                scanf("%d", q[i] + j);
            }
            sort(q[i] + 1, q[i] + p + 1);
        }
        printf("Case #%d: ", ++Tcase);
        solve();

    }
    return 0;
}
