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


pair<ll,ll> a[ARRS];
ll dp[1005][1005];
ll mi[ARRS];


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
        cin>>n>>k;
        for(int i=0; i<n; i++){
            cin>>a[i].fr>>a[i].sc;
        }
        sort(a,a+n);
        reverse(a,a+n);
        for(int i=0; i<=k; i++){
            mi[i]=-MAX;
        }
        ll pas=-MAX;
        for(int i=0; i<n; i++){
            for(int j=k; j>=1; j--){
                dp[i][j]=mi[j-1]+2*a[i].fr*a[i].sc;
                mi[j]=max(mi[j],dp[i][j]);
               // cout<<dp[i][j]<<" ";
            }
            dp[i][0]=a[i].fr*a[i].fr+2*a[i].fr*a[i].sc;
            mi[0]=max(mi[0],dp[i][0]);
            pas=max(pas,dp[i][k-1]);
           //  cout<<dp[i][0]<<" ";
           // cout<<endl;
        }
        printf("Case #%lld: %.9lf\n",ti,1.0l*pas*PI);
        ti++;
    }



    return 0;
}
