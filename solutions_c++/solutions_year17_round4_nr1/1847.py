#include <bits/stdc++.h>

using namespace std;

int G[10];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;cin>>t;
    for(int cs=1;cs<=t;cs++){
        memset(G,0,sizeof G);
        int n,p;cin>>n>>p;
        for(int i=0;i<n;i++){
            int x;cin>>x;
            G[x%p]++;
        }
        int res=0;
        res+=G[0];G[0]=0;
        if(p==2){res+=(G[1]/2+(G[1]&1));
        printf("Case #%d: %d\n",cs,res);
        continue;
        }
        if(p==3){
            res+=min(G[1],G[2]);
            int d=min(G[1],G[2]);
            G[1]-=d; G[2]-=d;
            res+=(G[1]/3)+(G[1]%3!=0);
            res+=(G[2]/3)+(G[2]%3!=0);
            printf("Case #%d: %d\n",cs,res);
            continue;
        }
        int d=min(G[1],G[3]);
        G[1]-=d; G[3]-=d;
        res+=d;
        res+=G[2]/2;
        G[2]=G[2]%2;
        if(G[2]==1){
            if(max(G[1],G[3])>1){
                res++;
                G[2]=0;
                if(G[1]>1)G[1]-=2;
                if(G[3]>1)G[3]-=2;
            }else{
                res++;
            printf("Case #%d: %d\n",cs,res);
            continue;
            }
        res+=G[1]/4+(G[1]%4!=0);
        res+=G[3]/4+(G[3]%4!=0);
            printf("Case #%d: %d\n",cs,res);
            continue;
        }
    }
    return 0;
}
