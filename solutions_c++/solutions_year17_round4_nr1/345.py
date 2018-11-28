#include<bits/stdc++.h>
using namespace std;
main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cs,i,j;
    scanf("%d",&T);
    for(cs=1;cs<=T;cs++){
        int n,p,rem[5]={0},g,ans=0;
        scanf("%d%d",&n,&p);
        for(i=0;i<n;i++)scanf("%d",&g),rem[g%p]++;
        if(p==2){
            ans=rem[0]+rem[1]/2+rem[1]%2;
            printf("Case #%d: %d\n",cs,ans);
        }
        if(p==3){
            ans=rem[0]+min(rem[1],rem[2]);
            if(rem[1]<rem[2]){
                rem[2]-=rem[1];
                ans+=rem[2]/3;
                ans+=(rem[2]%3>0);
            }
            else{
                rem[1]-=rem[2];
                ans+=rem[1]/3;
                ans+=(rem[1]%3>0);
            }
            printf("Case #%d: %d\n",cs,ans);
        }
        if(p==4){
            ans=rem[0]+min(rem[1],rem[3])+rem[2]/2;
            rem[2]%=2;
            rem[1]=abs(rem[1]-rem[3]);
            if(rem[2]==0){
                ans+=rem[1]/4;
                ans+=(rem[1]%4>0);
            }
            else{
                ans+=rem[1]/4;
                if(rem[1]%4==3)ans+=2;
                else ans++;
            }
            printf("Case #%d: %d\n",cs,ans);
        }
    }
}
