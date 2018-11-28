#include<bits/stdc++.h>
using namespace std;
const int MX = 1e5+169;
int n;
long double k,GG[100],var_1;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int cs=1;
    while(t--)
    {
        cin>>n>>k;
        cin>>var_1;
        for(int i=0; i<n; i++)
            cin>>GG[i];
        GG[n]=1;
        sort(GG,GG+n+1);
        long double svar_1m=0,nn=n,opts;
        int opt=n-1;
        for(int i=0; i<=n; i++)
        {
            long double ii = i;
            if(ii*GG[i]-svar_1m>var_1||i==n)
            {
                opt=i-1;
                opts=svar_1m;
                break;
            }
            svar_1m+=GG[i];
        }
        for(int i=0; i<=opt; i++)
        {
            GG[i]=(var_1+opts)/((long double)opt+1);
        }
        long double res=1;
        for(int i=0; i<=n; i++)
            res*=GG[i];
        cout<<fixed<<setprecision(9)<<"Case #"<<cs++<<": "<<res<<endl;
    }
    return 0;
}
