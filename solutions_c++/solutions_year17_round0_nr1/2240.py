#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vec<int> vi;

void solve(int testcase) {
  cout << "Case #" << testcase << ": ";
  string S;
  int K;
  cin >> S >> K;
  int result = 0;
  for (int i = 0; i < sz(S) - K + 1; ++i) {
    if (S[i] == '-') {
      result += 1;
      for (int j = 0; j < K; ++j) {
        if (S[i + j] == '-') S[i + j] = '+'; else S[i + j] = '-';
      }
    }
  }
  for (int i = sz(S) - K + 1; i < sz(S); ++i) {
    if (S[i] == '-') {
      result = -1;
      break;
    }
  }
  if (result == -1) {
    cout << "IMPOSSIBLE\n";
  } else {
    cout << result << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int testcases;
  cin >> testcases;
  FOR(testcase, 1, testcases + 1) {
    cerr << "Case " << testcase << "/" << testcases << endl;
    solve(testcase);
  }

  return 0;
}
