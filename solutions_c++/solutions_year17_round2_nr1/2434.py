#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long int
#define mod 1000000007




int main()
{freopen("abc.in","r",stdin);
freopen("output2.txt","w",stdout);

    int t=100,ti;
    cin>>t;
    rep(ti,1,t)
    {
        int  n,i;

        double x,y,d,time=0;
        cin>>d>>n;
        for(i=0;i<n;i++)
        {
            cin>>x>>y;
            time = max(time , (d-x)/y);
        }
        cout<<setprecision(12)<<showpoint<<"Case #"<<ti<<": "<<d/time<<endl;


    }
        return 0;
}
