#include <bits/stdc++.h>
using namespace std;
const int M = 1e3+10;
const double pi = acos(-1.0);

struct cake{
    int id;
    double r, h;
    double fa, ar;
}a[M];

double sum[M];
int vis[M];

bool cmp1(cake a, cake b) {
    return a.fa > b.fa;
}

bool cmp2(cake a, cake b) {
    return a.ar > b.ar;
}


int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int cas = 0;
    while(t --) {
        int n, k;
        scanf("%d%d", &n, &k);
        memset(vis, 0, sizeof(int)*(n+1));
        for(int i = 0; i < n; i ++) {
            scanf("%lf%lf", &a[i].r, &a[i].h);
            a[i].fa = a[i].r*a[i].r*pi;
            a[i].ar = a[i].r*2*a[i].h*pi;
            a[i].id = i;
        }
        sort(a, a+n, cmp2);
        double k1 = 0, k2 = a[k-1].ar;
        double mx = -1;
        for(int i = 0; i < k; i ++) {
            vis[a[i].id] = 1;
            k1 += a[i].ar;
            mx = max(a[i].r, mx);
        }
        double ans = mx*mx*pi + k1;
        sort(a, a+n, cmp1);
        for(int i = 0; i < n; i ++) {
            if(vis[a[i].id]) break;
            ans = max(ans, a[i].fa + a[i].ar + k1-k2);
        }
        printf("Case #%d: %.9f\n", ++cas, ans);
    }
}
