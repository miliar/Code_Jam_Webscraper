#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include<bits/stdc++.h>
using namespace std;
int T;
int n,c,m,a[1010],aa[1010],b[1010],cnt[1010],ans;
int l,r,mid;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d%d%d",&n,&c,&m);
        memset(aa,0,sizeof(a));

        memset(cnt,0,sizeof(cnt));
        for (int i=1;i<=m;i++){
            int x,y;
            scanf("%d%d",&x,&y);
            aa[x]++;
            cnt[y]++;
        }
        l=0;
        for (int i=1;i<=c;i++) l=max(l,cnt[i]);
        r=1010;
        for (int i=0;i<=n;i++) a[i]=aa[i],b[i]=0;
        while (l<r){
            mid=(l+r)/2;
            ans=0;
            for (int i=0;i<=n;i++) a[i]=aa[i],b[i]=0;
            for (int i=n;i>0;i--){
                if (a[i]+b[i]>mid) {
                    if (a[i]>mid) {
                        ans+=a[i]-mid;
                        b[i-1]+=a[i]-mid+b[i];
                    }
                    else {
                        b[i-1]+=a[i]+b[i]-mid;
                    }
                }
            }

            if (b[0]==0) r=mid;else l=mid+1;

        }
        ans=0;
        mid=l;
        for (int i=0;i<=n;i++) a[i]=aa[i],b[i]=0;
        for (int i=n;i>0;i--){
            if (a[i]+b[i]>mid) {
                if (a[i]>mid) {
                    ans+=a[i]-mid;
                    b[i-1]+=a[i]-mid+b[i];
                }
                else {
                    b[i-1]+=a[i]+b[i]-mid;
                }
            }
        }
        printf("Case #%d: %d %d\n",cas,l,ans);
    }
    return 0;
}
