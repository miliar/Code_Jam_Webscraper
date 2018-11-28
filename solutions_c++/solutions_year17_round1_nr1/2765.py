#include <bits/stdc++.h>

using namespace std;

#define int long long
#define all(v) begin(v), end(v)
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define reps(i, s, n) for(int i = (int)(s); i < (int)(n); i++)

template<class T1, class T2> void chmin(T1 &a, T2 b){if(a>b)a=b;}
template<class T1, class T2> void chmax(T1 &a, T2 b){if(a<b)a=b;}

using pint = pair<int, int>;
using tint = tuple<int, int, int>;
using vint = vector<int>;

const int inf = 1LL << 55;
const int mod = 1e9 + 7;

struct CumulativeSum2D {
  vector< vector<int> > data;
  CumulativeSum2D(int H, int W):data(++H, vector<int>(++W)){}
  inline void add(int x, int y, int z) {
    data[++y][++x] += z;
  }
  void build() {
    for(int i = 1; i < data.size(); i++)
      for(int j = 1; j < data[i].size(); j++)
	data[i][j] += data[i][j-1] + data[i-1][j] - data[i-1][j-1];
  }
  inline int query(int sx, int sy, int gx, int gy) {
    return data[gy][gx] - data[gy][sx] - data[sy][gx] + data[sy][sx];
  }
};

signed main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(12);

  int T; cin >> T;
  rep(t, T) {
    cout << "Case #" << t+1 << ":" << endl;
    int R, C;
    cin >> R >> C;
    CumulativeSum2D sum(R, C);
    char grid[33][33];
    bool init[33][33] = {{}};
    bool used[33][33] = {{}};
    rep(i, R) rep(j, C) {
      cin >> grid[i][j];
      if(grid[i][j] == '?') continue;
      sum.add(j, i, 1);
      init[i][j] = true;
    }
    sum.build();
    rep(i, R) rep(j, C) {
      if(used[i][j]) continue;
      int mx = 1, sr = i, sc = j, gr = i+1, gc = j+1;
      reps(k, i+1, R+1) reps(l, j+1, C+1) {
	if(sum.query(j, i, l, k) == 1) {
	  if(mx < (k-i)*(l-j)) {
	    sr = i, sc = j, gr = k, gc = l;
	    mx = (k-i)*(l-j);
	  }
	}
      }
      char ini;
      reps(k, sr, gr) reps(l, sc, gc) {
	if(init[k][l]) ini = grid[k][l];
      }
      reps(k, sr, gr) reps(l, sc, gc) {
	grid[k][l] = ini;
	used[k][l] = true;
      }
    }
    rep(i, R) {
      rep(j, C) cout << grid[i][j];
      cout << endl;
    }
  }

  return 0;
}
