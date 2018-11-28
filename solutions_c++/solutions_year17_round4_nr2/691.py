#include<bits/stdc++.h>
using namespace std;
#define s(x)        scanf("%d",&x);
#define pb(x)       push_back(x);
#define maxn 100005
#define pff(x)  printf("Case #%d: ");
#define pf(x,y)  printf("%d %d\n", l, check(l));
#define f(i,j,n)    for(int i = j; i <= n; i++)
#define ll long long
int a[1005], b[1005];
int T, n, c, m, x, y;
int check(int v) {
    int ret = 0, ss = 0;
    f(i,1,n) {
        ss += a[i];
        if(ss > i * v)return -1;
        ret += max(0, a[i] - v);
    }
    return ret;
}
int main() {
    s(T);
    f(j,1,T) {
        int ma = 0;
        s(n);
        s(c);
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        f(i,1,m) {
            s(x);
            s(y);
            a[x]++;
            b[y]++;
            ma = max(b[y], ma);
        }
        int l = ma, r = m;
        while(r - l > 1) {
            int mid = (l + r) >> 1;
            if(check(mid) >= 0)r = mid; else l = mid;
        }
        if(check(l) < 0)l++;
        pff(j);
        pf(l, check(l));
    }
    return 0;
}