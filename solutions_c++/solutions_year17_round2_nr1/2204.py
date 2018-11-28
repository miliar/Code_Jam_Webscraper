#include<bits/stdc++.h>
#define ll long long
using namespace std;
#define INF 1000000000000

int main()
{
    ifstream cin; cin.open("A-large.in"); ofstream cout; cout.open("fileout.txt"); //comment while testing.
    ll t;
    cin>>t;
    for(int testcase=1;testcase<=t;testcase++)
    {
        // Solve problem
        ll n, d;
        cin>>d>>n;
        pair <ll,ll> ds[n+5];
        for(int i=0;i<n;i++)
        {
            cin>>ds[i].first>> ds[i].second;
        }
        sort(ds,ds+n);
        double maxtime = -1.0;
        for(int i=0;i<n;i++)
        {
                if(ds[i].first > d)
                    break;
                maxtime = max ( 1.0*(d - ds[i].first)/(1.0*(ds[i].second)) , maxtime );
        }
        //cout<<"wut";
        maxtime = (d/maxtime);
        cout<<"Case #"<<testcase<<": "<<setprecision(14)<<maxtime<<endl;
    }
    return 0;
}
