#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> VI;

const int MAX_N = 1005;

void solve() {
  int K;
  string S;
  cin >> S;
  cin >> K;

  VI v;
  for (int i = 0; i < S.size(); i++) {
    char c;
    if (S[i] == '+') {
      v.push_back(1);
    } else {
      v.push_back(0);
    }
  }

  int res = 0;
  for (int i = 0; i < S.size() - K + 1; i++) {
    if (v[i] == 0) {
      res++;
      for (int j = i; j < i+K; j++) {
        v[j] ^= 1;
      }
    }
  }

  bool ok = true;
  for (int i = S.size()-K+1; i < S.size(); i++) {
    ok &= (v[i] == 1);
  }

  if (ok) {
    cout << res;
  } else {
    cout << "IMPOSSIBLE";
  }
}

int main() {
  int N;
  cin >> N;

  for (int i = 0; i < N; i++) {
    cout << "Case #" << (i+1) << ": ";
    solve();
    cout << endl;
  }

  return 0;
}
