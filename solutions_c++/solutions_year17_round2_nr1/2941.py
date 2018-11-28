#include "bits/stdc++.h"

using namespace std;

#define ll long long int
#define FOR(i,a,b) for(ll i=a;i<b;i++)
#define NFOR(i,a,b) for(ll i=a;i>b;i--)
#define sz(a) int((a).size())
#define all(c) c.begin(),c.end()
#define find(c, x) (c.find(x)!=c.end())
#define tr(c,i) for(typeof((c).begin() i=(c).begin();i!=(c).end();i++)
#define pb push_back
#define mp make_pair
#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define Mod 1000000007

int main()
    {
        freopen ("A-large.in","r",stdin);
        freopen ("ans2.txt","w",stdout);
        ll t;
        cin>>t;
        ll ptr=1;
        while(ptr<=t)
            {
                cout<<"Case #"<<ptr<<": ";
                ll d,horse;
                cin>>d>>horse;
                ll dist[horse],speed[horse];
                FOR(i,0,horse)
                    cin>>dist[i]>>speed[i];
                double max_time=0;
                FOR(i,0,horse)
                    {
                        double ans=(d-dist[i]);
                        ans=ans/speed[i];
                        max_time=max(max_time,ans);
                    }
                double ans1=d/max_time;
                printf("%0.9f",ans1);
                cout<<endl;
                ptr++;
            }
        return 0;
    }
