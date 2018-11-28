#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	ll;

#define mod 1000000007
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define forv(i, n) for(int i = 0; i != int(n); ++i)
#define cases int t;  cin>>t;   while(t--)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

int main()
{
    fast_io;
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    int t;
    cin>>t;
    forn(ca,t)
    {
        double n,p,d,m,s[1005],k[1005],time[1005],ans=0;
        cin>>d>>n;
        forn(i,n)
            cin>>k[i]>>s[i];
        forn(i,n)
            time[i]=(d-k[i])/s[i];
        double max=0;
        forn(i,n)
            if(max<time[i])
                max=time[i];
        ans=d/max;
        cout<<"Case #"<<ca+1<<": "<<setprecision(7)<<fixed<<ans<<"\n";
    }
    return 0;
}
