#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front;
#define fbo find_by_order
#define ook order_of_key
#define lb lower_bound
#define ub upper_bound
#define rep(i,n) for(int i=0;i<n;i++)
#define fo(j,a,b) for(int j=a;j<=b;j++)
#define mem(x,a) memset(x,a,sizeof(x))

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<ll> vi;
typedef double ld;
typedef map<ll,ll> spt;
typedef set<ll> si;
typedef multiset<ll>::iterator sit;
typedef map<int,int>::iterator mi;
typedef vector<int>::iterator vit;
typedef vector<ii> vii;
typedef set<ii> sii;
typedef multiset<ll> msi;
typedef vector< vector<ll> > matrix;
template<class T> T chmin(T& a, T& b) { if(a>b) return a; }
template<class T> T chmax(T& a, T& b) { if(a<b) return b; }

const ll INF = 1e18;
const int MOD = 3;
const int N = 1e5 +3 ;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("aoutput.out","w",stdout);
    ll t;
    cin>>t;
    rep(z,t)
    {
        ll n;
        cin>>n;
        cout<<"Case #"<<z+1<<": ";
        ll temp=n,r,mn=100,d=0;
        while(temp)
        {
            temp/=10;
            d++;
        }
            ll a[d+2]={0};
            temp=n,mn=100;
            ll cnt=d;
            while(temp)
            {
                r=temp%10;
                mn=min(mn,r);
                //cout<<d;
                if(r>mn)
                {
                    a[cnt]=r-1;
                    mn=r-1;
                   for(int i=cnt+1;i<=d;i++)
                    a[i]=9;
                }
                else
                    a[cnt]=r;
                temp/=10;
                cnt--;
            }
            if(a[1]!=0)
            for(int i=1;i<=d;i++)
                cout<<a[i];
                else
                    for(int i=2;i<=d;i++)
                    cout<<a[i];
            cout<<"\n";
    }
}
