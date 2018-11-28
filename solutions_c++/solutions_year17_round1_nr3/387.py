#pragma GCC optimize ("O2")
#include <bits/stdc++.h>
#include <unistd.h>

using namespace std;

#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
#define fst first
#define snd second

template<typename A, typename B>
ostream& operator <<(ostream& s, const pair<A, B>& p)
{
  return s << "(" << p.first << "," << p.second << ")";
}
template<typename T>
ostream& operator <<(ostream& s, const vector<T>& c)
{
  s << "[ ";
  for (auto it : c) s << it << " ";
  s << "]";
  return s;
}

const int MAX = 101;
const int INF = 1000000000;
int table[MAX][MAX][MAX][MAX];

int hd, ad, hk, ak, b, d;

int solve(int nhd, int nad, int nhk, int nak)
{
  if (nhk <= 0) {
    return 0;
  }
  if (nhd <= 0) {
    return INF;
  }

  if (nak < 0)
    nak = 0;

  if (nad > nhk) {
    nad = nhk;
    return 1;
  }

  if (table[nhd][nad][nhk][nak] > -1)
    return table[nhd][nad][nhk][nak];

  table[nhd][nad][nhk][nak] = INF;
  int ans = INF;
  if (nak > 0 && d > 0) {
    int tak = nak - d;
    if (tak < 0)
      tak = 0;
    ans = min(ans, 1 + solve(nhd - tak, nad, nhk, tak));
  }
  if (nad < nhk && b > 0) {
    ans = min(ans, 1 + solve(nhd - nak, nad + b, nhk, nak));
  }
  // attack
  ans = min(ans, 1 + solve(nhd - nak, nad, nhk - nad, nak));
  // cure
  ans = min(ans, 1 + solve(hd - nak, nad, nhk, nak));

  table[nhd][nad][nhk][nak] = ans;

  return ans;
}

int main()
{
  IOS;
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; ++tt) {
    cin >> hd >> ad >> hk >> ak >> b >> d;

    //if (2*ak - 3*d >= hd) {
      //if (
      //cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
      //continue;
    //}

    for (int i = 0; i <= hd; ++i) {
      for (int j = 0; j <= hk; ++j) {
        for (int k = 0; k <= hk; ++k) {
          for (int l = 0; l <= ak; ++l) {
            table[i][j][k][l] = -1;
          }
        }
      }
    }

    int ans = solve(hd, ad, hk, ak);
    if (ans == INF)
      cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
    else
      cout << "Case #" << tt << ": " << ans << endl;
  }
  return 0;
}
