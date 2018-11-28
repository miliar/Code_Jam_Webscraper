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

const ll INF = 1e18;
const int MOD = 3;
const int N = 1e5 +3 ;
struct cmp{
    bool operator()(ii x,ii y)
    {
        if(abs(x.se-x.fi-1)==abs(y.se-y.fi-1))
        {
            if((abs(x.se-x.fi-1)%2) == (abs(y.se-y.fi-1)%2))
                return x.fi>y.fi;
                else
                    return (abs(x.se-x.fi-1)%2) < (abs(y.se-y.fi-1)%2);
        }
        else
            return abs(x.se-x.fi-1)<abs(y.se-y.fi-1);
    }
};
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("aoutput.out","w",stdout);
    ll t;
    cin>>t;
    rep(z,t)
    {
        ll n,k;
        set<ii,cmp> v;
        set<ii,cmp>::reverse_iterator rit;
        cin>>n>>k;
        cout<<"Case #"<<z+1<<": ";
        v.insert({0,n+1});
        rep(i,k-1)
        {
           rit=v.rbegin();
           ll l=(*rit).fi;
           ll r=(*rit).se;
           //cout<<l<<" "<<r<<"\n";
           ll mid=abs(l+r)/2;
           v.erase({l,r});
           v.insert({l,mid});
           v.insert({mid,r});
           //for(auto it:v)
            //cout<<it.fi<<" "<<it.se<<"\n";
           //cout<<"\n";
        }
        rit=v.rbegin();
        ll l=(*rit).fi;
        ll r=(*rit).se;
        ll mid=abs(l+r)/2;
        cout<<max(abs(l-mid)-1,abs(r-mid)-1)<<" "<<min(abs(l-mid)-1,abs(r-mid)-1)<<"\n";
    }
}
