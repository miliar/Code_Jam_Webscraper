#include <iostream>
#include <string>

using namespace std;

long long m[128][128];
long long e[128];
long long s[128];

double dp[128];

long long d(int j, int i) {
  long long s = 0;
  for (; j < i; ++j) {
    s += m[j][j+1];
  }
  return s;
}

int main()
{
  cout.precision(20);
  uint nCase;
  cin >> nCase;
  for (auto iCase = 1; iCase <= nCase; ++iCase) {
    uint n, q;
    cin >> n >> q;

    for (auto i = 0; i < n; ++i) {
      cin >> e[i] >> s[i];
    }
    for (auto i = 0; i < n; ++i) {
      for (auto j = 0; j < n; ++j) {
        cin >> m[i][j];
      }
    }
    for (auto i = 0; i < q; ++i) {
      uint f, t;
      cin >> f >> t;
    }

    for (auto i = 0; i < 128; ++i) {
      dp[i] = 1e16;
    }
    dp[0] = 0.0;

    for (auto i = 1; i < n; ++i) {
      double cand = 1e16;
      for (auto j = 0; j < i; ++j) {
        long long dist = d(j, i);
        if (e[j] >= dist) {
          cand = min(cand, dp[j] + (1.0*dist)/s[j]);
        }
      }
      dp[i] = cand;
    }

    cout << "Case #" << iCase << ":";

    for (auto i = 0; i < q; ++i) {
      cout << " " << dp[n-1];
    }

    cout << endl;
  }

  return 0;
}
