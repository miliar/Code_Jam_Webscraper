#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b)                for(ll i=a;i<b;i++)
#define repr(i,n)                for(ll i=n-1;i>=0;i--)
#define ll long long int
#define ld long double
#define llu long long unsigned
#define pb push_back
#define mod 1e9+7
#define pp 3.1415926535897

/*
                    ** author **
                ** Parth Lathiya **
    ** https://www.cse.iitb.ac.in/~parthiitb/ **
*/


bool myf (pair<ld,ld> a,pair<ld,ld> b) { return (a.first>b.first); }
bool myff (ld a,ld b) { return (a>b); }


int main()
{

ios::sync_with_stdio(false);

#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
#endif

freopen("A-large.out","w",stdout);

//  --------------------------------------------------------------------------------------

    // ll T;
    // cin>>T;
    // ll bk=T;
    // while(T--)
    // {
    
    //     ll n,k;
    //     ld r,h;
    //     ld pi=3.1415926535897932384626433;
    //     cin>>n>>k;
    //     std::vector<pair<ld,ld> > my;
    //     rep(i,0,n)
    //     {
    //         cin>>r>>h;
    //         my.pb(make_pair(r,h));
    //     }
        
    //     sort(my.begin(),my.end());
    //     sort(my.begin(),my.end(),myf);
    //     cout<<my.at(0).second;
    //     ld maxx = -1.0;
    //     ld dp[n+1][k+1];
    //         rep(i,1,n+1)
    //         {
    //             ld temp = pi*my.at(i-1).first*my.at(i-1).first + 2.0*pi*my.at(i-1).first*my.at(i-1).second;
    //             // cout<<temp<<endl;
    //             maxx=temp>maxx?temp:maxx;
    //             dp[i][1]= maxx;
    //             // cout<<maxx<<endl;
    //         }

    //     rep(j,2,k+1)
    //     {
    //         rep(i,j,n+1)
    //         {
    //            if(i==j)
    //             dp[i][j]= dp[i-1][j-1]+ pi*((my.at(i-1).first)*(my.at(i-1).first)-(my.at(i-2).first)*(my.at(i-2).first)) + 2*pi*my.at(i-1).first*my.at(i-1).second;
    //         else
    //             dp[i][j]= max(dp[i-1][j] ,dp[i-1][j-1]+ pi*((my.at(i-1).first)*(my.at(i-1).first)-(my.at(i-2).first)*(my.at(i-2).first))+ 2*pi*my.at(i-1).first*my.at(i-1).second);

    //         }
    //     }         
    //             cout<<"Case #"<<bk-T<<": "<<fixed<<setprecision(9)<<dp[n][k]<<endl;
       
    // }


    ll T;
    cin>>T;
    ll bk=T;
    while(T--)
    {
    
        ll n,k;
        ld r,h;
        ld pi=3.1415926535897932384626433;
        cin>>n>>k;
        std::vector<pair<ld,ld> > my;
        rep(i,0,n)
        {
            cin>>r>>h;
            my.pb(make_pair(r,r*h));
        }
        
        // sort(my.begin(),my.end());
        sort(my.begin(),my.end(),myf);
        // cout<<my.at(0).first;
        ld maxx = -1.0;
        // ld dp[n+1][k+1];
        // ld maxx=0;
            // ld maxx=-1;
            rep(i,0,n)
            {
                std::vector<ld> v;
                rep(j,0,n)
                {if(j!=i &&  my.at(j).first <= my.at(i).first) v.pb(my.at(j).second);}
                sort(v.begin(), v.end(),myff);
                // if(v.size()>0)cout<<v.at(0);

                ld ans=0;
                if(v.size()>=k-1)
                    {rep(j,0,k-1)
                {ans+=2*pi*v.at(j);}
                maxx=max(maxx,ans + 2*pi*my.at(i).second + pi*my.at(i).first*my.at(i).first);
            }

            }

                cout<<"Case #"<<bk-T<<": "<<fixed<<setprecision(9)<<maxx<<endl;
       
    }


//  --------------------------------------------------------------------------------------

return 0;
}