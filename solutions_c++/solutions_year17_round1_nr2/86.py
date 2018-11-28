#include<bits/stdc++.h>
using namespace std;
int higher(long long now,int a){
    if(now*9>a*10)return 1;
    return 0;
}
int check(long long now,int a){
    if(now*9<=a*10&&now*11>=a*10)return 1;
    return 0;
}
main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,cs;
    scanf("%d",&T);
    for(cs=1;cs<=T;cs++){
        long long val[60];
        int i,j,n,p,ary[60][60],pos[60]={0};
        scanf("%d%d",&n,&p);
        for(i=0;i<n;i++)scanf("%lld",&val[i]);
        for(i=0;i<n;i++)for(j=0;j<p;j++)scanf("%d",&ary[i][j]);
        for(i=0;i<n;i++)sort(ary[i],ary[i]+p);
        int now=1,ans=0;
        while(1){
            int tag=1;
            for(i=0;i<n;i++){
                while(higher(now*val[i],ary[i][pos[i]])){
                    if(pos[i]==p-1){
                        tag=0;
                        break;
                    }
                    else pos[i]++;
                }
                if(tag==0)break;
            }
            if(tag==0)break;
            int suc=1;
            for(i=0;i<n;i++){
                if(!check(now*val[i],ary[i][pos[i]])){
                    suc=0;
                    break;
                }
            }
            if(suc){
                ans++;
                int fail=0;
                for(i=0;i<n;i++){
                    if(pos[i]==p-1){
                        fail=1;
                        break;
                    }
                    pos[i]++;
                }
                if(fail)break;
            }
            else{
                now++;
            }
        }
        printf("Case #%d: %d\n",cs,ans);
    }
}
