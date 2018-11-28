#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    string S;
    int K;
    cin >> S >> K;

    int number = 0;
    vector<int> m(K, -1);
    vector<int> p(K, 0);
    if (S[0] != '+') {
      m[0] = 0;
    }
    for (int i=1;i<S.length();i++) {
      if (S[i] != S[i-1]) {
        if (m[i%K] == -1) {
          m[i%K] = i;
        }
        else {
          p[i%K] += (i - m[i%K]);
          m[i%K] = -1;
        }
      }
    }
    if (m[S.length()%K] != -1) {
      p[S.length()%K] += S.length() - m[S.length()%K];
      m[S.length()%K] = -1;
    }

    bool possible = true;
    for (int i=0;i<K;i++) {
      if (m[i] != -1) possible = false;
      number += p[i];
    }

    if (possible) {
      printf("Case #%d: %d\n", t, number/K);
    }
    else {
      printf("Case #%d: IMPOSSIBLE\n", t);
    }
  }

}
