#include<bits/stdc++.h>
using namespace std;
//#define CHKR
#define ll long long
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define ARRS int(5e5+500)
#define BARRS int(6e4+600)
#define MAX ((long long)(1e12+1))
#define MMAX ((long long)(1e9+10))
#define HS1 ((long long)(1000001329))
#define HS2 ((long long)(1000001531))
#define MOD ((long long)1000000007ll)
#define SQ 31622780
#define PI 3.14159265358979323846264338327950288419716939937510
#define BG 4294967232ll
#define MH 200008


ll dp[2][2000][2];
ll mi[ARRS];
ll f[ARRS];

pair<ll,ll> a[ARRS];
pair<ll,ll> b[ARRS];
#ifndef CHKR
int main(){
#else
int doit(fstream &in,fstream &out){
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
#endif
    #ifdef KHOKHO
        #ifndef CHKR
        freopen("in.in","r",stdin);
        freopen("out.out","w+",stdout);
        #endif //CHKR
    #endif //KHOKHO
    ll q,n,k;
    cin>>q;
    ll ti=1;
    while(q--){
        ll x,y,l,r;
        cin>>x>>y;

        n=24*60;
        for(int j=0; j<=n; j++)
            f[j]=0;
        pair<ll,ll>  ch={MAX,MAX};
        for(int i=0; i<x; i++){
            cin>>a[i].fr>>a[i].sc;
            ch=min({a[i].fr,0},ch);
        }
        for(int i=0; i<y; i++){
            cin>>b[i].fr>>b[i].sc;
            ch=min({b[i].fr,1},ch);
        }
        for(int i=0; i<x; i++){
            l=a[i].fr-ch.fr;
            r=a[i].sc-ch.fr;
            for(int j=l; j<r; j++){
                f[j]=1;
            }
        }
        for(int i=0; i<y; i++){
            l=b[i].fr-ch.fr;
            r=b[i].sc-ch.fr;
            for(int j=l; j<r; j++){
                f[j]=2;
            }
        }

        ll N=1,P=0;

        for(int j=0; j<=n; j++){
            dp[P][j][0]=MAX;
            dp[P][j][1]=MAX;
        }
        dp[P][0][0]=1;
        dp[P][0][1]=1;
        for(int i=0; i<n; i++){
            for(int j=0; j<=n; j++){
                dp[N][j][0]=MAX;
                dp[N][j][1]=MAX;
            }
            for(int j=0; j<=720; j++){
                if(f[i]!=2){
                    dp[N][j+1][0]=dp[P][j][0];
                    dp[N][j+1][0]=min(dp[N][j+1][0],dp[P][j][1]+1);
                }
                if(f[i]!=1){
                    dp[N][j][1]=dp[P][j][1];
                    dp[N][j][1]=min(dp[N][j][1],dp[P][j][0]+1);
                }
            }
            swap(N,P);
        }
        printf("Case #%lld: %lld\n",ti, min(dp[P][720][ch.sc]-1,dp[P][720][ch.sc^1]));
        ti++;
    }



    return 0;
}
