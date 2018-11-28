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
#define EP ((long double)(1e-9))
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

double a[ARRS];
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
    double t;
    cin>>q;
    ll ti=1;
    while(q--){
        ll x,y,l,r,m;
        cin>>n>>m;
        cin>>t;
        for(int i=0; i<n; i++){
            cin>>a[i];
        }
        double f1=-1,f2=-1;
        ll c;
        while(t>EP){
            f1=-1;
            f2=-1;
            c=0;
            for(int i=0; i<n; i++){
                if(a[i]+EP>f1&&f1>a[i]-EP){c++;continue;}
                //cout<<a[i]<<" "<<f1<<endl;
                if(f1==-1||a[i]+EP<f1){
                    swap(f1,f2);
                    f1=a[i];
                    c=1;
                   // continue;
                } else if(f2==-1||a[i]+EP<f2){
                    f2=a[i];
                }
            }
            if(f2==-1)break;
            double d;
            d=min(1.0*t/c,(f2-f1));
            t-=1.0*d*c;
          // cout<<f1<<" "<<f2<<" "<<d<<" "<<t<<endl;
            for(int i=0; i<n; i++){
                if(a[i]+EP>f1&&f1>a[i]-EP)a[i]+=d;
            }
        }
        double d=min(t/n,1.0-f1);
        double p=1.0;
        for(int i=0; i<n; i++){
            if(a[i]+EP>f1&&f1>a[i]-EP)a[i]+=d;
            p*=a[i];
        }
        printf("Case #%lld: %.9f\n",ti, p);
        ti++;
    }



    return 0;
}
