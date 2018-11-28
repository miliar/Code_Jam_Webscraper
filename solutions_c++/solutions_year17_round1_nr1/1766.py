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
const int MOD =1e9 + 7;
const int N = 1e5 +3 ;
ll v[N],st[N],ans=0,st2[N]={0};
vi adj[N];
ll dfs(ll u)
{
    v[u]=1;
    vi q;
    for(auto it:adj[u])
        if(!v[it])
        q.pb(dfs(it));
    if(q.size()<=1)
        return 1;
    sort(q.begin(),q.end());
    return 1+q[q.size()-1]+q[q.size()-2];
}
int main()
{
  freopen("A-large (1).in","r",stdin);
freopen("aoutput.out","w",stdout);
    ll t;
    cin>>t;
    cout<<setprecision(100);
    rep(z,t)
    {
        ll r,c;
        cin>>r>>c;
        char s[r+2][c+2];
        cout<<"Case #"<<z+1<<":\n";
        rep(i,r)
        rep(j,c)
        cin>>s[i][j];
        rep(i,r)
        rep(j,c)
        {
            if(s[i][j]!='?')
            {char p=s[i][j];
                for(int k=j-1;k>=0 && s[i][k]=='?';k--)
                    s[i][k]=p;
                for(int k=j+1;k<c && s[i][k]=='?';k--)
                    s[i][k]=p;
            }
        }
        rep(i,r)
        rep(j,c)
        {
            if(s[i][j]=='?')
            {
                for(int k=0;k<c;k++)
                {
                    if(i>0)
                        s[i][k]=s[i-1][k];
                    else
                        s[i][k]=s[i+1][k];
                }
            }
        }
        for(int i=r-1;i>=0;i--)
        {
            for(int j=0;j<c;j++)
            {
                if(s[i][j]=='?'){
                        for(int k=0;k<c;k++)
                        {
                            if(i<r-1)
                    s[i][k]=s[i+1][k];
                    else
                        s[i][k]=s[i-1][k];
                        }
                }
            }
        }
        rep(i,r)
        {
            rep(j,c)
            cout<<s[i][j];
            cout<<"\n";
        }
    }
}
