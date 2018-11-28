#include <bits/stdc++.h>
using namespace std;

int r[60],c[60],d[60];
int a[60][60];
map<int,int> has,now;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=1;i<=n;i++) {
            scanf("%d",&r[i]);
        }
        int mi=-1,ma=1<<30;
        for (int i=1;i<=n;i++) {
            for (int j=1;j<=m;j++) {
                scanf("%d",&a[i][j]);
//                a[i][j]*=10;
            }
            sort(a[i]+1,a[i]+m+1);
            mi=max(mi,int(ceil((double)a[i][1]/(1.1*r[i]))));
            ma=min(ma,int(floor((double)a[i][m]/(0.9*r[i]))));
        }
        memset(c,0,sizeof(c));
        int ans=0;
        for (int k=mi;k<=ma;) {
            int f=0;
            for (int i=1;i<=n;i++) {
                if (c[i]==m) {
                    f=1;
                    break;
                }
            }
            if (f) break;
            int cnt=0;
            memcpy(d,c,sizeof(c));
            for (int i=1;i<=n;i++) {
                int low=r[i]*k*9,up=r[i]*k*11;
                for (int j=c[i]+1;j<=m;j++) {
                    if (low<=a[i][j]*10&&a[i][j]*10<=up) {
                        d[i]=j;
                        cnt++;
                        break;
                    }
                }
                if (cnt<i) break;
            }
            if (cnt==n) {
                memcpy(c,d,sizeof(c));
                ans++;
//                printf("%d\n",k);
//                printf("%d %d\n",c[1],c[2]);
            } else {
                k++;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
