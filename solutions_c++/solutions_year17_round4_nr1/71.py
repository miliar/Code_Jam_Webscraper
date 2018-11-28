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


int N, tt, T, P;
string S;

map<vi,int> h;

void afis(vi v) {
  for(auto x : v) {
    cout << x << " ";
  }
  cout << endl;
}

int make(vi v) {
  if(h.count(v)) return h[v];
  
  int ret = 0;
  if(v[0] == 0) ++ret;
  int ras = 0;
  int ok = 0;
  if(v[1]) {
    ok = 1;
    vi va = v;
    va[1]--;
    va[0] += 1;
    va[0] %= v[4];
    ras = max(ras,make(va));
  }
  if(v[2]) {
  ok = 1;
    vi va = v;
    va[2]--;
    va[0] += 2;
    va[0] %= v[4];
    ras = max(ras,make(va));
  }
  if(v[3]) {
  ok = 1;
    vi va = v;
    va[3]--;
    va[0] += 3;
    va[0] %= v[4];
    ras = max(ras,make(va));
  }
  ret = min(ret,ok);
  h[v] = ras + ret;
  return h[v];
}

int main() {
  cin >> T;
  while(T--) {
    ++tt;
    cin >> N >> P;
    vector<int> v;
    int ret = 0;
    v.resize(5);
    v[4] = P;
    for(int i=1;i<=N;++i) {
      int x;
      cin >> x;
      x %= P;
      if(x == 0) ++ ret;
      else v[x]++;
    }
    cout << "Case #" << tt <<": ";
    cout << make(v)+ret << endl;
  }
}
