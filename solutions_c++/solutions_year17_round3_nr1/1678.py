#include <bits/stdc++.h>
#define pb push_back
#define ll long long
#define fi first
#define mp make_pair
#define se second
#define pii pair<int,int>
using namespace std;
double PI=3.1415926535897932384626433;
int n,k,test;
long long r[10007],h[10007],ok[10007],res=0;
pair <long long,int> lk[10007];
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&test);
    for(int t=1;t<=test;t++){
        res=0;
        long long mk=0;
        scanf("%d %d",&n,&k);
        for(int i=1;i<=n;i++){
            scanf("%lld %lld",&r[i],&h[i]);
            lk[i]=mp(r[i]*h[i],i);
            ok[i]=0;
        }
        sort(lk+1,lk+1+n,greater < pair <long long,int> >());
        mk=0;
        long long sec=0;
        for(int i=1;i<=k;i++){
            pair <long long,int> pl=lk[i];
            int id=pl.se;
            res+=2*r[id]*h[id];
            if(r[id]>mk){
                sec=mk;
                mk=r[id];
            }
            if(r[id]>sec){
                sec=r[id];
            }
        }
        int cnt=0;
        for(int i=1;i<=k;i++){
            int id=lk[i].se;
            if(r[id]==mk){
                if(cnt==0) cnt=id;
                else cnt=-6;
            }
        }
        res+=mk*mk;
        long long ans=res;
        int ck=0;
            for(int i=k+1;i<=n;i++){
                int id=lk[i].se;
                for(int j=1;j<=k;j++){
                    int pok=lk[j].se;
                    //cout<<pok<<endl;
                    if(pok==cnt){
                        if(k==1){
                            ans=max(ans,res-mk*mk+r[id]*r[id]-2*r[pok]*h[pok]+2*r[id]*h[id]);
                        }
                        else{
                            ans=max(ans,res-mk*mk+max(r[id]*r[id],sec*sec)-2*r[pok]*h[pok]+2*r[id]*h[id]);
                        }
                    }
                    ans=max(ans,res-mk*mk+max(r[id]*r[id],mk*mk)-2*r[pok]*h[pok]+2*r[id]*h[id]);
                }
            }
        double kq=ans*PI;
        printf("Case #%d: %.10lf\n",t,kq);
    }
}

