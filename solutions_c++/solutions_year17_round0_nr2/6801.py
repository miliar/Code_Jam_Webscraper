#include<bits/stdc++.h>
using namespace std;
//#define CHKR
#define ll unsigned long long
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define ARRS int(5e5+500)
#define BARRS int(6e4+600)
#define MAX ((long long)(1e9+1))
#define MMAX ((long long)(1e9+10))
#define HS1 ((long long)(1000001329))
#define HS2 ((long long)(1000001531))
#define MOD ((long long)1000000007ll)
#define SQ 31622780
#define PI 3.14159265358979323846264338327950288419716939937510
#define BG 4294967232ll
#define MH 200008
ll c,m,pas;
ll att[30];
ll a[30];
bool go(ll x,ll mn,bool c){
    if(x==m)return 1;
    //cout<<x<<" "<<mn<<" "<<c<<" "<<a[x]<<endl;
    if(c){
        go(x+1,0,1);
        pas+=att[m-x-1]*9;
        return 1;
    }
    if(a[x]>=mn&&go(x+1,a[x],0)){
        pas+=att[m-x-1]*a[x];
        return 1;
    }
    if(a[x]-1>=mn&&a[x]&&go(x+1,0,1)){
        pas+=att[m-x-1]*(a[x]-1);
        return 1;
    }
    return 0;
}

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
    att[0]=1;
    for(int i=1; i<=20; i++)
        att[i]=att[i-1]*10;
    ll t,n,qi=0;
    cin>>t;
    while(t--){
        cin>>n;
        m=0;
        while(n){
            a[m]=n%10;
            n/=10;
            m++;
        }
        reverse(a,a+m);
        pas=0;
        go(0,0,0);
        qi++;
        cout<<"Case #"<<qi<<": "<<pas<<endl;
    }

    return 0;
}
