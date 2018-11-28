//created by missever

#include<bits/stdc++.h>
#define MAX 1000000007
using namespace std;
typedef long long LL;

int f[1005],a[1005],s;

bool check(int u) {
    int d;
    d = s = 0;
    for(int i = 1000; i > 0; i--) {
        if(f[i] > u) s += f[i] - u;
        d = max(0,d + f[i] - u);
    }
    return d == 0;
}

int main() {
//    freopen("B-large.in","r",stdin);
//    freopen("A.out","w",stdout);
    int t,n,m,c,i,x,y;
    int l,r,mid;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas++) {
        scanf("%d%d%d",&n,&c,&m);
        memset(f,0,sizeof(f));
        memset(a,0,sizeof(a));
        for(i = 0; i < m; i++) {
            scanf("%d%d",&x,&y);
            f[x]++;
            a[y]++;
        }
        for(i = 1,l = 0; i <= 1000; i++) l = max(l,a[i]);
        r = m;
        x = m + 1;
        while(l <= r) {
            mid = (l + r) >> 1;
            if(check(mid)) {
                if(x > mid) {
                    x = mid;
                    y = s;
                }
                r = mid - 1;
            } else l = mid + 1;
        }
        printf("Case #%d: %d %d\n",cas,x,y);

    }
    return 0;
}
