#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#define pi acos(-1.0)
using namespace std;
long double dp[1011][1011];
vector<pair<long double,long double> > v;
int n,k;
long double rec(int a,int b)
{
    if(b==k)
        return 0;
    if(a==n)
        return -1e17;
    long double &ans = dp[a][b];
    if(ans!=-1.0)
        return ans;
    ans = max(rec(a+1,b),rec(a+1,b+1)+v[a].second);
    return ans;
}
main()
{
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++)
    {
        for(int i=0;i<1011;i++)
            for(int j=0;j<1011;j++)
                dp[i][j]=-1.0;
        v.clear();

        cin>>n>>k;
        long double r[n],h[n];
        for(int i=0;i<n;i++)
        {
            cin>>r[i]>>h[i];
            h[i]=2.0*pi*r[i]*h[i];
            r[i]=pi*r[i]*r[i];
            v.push_back(make_pair(r[i],h[i]));
        }
        sort(v.begin(),v.end(),greater<pair<long double,long double> >());
        long double mans = -1.0;
        for(int i=0;i<n;i++)
        {
            long double ta = rec(i+1,1) + v[i].first + v[i].second;
            if(ta>mans)
                mans=ta;
        }
        cout.precision(17);
        cout<<"Case #"<<ii+1<<": "<<mans<<endl;
    }
}

