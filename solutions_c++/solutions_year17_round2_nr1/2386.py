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

//string stringtonum(ll num){ text= boost::lexical_cast<string>(Number); return text;};
//Number = boost::lexical_cast<Type>(Text);
const ll INF = 1e18;
const int MOD =1e9 + 7;
const int N = 1e5 +3 ;
ll v[N],st[N],ans=0,st2[N]={0};
vi adj[N];

int main()
{
 freopen("A-large (2).in","r",stdin);
 freopen("aoutput.out","w",stdout);
 cout<<setprecision(10);
    ll t;
    cin>>t;
    rep(z,t)
    {
        //string s;
        //cin>>s;
        ll d,n;
        cin>>d>>n;
        double a,b;
        ii p[n+2];
        vector<double> v;
        rep(i,n)
        {
            cin>>a>>b;
            double t=double(d-a)/double(b);
            v.pb(t);
        }
        sort(v.begin(),v.end());
        cout<<"Case #"<<z+1<<": ";
        double mx=double(d)/double(v[v.size()-1]);
        cout<<mx<<"\n";
    }
}
