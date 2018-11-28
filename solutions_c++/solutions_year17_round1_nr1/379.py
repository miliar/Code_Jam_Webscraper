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

char cake[26][26];
bool hasc[26];

int main()
{
  IOS;
  int T;
  cin >> T;
  int r, c;
  for (int tt = 1; tt <= T; ++tt) {
    cin >> r >> c;
    for (int i = 0; i < r; ++i) {
      hasc[i] = false;
      for (int j = 0; j < c; ++j) {
        cin >> cake[i][j];
        if (cake[i][j] != '?')
          hasc[i] = true;
      }
    }

    int st = 0;
    while (!hasc[st]) {
      ++st;
    }

    for (int i = st; i < r; ++i) {
      if (hasc[i]) {
        int jst = 0;
        while (cake[i][jst] == '?')
          ++jst;

        for (int x = 0; x < jst; ++x) {
          cake[i][x] = cake[i][jst];
        }
        for (int j = jst; j < c; ++j) {
          if (cake[i][j] == '?')
            cake[i][j] = cake[i][j - 1];
        }
      }
      else {
        for (int j = 0; j < c; ++j) {
          cake[i][j] = cake[i - 1][j];
        }
      }
    }

    for (int i = st - 1; i >= 0; --i) {
      for (int j = 0; j < c; ++j) {
        cake[i][j] = cake[i+1][j];
      }
    }

    cout << "Case #" << tt << ": ";
    for (int i = 0; i < r; ++i) {
      cout << "\n";
      for (int j = 0; j < c; ++j) {
        cout << cake[i][j];
      }
    }
    cout << endl;
  }
  return 0;
}
