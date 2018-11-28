#include<bits/stdc++.h>

using namespace std;

const int Maxn=1e3+10;
const double ep=1e-7;
long long n,p[Maxn],s[Maxn],d;
double ans;


long double bs(long double f,long double l)
{
    cerr<<"binary search:::\tl::::"<<l<<" f::"<<f<<" "<<l-f<<endl;
    if(abs(l-f)<(double)ep||(double)abs(l-f-9.53674e-07)<ep)
        return l;
    long double mid=(long double) (f+l)/2;
    for(int i=0;i<n;i++)
        if(p[i]<d&&(long double)d/mid<(long double)(d-p[i])/s[i])
            return bs(f,mid);
    return bs(mid,l);
}

int main()
{
    int t;
    cin>>t;
    for(int o=0;o<t;o++)
    {
        cin>>d>>n;
        for(int i=0;i<n;i++)
            cin>>p[i]>>s[i];
        ans=bs(0,1e18);
        cout<<fixed<<setprecision(9)<<"Case #"<<o+1<<": "<<ans<<endl;

    }

}
