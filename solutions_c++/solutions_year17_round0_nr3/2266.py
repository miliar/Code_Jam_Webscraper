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
    freopen("C-large.txt","r",stdin);
    freopen("output-large.txt","w",stdout);
    int t;
    cin>>t;
    forn(c,t)
    {
        ll n,k,p=1;
        cin>>n>>k;
        while(k>0)
        {
            if(k-p>0)
            {
                n-=p;
                k-=p;
                p*=2;
            }
            else
            {
                n-=p;
                p*=2;
                cout<<"Case #"<<c+1<<": ";
                if(n%p>p/2)
                {
                    if(k>n%p-p/2)
                        cout<<n/p+1<<" "<<n/p<<"\n";
                    else
                        cout<<n/p+1<<" "<<n/p+1<<"\n";
                }
                else
                {
                    if(k>n%p)
                        cout<<n/p<<" "<<n/p<<"\n";
                    else
                        cout<<n/p+1<<" "<<n/p<<"\n";
                }
                break;
            }
        }
    }
    return 0;
}
