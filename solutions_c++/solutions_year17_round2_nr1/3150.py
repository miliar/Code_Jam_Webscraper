#include<bits/stdc++.h>
//#include "A-small-practice.in"
#include <fstream>
#define ll long long
#define pb push_back
#define mp make_pair
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1L.out","w",stdout);
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        ll D, n;
        cin >> D >> n;
        vector< pair<double, double> > v;
        double a, b;
        for(int i=0;i<n;i++)
        {
            cin >> a >> b;
            v.pb(mp(a,b));
        }
        sort(v.begin(),v.end());
        double ti=0.0, vel=0.0;
        for(int i=n-1;i>=0;i--)
        {
            if(i==n-1)
            {
                ti = (D-v[i].first)/v[i].second;
                vel = v[i].second;
            }
            else
            {
                if(((D-v[i].first)/ti) >= v[i].second)
                {
                    ti = (D-v[i].first)/v[i].second;
                    vel = v[i].second;
                }
            }
        }
        vel = D/ti;
        printf("Case #%d: %0.8lf\n", t+1, vel);
    }

    return 0;
}

