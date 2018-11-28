#include <iostream>
#include <string.h>

using namespace std;

void solve(bool *s, int K, int n)
{
  int ans = 0;

  for (int i = 0; i <= n - K; i++) {
    if (!s[i]) {
      ans++;
      for (int j = 0; j < K; j++) {
        s[i + j] = !s[i + j];
      }
    }
  }
  for (int i = 0; i < n; i++) {
    if (!s[i]) {
      ans = -1;
    }
  }

  if (ans == -1) {
    cout << "IMPOSSIBLE";
  }
  else {
    cout << ans;
  } 
}

int main()
{
  int T;
  cin >> T;
  char *S = new char[10000];
  bool *s = new bool[10000];
  for (int t = 1; t <= T; t++) {
    int K;

    cin >> S >> K;
    for (int i = 0; i < strlen(S); i++) {
      s[i] = (S[i] == '+');
    }

    cout << "Case #" << t << ": ";
    solve(s, K, strlen(S));
    cout << "\n";
  }

  delete[] S;
  delete[] s;
  return 0;
}

