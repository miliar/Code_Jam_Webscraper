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
    freopen("A-large.in","r",stdin);
    freopen("aoutput.out","w",stdout);
    ll t;
    cin>>t;
    rep(z,t)
    {
        string s;
        cin>>s;
        ll k;
        cin>>k;
        ll ans=0;
        cout<<"Case #"<<z+1<<": ";
        rep(i,s.size()-k+1)
        {
            if(s[i]=='-')
            {
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
                ans++;
            }
        }
        ll flag=0;
        //cout<<s.size()-k;
        for(int i=s.size()-k;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                flag=1;
                break;
            }
        }
        if(flag)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<"\n";
    }
}
