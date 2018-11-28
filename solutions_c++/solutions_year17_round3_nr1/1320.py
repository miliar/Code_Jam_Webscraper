#include <bits/stdc++.h>

using namespace std;

bool comp(pair <int,int> &a, pair <int,int> &b)
{
    long long aa=1ll*a.first*a.second;
    long long bb=1ll*b.first*b.second;
    return aa>bb;
}


int main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    int t;
    cin>>t;
    for (int test=1; test<=t; test++)
    {
        int n,k;
        cin>>n>>k;
        vector < pair <int,int> > v(n);
        for (int i=0; i<n; i++)
        {
            cin>>v[i].first>>v[i].second;
        }

        sort(v.begin(),v.end(),comp);

        double tmp_r=0;
        double ans=0;
        double cnt_v=0;
        for (int i=0; i<k-1; i++)
        {
            cnt_v+=2.*M_PI*v[i].first*v[i].second;
            tmp_r=max(tmp_r, 1.*v[i].first);
        }

        for (int i=k-1; i<n; i++)
        {
            double tmp_v=2*M_PI*v[i].first*v[i].second;
            double tmp_R=max(tmp_r, 1.*v[i].first);
            ans=max(ans, cnt_v + tmp_v  + M_PI*tmp_R*tmp_R);
        }

        for (int i=k-1; i<n; i++)
        {
            double tmp= 2.*M_PI*v[i].first*v[i].second + 1.*M_PI*v[i].first*v[i].first;
            ans=max(ans, tmp+cnt_v);
        }

        cout<<"Case #"<<test<<": "<<fixed<<setprecision(20)<<ans<<'\n';
    }
    return 0;
}
