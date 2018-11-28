#include <bits/stdc++.h>
using namespace std;

#define int long long
#define inf 1000000007LL

#define rep(i, n) for(int i = 0; i < (n); i++)
#define rrep(i, n) for(int i = (n) - 1; i >= 0; i--)
#define trep(i, n) for(int i = 0; i <= (n); i++)
#define rep1(i, n) for(int i = 1; i <= (n); i++)
#define mfor(i, s, t) for(int i = (s); i < (t); i++)
#define tfor(i, s, t) for(int i = (s); i <= (t); i++)

pair<bool, string> solve(string in, int nk, int nb) {
  if(in.size() == nk) {
    return make_pair(true, "");
  }
  int s = in[nk] - '0';
  if(s < nb) {
    return make_pair(false, "");
  }
  else if(s == nb) {
    auto r = solve(in, nk + 1, nb);
    if(r.first) {
      return make_pair(true, in[nk] + r.second);
    }
    else {
      return make_pair(false, "");
    }
  }
  else {
    auto r = solve(in, nk + 1, s);
    if(r.first) {
      return make_pair(true, in[nk] + r.second);
    }
    else {
      string ret;
      ret += in[nk] - 1;
      rep(i, in.size() - nk - 1) {
        ret += '9';
      }
      return make_pair(true, ret);
    }
  }
}

signed main() {
  int t;
  cin >> t;
  rep1(_, t) {
    string s;
    cin >> s;
    auto r = solve(s, 0, 1);
    if(!r.first) {
      rep(i, s.size() - 1) {
        r.second += '9';
      }
    }
    cout << "Case #" << _ << ": " << r.second << endl;
  }
}
