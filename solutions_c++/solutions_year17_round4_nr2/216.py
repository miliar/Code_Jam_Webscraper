#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

const int maxn = 1100;
int a[maxn];
int b[maxn];
int s[maxn];
int w[maxn];
int n, m, k;
int ss[maxn];

bool cmp(int x) {
    for (int i = 1; i <= n; i++)
        if (ss[i] > x*i)
            return false;
    return true;
}
int work(int l, int r) {
    while (l < r) {
        int mid = (l+r)/2;
        
        if (!cmp(mid)) l = mid+1;
        else r = mid;
    }
    return l;
}
int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d", &n, &k, &m);
        memset(s,0,sizeof(s));
        memset(w,0,sizeof(w));
        for (int i = 1; i <= m; i++) {
            scanf("%d%d", &a[i], &b[i]);
            s[b[i]]++;
            w[a[i]]++;
            
        }
        ss[0] = 0;
        for (int i = 1; i <= n; i++) ss[i] = ss[i-1]+w[i];
        int tt = 0;
        for (int i = 1; i <= k; i++) tt = max(tt, s[i]);
        
        int ansx = work(tt, m);
        int ansy = 0;
        for (int i = 1; i <= n; i++) if (w[i] > ansx) ansy += w[i]-ansx;
        printf("Case #%d: %d %d\n", ++cas, ansx, ansy);
    }
    
}
