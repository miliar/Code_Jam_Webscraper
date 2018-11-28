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

const int N = 1011;
const double pi = acos(-1.0);
int n, k;
//int h[N], r[N];
pii cake[N]; // (r, h)
ll tmp[N];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, tcase = 0;
    cin>>T;
    while (T--){
        scanf("%d%d", &n, &k);
        rep(i, 1, n){
            scanf("%d%d", &cake[i].fi, &cake[i].se);
        }
        printf("Case #%d: ", ++tcase);
        sort(cake + 1, cake + n + 1);

        rep(i, 1, k - 1){
            tmp[i] = (ll)cake[i].fi * cake[i].se;
        }
        double ans = 0;
        rep(i, k, n){
            double now = (ll)cake[i].fi * cake[i].fi * pi + (ll)cake[i].fi * cake[i].se * pi * 2;
            sort(tmp + 1, tmp + i);
            reverse(tmp + 1, tmp + i);
            rep(j, 1, k - 1){
                now += 2 * pi * tmp[j];
            }
            if (ans < now) ans = now;
            tmp[i] = (ll)cake[i].fi * cake[i].se;
        }

        printf("%.10f\n", ans);
    }
    return 0;
}
