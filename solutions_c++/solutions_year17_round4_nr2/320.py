#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,cs,i,j;
    scanf("%d",&T);
    for(cs=1;cs<=T;cs++){
        int n,c,m,p,b,ary[1010]={0},cnt[1010]={0},Max=0;
        scanf("%d%d%d",&n,&c,&m);
        for(i=0;i<m;i++){
            scanf("%d%d",&p,&b);
            ary[p]++;
            cnt[b]++;
            Max=max(Max,cnt[b]);
        }
        int L=Max-1,R=1000000;
        while(L<R-1){
            int M=(L+R)/2,left=0,fail=0;
            for(i=1;i<=n;i++){
                if(ary[i]<=M)left+=M-ary[i];
                else if(ary[i]-M<=left)left-=(ary[i]-M);
                else{
                    fail=1;
                    break;
                }
            }
            if(fail==0)R=M;
            else L=M;
        }
        int ans=0,left=0;
        for(i=1;i<=n;i++){
            if(ary[i]<=R)left+=R-ary[i];
            else if(ary[i]-R<=left)left-=(ary[i]-R),ans+=ary[i]-R;
        }
        printf("Case #%d: %d %d\n",cs,R,ans);
    }
}
