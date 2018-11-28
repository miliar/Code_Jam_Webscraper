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
    string N;
    cin >> N;
    reverse(all(N));
    string ans = "";
    int hoge = false;
    rep(i, N.size()) {
      int mn = N[i];
      bool izryt = true;
      reps(j, i, N.size()) {
	if(mn < N[j]) izryt = false;
	if(N[j] < mn) mn = N[j];
      }
      if(izryt) {
	ans += N[i];
      } else {
	ans += "9";
	int j = i+1;
	while(j < N.size() && N[j] == '0') N[j++] = '9';
	if(j < N.size()) N[j]--;
      }
    }
    while(ans.back() == '0') ans.pop_back();
    reverse(all(ans));
    cout << "Case #" << t+1 << ": " << ans << endl;
  }

  return 0;
}
