#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<long long int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	ll;

#define mod 1000000007
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define forn(i, n) for(ll i = 0; i < ll(n); ++i)
#define forv(i, n) for(int i = 0; i != int(n); ++i)
#define cases int t;  cin>>t;   while(t--)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

int main()
{
    fast_io;
    freopen("A-large.in","r",stdin);
    freopen("output4.in","w",stdout);
    int t,k;
    cin>>t;
    forn(c,t)
    {
        string s;
        cin>>s>>k;
        int n=s.length(),ans=0,f=1;
        forn(i,n-k+1)
            if(s[i]=='-')
            {
                for(int j=i;j<k+i;j++)
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                ans++;
            }
        forn(i,n)
            if(s[i]=='-')
            {
                f=0;
                break;
            }
        if(f)
            cout<<"Case #"<<c+1<<": "<<ans<<"\n";
        else
            cout<<"Case #"<<c+1<<": "<<"IMPOSSIBLE\n";
    }
    return 0;
}
