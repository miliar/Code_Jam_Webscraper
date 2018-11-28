#include <bits/stdc++.h>
#include <time.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<ll> vi;
typedef pair<ll, ll> pii;
typedef vector<pii > vii;
typedef vector<vector<ll> > vvi;
typedef vector<vector<pair<ll, ll> > > vvii;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,s,e) for(ll i=(s);i<(e);++i)
#define repr(i,s,e) for(ll i=(e);i>(s);--i)

const ll MOD = 1e9+7;
const ll INF = 1e14;
const ll TE3 = 1005;
const ll TE5 = 100005;

bool PRINT_TIME_OF_EXEC = false;

struct node {
  ll lv,rv,idx;
};

struct node_cmp {
  bool operator () (const node& lhs, const node& rhs) {
    ll a,b,c;
    a=min(lhs.lv,lhs.rv);
    b=min(rhs.lv,rhs.rv);
    if(a<b) return true;
    if(a>b) return false;
    a=max(lhs.lv,lhs.rv);
    b=max(rhs.lv,rhs.rv);
    if(a<b) return true;
    if(a>b) return false;
    return lhs.idx>rhs.idx;
  }
};

int main() {
  ll start_time = clock();
  node nn,tmp;
  ll t;
  cin>>t;
  ll n,k;
  rep(ii,0,t) {
    cin>>n>>k;
    vi a;
    vi v(n+2,0),lv(n+2,0),rv(n+2,n+1);
    v[0]=v[n+1]=1;
    // lv[n+1]=n+1;rv[0]=0;
    // rep(i,0,n+2) v[i]=i;
    a.pb(0);
    a.pb(n+1);
    rep(i,1,k+1) {
      priority_queue<node,vector<node>,node_cmp> pq;
      rep(j,1,n+1) {
        if(v[j]) continue;
        nn.idx=j;
        ll y=*(upper_bound(a.begin(),a.end(),j)-1);
        nn.lv=j-y-1;
        nn.rv=*(lower_bound(a.begin(),a.end(),j))-j-1;
        // cout<<i<<" "<<y<<" "<<nn.lv<<" "<<nn.rv<<endl;
        pq.push(nn);
      }
      tmp=pq.top();
      // cout<<tmp.idx<<" "<<tmp.lv<<" "<<tmp.rv<<endl;
      v[tmp.idx]=1;
      a.pb(tmp.idx);
      // rep(i,0,n+2) cout<<v[i]<<" ";
      // cout<<endl;
      sort(a.begin(),a.end());
    }
    cout<<"Case #"<<ii+1<<": "<<tmp.rv<<" "<<tmp.lv<<endl;
  }

  ll end_time = clock();
  if(PRINT_TIME_OF_EXEC) cout<<"Time of exec. "<<((double)end_time-start_time)/CLOCKS_PER_SEC<<endl;
  return 0;
}
