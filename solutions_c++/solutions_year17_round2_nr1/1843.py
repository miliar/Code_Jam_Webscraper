#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b)                for(ll i=a;i<b;i++)
#define repr(i,n)                for(ll i=n-1;i>=0;i--)
#define ll long long int
#define ld long double
#define llu long long unsigned
#define pb push_back
#define mod 1e9+7

/*
                    ** author **
                ** Parth Lathiya **
    ** https://www.cse.iitb.ac.in/~parthiitb/ **
*/

int main()
{

ios::sync_with_stdio(false);

#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
#endif

freopen("A-large.out","w",stdout);

//  --------------------------------------------------------------------------------------

    ll T;
    cin>>T;
    ll bk=T;
    while(T--)
    {
        ll c,n;
        double d;
        cin>>d>>n;
        vector<pair<ll,ll> > my;
        double k,s;
        rep(i,0,n)
        {
            cin>>k>>s;
            my.pb(make_pair(k,s));
        }

        // sort(my,my)
        sort(my.begin(), my.end());

        // rep(i,0,my.size())
        // {
        //     cout<<my.at(i).first<<my.at(i).second;
        // }
        double curk,curs;
        curk=my.at(0).first;
        curs=my.at(0).second;

        rep(i,1,my.size())
        {
            if(my.at(i).second<curs)
            {
                double temp=(my.at(i).first-curk)/(curs-my.at(i).second);
                if((curk+curs*temp) < d ){curs=my.at(i).second;
                    curk=my.at(i).first;}
            }
        }

        double ans;
        ans= d/((d-curk)/curs);
        cout<<"Case #"<<bk-T<<": "<<fixed<<setprecision(6)<<ans<<endl;
    }

//  --------------------------------------------------------------------------------------

return 0;
}