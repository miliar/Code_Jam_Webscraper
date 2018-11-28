#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define FOR(i, to) for (int i = 0; i < (to); ++i)


typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<vector<int> > vvi;
typedef vector<vll> vvll;
typedef vector<pair<int, int> > vpi;
typedef pair<double,double> pdd;
typedef pair<ll,ll> pll;


int N, tt, T, P, C, M;
string S;

map<vi,int> h;

void afis(vi v) {
  for(auto x : v) {
    cout << x << " ";
  }
  cout << endl;
}

vi v[2020];
int nr[2020];
pii ch(int val) {
  int fr = 0;
  int ret=0;
  for(int i=1;i<=N;++i) {
    if(v[i].size()<=val) {
      fr += val - sz(v[i]);
    } else {
      if(fr < (sz(v[i])-val)) {
        return mp(0,0);
      }else {
        fr -= (sz(v[i]) - val);
        ret += (sz(v[i]) - val);
      }
    }
  }
  return mp(1,ret);
}
int main() {
  cin >> T;
  while(T--) {
    ++tt;
    cin >> N >> C >> M;
    FOR(i,N+10) v[i].clear();
    FOR(i,C+10) nr[i] = 0;
    int mmax = 0;
    FOR(i,M) {
      int x,y;
      cin >> x >> y;
      v[x].pb(y);
      nr[y]++;
      mmax = max(mmax,nr[y]);
    }
   // ch(1);
   // return 0;
    int st = mmax;
    int dr = 10100;
    int ret = 0;
    int ret1 = 0;
    while(st <= dr) {
      int mij = (st+dr)/2;
      auto x = ch(mij);
      if(x.fs) {
        ret = mij;
        ret1=x.sc;
        dr = mij - 1;
      } else {
        st = mij + 1;
      }
    }
    cout << "Case #" << tt <<": ";
    cout << ret << " " << ret1 << endl;
  }
}
