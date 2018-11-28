#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define repr(i,n) for(int i=(int)(n-1);i>=0;i--)
#define rep(i,n) repl(i,0,n)
#define each(itr,v) for(auto itr:v)
#define pb(s) push_back(s)
#define all(x) (x).begin(),(x).end()
#define dbg(x) cout << #x" = " << x << endl
#define print(x) cout << x << endl
#define maxch(x,y) x=max(x,y)
#define minch(x,y) x=min(x,y)
#define uni(x) x.erase(unique(all(x)),x.end())
#define exist(x,y) (find(all(x),y)!=x.end())
#define bcnt(x) bitset<32>(x).count()

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> P;
typedef pair<double, P> PDP;
typedef pair<P, int> PPI;
typedef pair<int, P> PIP;
typedef pair<ll, ll> PL;
typedef pair<P, ll> PPL;
typedef set<int> S;

#define INF INT_MAX/3
#define MAX_N 1000000001
#define pi acos(-1)


int main(){
  cin.sync_with_stdio(false);
  int t;
  cin >> t;
  rep(ii, t) {
    int n, k;
    cin >> n >> k;

    vector<PL> v;
    rep(i, n) {
      ll r, h;
      cin >> r >> h;
      v.pb(PL(r, h));
    }
    sort(all(v));

    vector<double> d(0);
    rep(i, k - 1) d.pb(2.0*v[i].fi*pi*v[i].se);

    double ans = 0;
    repl(i, k - 1, n) {
      double m = v[i].fi*v[i].fi*pi + 2.0*v[i].fi*pi*v[i].se;
      sort(all(d), greater<double>());
      rep(j, k - 1) {
        m += d[j];
      }
      maxch(ans, m);
      d.pb(2.0*v[i].fi*pi*v[i].se);
    }


    printf("Case #%d: %.10f\n", ii + 1, ans);
  }

  return 0;
}