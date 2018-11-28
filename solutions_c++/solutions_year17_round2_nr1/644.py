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
    int D, N;
    cin >> D >> N;
    vector< pair<double, double> > H(N);
    rep(i, N) cin >> H[i].first >> H[i].second;
    sort(all(H));
    vector<double> tim(N);
    rep(i, N) {
      tim[N-1-i] = (D-H[i].first)/H[i].second;
      if(i) chmax(tim[N-1-i], tim[N-i]);
    }
    cout << D/tim[0] << endl;
  }

  return 0;
}
