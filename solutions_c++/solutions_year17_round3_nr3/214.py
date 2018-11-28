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
typedef pair<int,int> pii;
//head

const int N = 222;
double p[N], u;
int n;
int main(){
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
    int T, tcase = 0;
    cin>>T;
    while (T--){
        scanf("%d%d", &n, &n);
        scanf("%lf", &u);
        rep(i, 1, n)
            scanf("%lf", p + i);
        sort(p + 1, p + n + 1);
        p[n + 1] = 1.1;
        rep(i, 1, n){
            u += p[i];
            if (p[i + 1] * i > u){
                rep(j, 1, i)
                    p[j] = min(1., u / i);
                break;

            }
        }
        double ans = 1;
        rep(i, 1, n){
            ans *= p[i];
        }
        printf("Case #%d: %.10f\n", ++tcase, ans);
    }
    return 0;
}
