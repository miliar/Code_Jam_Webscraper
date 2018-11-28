#include <iostream>
#include <unordered_set>
#include <cstring>

using namespace std;

static void flip(string S, int K) {
  int f = 0;
  char *s = strdup(S.c_str());
  for (int i = 0; i < S.size() - K + 1; ++i) {
    if (s[i] == '+') continue;
    for (int j = i; j < i + K; ++j) {
      s[j] = (s[j] == '+') ? '-' : '+';
    }
    ++f;
  }
  for (int i = 0; i < S.size(); ++i) {
    if (s[i] == '-') {
      cout << "IMPOSSIBLE";
      free(s);
      return;
    }
  }
  free(s);
  cout << f;
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int K;
    string S;
    cin >> S >> K;
    cout << "Case #" << i+1 << ": ";
    flip(S, K);
    cout << endl;
  }
  return 0;
}

