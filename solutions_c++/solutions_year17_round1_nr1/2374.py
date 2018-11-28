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
typedef pair<P, int> PPI;
typedef pair<int, P> PIP;
typedef pair<ll, ll> PL;
typedef pair<P, ll> PPL;
typedef set<int> S;

#define INF INT_MAX/3
#define MAX_N 1000000001

int r, c;
string cake[25];
bool check[25][25];

void fill(int i, int j, char cc) {
  check[i][j] = true;
  int p = 1, q = -1, l = -1, s = 1;
  while (j + p < c && cake[i][j + p] == '?') cake[i][j + p] = cc, check[i][j + p] = true, p++;
  while (j + q >= 0 && cake[i][j + q] == '?') cake[i][j + q] = cc, check[i][j + q] = true, q--;
  while(i + l >= 0) {
    bool ok = true;
    repl(k, j + q + 1, j + p) if (cake[i + l][k] != '?') ok = false;
    if (ok) repl(k, j + q + 1, j + p) cake[i + l][k] = cc, check[i + l][k] = true;
    else break;
    l--;
  }
  while(i + s < r) {
    bool ok = true;
    repl(k, j + q + 1, j + p) if (cake[i + s][k] != '?') ok = false;
    if (ok) repl(k, j + q + 1, j + p) cake[i + s][k] = cc, check[i + s][k] = true;
    else break;
    s++;
  }
}

int main(){
  cin.sync_with_stdio(false);
  int t;
  cin >> t;
  rep(ii, t) {
    cin >> r >> c;

    rep(i, r) cin >> cake[i];
    rep(i, r)rep(j, c) check[i][j] = false;

    repr(i, r) {
      rep(j, c) {
        if (cake[i][j] != '?' && !check[i][j]) {
          fill(i, j, cake[i][j]);
        }
      }
    }

    cout << "Case #" << ii + 1 << ":\n";
    rep(i, r) cout << cake[i] << endl;
  }

  return 0;
}