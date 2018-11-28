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

const int MAX = 51;

int n, p;
int target[MAX];
int ingred[MAX][MAX];
int least[MAX][MAX];
int most[MAX][MAX];

int pos[MAX];

bool check()
{
  int maxl = -1000;
  int minr = 100000000;
  for (int i = 0; i < n; ++i) {
    maxl = max(maxl, least[i][pos[i]]);
    minr = min(minr, most[i][pos[i]]);
  }
  return (maxl <= minr);
}

int main()
{
  IOS;
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; ++tt) {
    cin >> n >> p;

    for (int i = 0; i < n; ++i)
      cin >> target[i];

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        cin >> ingred[i][j];
      }
      sort(ingred[i], ingred[i] + p);
    }

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        int approx = ingred[i][j] / target[i];
        least[i][j] = approx;
        while (ingred[i][j] * 10 <= least[i][j] * target[i] * 11)
          least[i][j]--;
        least[i][j]++;
        most[i][j] = approx;
        while (ingred[i][j] * 10 >= most[i][j] * target[i] * 9)
          most[i][j]++;
        most[i][j]--;
      }
    }

    for (int i = 0; i < n; ++i)
      pos[i] = 0;

    int ans = 0;

    bool running = true;
    while (running) {
      bool ret = check();
      if (ret) {
        ans += 1;
        for (int i = 0; i < n; ++i) {
          pos[i] += 1;
          if (pos[i] == p)
            running = false;
        }
      }
      else {
        int argminr = 0;
        for (int i = 0; i < n; ++i) {
          if (most[i][pos[i]] < most[argminr][pos[argminr]])
            argminr = i;
        }
        pos[argminr] += 1;
        if (pos[argminr] == p)
          running = false;
      }
    }

    cout << "Case #" << tt << ": " << ans << endl;
  }
  return 0;
}
