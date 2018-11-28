#include <bits/stdc++.h>
#define ll long long int
#define si1(a) scanf("%d",&a)
#define si2(a,b) scanf("%d%d",&a,&b)
#define si3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sil1(a) scanf("%lld",&a)
#define sil2(a,b) scanf("%lld%lld",&a,&b)
#define sil3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define pi1(a) printf("%d\n",a)
#define pi2(a,b) printf("%d%d",a,b)
#define pi3(a,b,c) printf("%d%d%d",a,b,c)
#define pil1(a) printf("%lld",a)
#define pil2(a,b) printf("%lld%lld",a,b)
#define pil3(a,b,c) printf("%lld%lld%lld",a,b,c)
#define dd double
using namespace std;
int main()
{   freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tt=1;
    si1(t);
    while(t--){
        ll n,i,j,k,p,ctr=0;
        vector<ll>v;ll ctr1=0;
        sil1(n);
        k=n;
        int vis[20];
        for(i=0;i<19;i++){
            vis[i]=0;
        }
        while(k!=0){
            v.pb(k%10);
            k/=10;
        }
        p=v.size();
        ctr=1;
        while(ctr!=0){
            ctr=0;
            for(i=1;i<p;i++){
                if(v[i]>v[i-1]&&i!=p-1){
                    v[i-1]=9;
                    if(vis[i]==0){
                    v[i]--;
                    }
                    vis[i-1]++;
                    ctr++;
                }
                else if(v[i-1]==-1&&i!=p-1){
                    v[i-1]=9;
                    if(vis[i]==0){
                    v[i]--;
                    }
                    vis[i-1]++;
                    ctr++;
                }
                else if(v[i]>v[i-1]&&i==p-1){
                     v[i]--;
                     vis[i-1]++;
                    v[i-1]=9;
                    ctr++;
                }
            }
        }
        reverse(v.begin(),v.end());
        for(j=0;j<p;j++){
            if(v[j]!=0){
                break;
            }
        }
        printf("Case #%d: ",tt);
        for(i=j;i<p;i++){

            pil1(v[i]);
        }

        printf("\n");
        tt++;
    }
    return 0;
}
