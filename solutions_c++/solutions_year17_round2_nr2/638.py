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
    vector<pint> col(6);
    int N;
    cin >> N;
    rep(i, 6) {
      cin >> col[i].first;
      col[i].second = i;
    }
    sort(all(col), greater<pint>());
    string ans = "";
    rep(i, col[0].first) {
      if(col[0].second == 0) ans += "R";
      else if(col[0].second == 2) ans += "Y";
      else if(col[0].second == 4) ans += "B";
    }
    rep(i, col[1].first) {
      string tmp = ans.substr(0, i*2);
      if(col[1].second == 0) tmp += "R";
      else if(col[1].second == 2) tmp += "Y";
      else if(col[1].second == 4) tmp += "B";
      ans = tmp + ans.substr(i*2);
    }
    reverse(all(ans));
    rep(i, col[2].first) {
      /*
      string tmp = ans.substr(ans.size()-1-i*2);
      if(col[2].second == 0) tmp = "R" + tmp;
      else if(col[2].second == 2) tmp = "Y" + tmp;
      else if(col[2].second == 4) tmp = "B" + tmp;
      ans = ans.substr(0, N-1-i*2) + tmp;
      */
      string tmp = ans.substr(0, i*2+1);
      if(col[2].second == 0) tmp += "R";
      else if(col[2].second == 2) tmp += "Y";
      else if(col[2].second == 4) tmp += "B";
      ans = tmp + ans.substr(i*2+1);
    }
    reverse(all(ans));
    //assert(ans.size()==N);
    //cout<<ans<<endl;
    bool flag = true;
    rep(i, ans.size()) if(ans[i] == ans[(i+1)%ans.size()]) flag = false;
    cout << (flag ? ans : "IMPOSSIBLE") << endl;
  }

  return 0;
}
