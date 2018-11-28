#include <cstring>
#include <iostream>
#include <cstdio>
#include <bitset>
#include <stack>
using namespace std;
int minim,maxim;
int S[1005],D[1005];
bitset<1005> B;
int T,N,K;
void solve()
{
    maxim=0;
    minim=(1<<30);
    int poz=1;
    stack <int> st,dr;
    st.push(0);
    dr.push(N+1);
    memset(S,0,sizeof(S));
    memset(D,0,sizeof(D));
    for(int i=1;i<=N;i++)
    {
        if(B[i])
        {
            st.push(i);
        }
        S[i]=i-st.top()-1;
    }
    for(int i=N;i;i--)
    {
        if(B[i])
        {
            dr.push(i);
        }
        D[i]=dr.top()-i-1;
    }
    for(int i=1;i<=N;i++)
    {
        if(B[i]) continue;
        if(min(S[poz],D[poz])<min(S[i],D[i]))
        {
            poz=i;
        }
        else if(min(S[poz],D[poz])==min(S[i],D[i])&&max(S[poz],D[poz])<max(S[i],D[i]))
        {
            poz=i;
        }
    }
    B[poz]=1;
    maxim=max(S[poz],D[poz]);
    minim=min(S[poz],D[poz]);
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        B.reset();
        cout<<"Case #"<<t<<": ";
        cin>>N>>K;
        while(K--) solve();
        cout<<maxim<<" "<<minim<<"\n";
    }
    return 0;
}
