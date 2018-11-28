#include <bits/stdc++.h>
#include <unistd.h>

using namespace std;

#define fst first
#define snd second
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)

template<typename A, typename B>
ostream& operator<<(ostream& out, const pair<A, B>& p)
{
  out << "( " << p.first << ", " << p.second << " )";
  return out;
}

template<typename T>
ostream& operator<<(ostream& out, const vector<T>& v)
{
  out << "[ ";
  for (auto it : v)
    out << it << " ";
  out << "]";
  return out;
}

int main()
{
  IOS;
  int T;
  cin >> T;
  int n, p;
  int gs[101];
  int mod[5];
  for (int tt = 1; tt <= T; ++tt) {
    cin >> n >> p;
    for (int i = 0; i < p; ++i) {
      mod[i] = 0;
    }
    for (int i = 0; i < n; ++i) {
      cin >> gs[i];
      gs[i] %= p;
      mod[gs[i]] += 1;
    }

    int ans = 0;
    ans += mod[0];
    if (p == 2) {
      ans += (mod[1] + 1) / 2;
    }
    else if (p == 3) {
      int pair = min(mod[1], mod[2]);
      int r = max(mod[1], mod[2]) - pair;
      ans += pair;
      ans += (r + 2) / 3;
    }
    else if (p == 4) {
      int pair = min(mod[1], mod[3]);
      int r1 = max(mod[1], mod[3]) - pair;
      int r2 = mod[2] % 2;
      ans += pair;
      ans += mod[2] / 2;
      if (r2) {
        ans += 1;
        r1 = max(0, r1 - 2);
      }
      ans += (r1 + 3) / 4;
    }

    cout << "Case #" << tt << ": ";
    cout << ans << endl;
  }
  return 0;
}
