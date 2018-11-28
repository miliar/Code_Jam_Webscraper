#include<cmath>
#include<iostream>

using namespace std;

#define rep(i,a,b) for(register int i=a;i<b;i++)

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    long long t,n,k,N,level,ext,filled;
    cin>>t;
    rep(i,0,t)
    {
        cin>>n>>k;
        N=n+1;
        level=log2(k);
        filled=pow(2,level)-1;
        ext=N%(long long)pow(2,level);
        N=N>>level;
        cout<<"Case #"<<i+1<<": "<<(N-((N+1)>>1))-(k>filled+ext)*!(N&1)<<' '<<(N>>1)-1+(k<=filled+ext)*(N&1)<<'\n';
    }
}
