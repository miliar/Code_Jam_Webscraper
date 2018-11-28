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

signed main()
{
  cin.tie(0);
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(12);

  int T;
  cin >> T;
  rep(t, T) {
    cout << "Case #" << t+1 << ": ";
    int N, K;
    cin >> N >> K;
    priority_queue< tuple<int, int, int> > que;
    que.emplace(N, 0, N);
    rep(i, K) {
      int w, l, r;
      tie(w, l, r) = que.top(); que.pop();
      l = -l;
      int m = (l + r) / 2;
      que.emplace(m-l, -l, m);
      que.emplace(r-m-1, -m-1, r);
      if(i == K-1) {
	int a, b;
	tie(a, b) = minmax(m-l, r-m-1);
	cout << b << " " << a << endl;
      }
    }
  }

  return 0;
}
