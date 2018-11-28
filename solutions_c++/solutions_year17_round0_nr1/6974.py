
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

string s;
ll cnt=0;

void solve(int x,int y)
    {
        FOR(i,x,y+1)
            if(s[i]=='+') s[i]='-';
            else s[i]='+';
    }

int main()
    {
        freopen("A-large.in" , "r" , stdin);
        freopen("A-output1.txt" , "w" , stdout);
        ll t;
        cin>>t;
        ll ptr=1;
        while(ptr<=t)
            {
                cnt=0;
                cin>>s;
                ll n;
                cin>>n;
                FOR(i,0,s.size()-n+1)
                    {
                        if(s[i]=='+') continue;
                        else solve(i,i+n-1);
                        cnt++;
                        //cout<<s<<endl;
                    }
                ll f=0;
                FOR(i,0,s.size())
                    if(s[i]=='-')
                        f=1;
                if(f) cout<<"Case #"<<ptr<<": IMPOSSIBLE";
                else cout<<"Case #"<<ptr<<": "<<cnt;
                cout<<endl;
                ptr++;
            }
        return 0;
    }
