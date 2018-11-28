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

bool used[404];

signed main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(12);

  int T; cin >> T;
  rep(t, T) {
    cout << "Case #" << t+1 << ": ";
    int N, P, M = 0;
    cin >> N >> P;
    int sum = 0, ans = N;
    vint G(N);
    rep(i, N) {
      cin >> G[i];
      G[i] %= P;
      sum += G[i];
    }
    sort(all(G));
    reverse(all(G));
    memset(used, false, sizeof(used));
    rep(i, N) if(G[i] == 0) used[i] = true;
    rep(i, N) {
      if(used[i]) continue;
      used[i] = true;
      int j = N-1;
      int hoge = G[i];
      while(j > i && hoge < P) {
	if(!used[j]) {
	  hoge += G[j], ans--;
	  if(hoge <= P) used[j] = true;
	  else G[j] = hoge-P;
	}
	j--;
      }
    }
    cout << ans << endl;
  }


  return 0;
}
