#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include<bits/stdc++.h>
using namespace std;
int T,n,k,ans,a[1010],b[1010],cnt[100];
int main()
{
    scanf("%d",&T);
    freopen("A.out","w",stdout);
    for(int cas=1;cas<=T;cas++){
        scanf("%d%d",&n,&k);
        memset(cnt,0,sizeof(cnt));
        for (int i=1;i<=n;i++) {
            scanf("%d",&a[i]);
            cnt[a[i]%k]++;
        }
        if(k==2){
            ans=cnt[0]+(cnt[1]+1)/2;
        }
        if (k==3){
            int x=min(cnt[1],cnt[2]);
            ans=cnt[0]+x;
            ans+=(cnt[1]+cnt[2]-x-x+2)/3;
        }
        if (k==4){
            ans=cnt[0];
            ans+=(cnt[2]/2+1)/2; cnt[2]%=2;
            int x=min(cnt[1],cnt[3]);
            ans+=x; cnt[3]-=x;cnt[1]-=x;
            if (cnt[2]>=1 && cnt[3]>=2) cnt[2]--,cnt[3]-=2,ans++;
            if (cnt[2]>=1 && cnt[1]>=2) cnt[2]--,cnt[1]-=2,ans++;
            ans+=(cnt[1]+3)/4;
            ans+=(cnt[3]+3)/4;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
