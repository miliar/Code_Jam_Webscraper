#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

string flip(string S, int p, int K) {
  for (int i = p; i < p + K; i++) {
    S = S.replace(i, 1, ((S[i] == '+') ? "-" : "+")); 
  }
  return S; 
}

bool hasBlanks(string S) {
  bool ret = false; 
  for (int i = 0; i < S.length(); i++) {
    if (S[i] == '-') ret = true; 
  }
  return ret; 
}

int main() {
  int T, N, K;
  string S; 
  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> S >> K;
    int flipCount = 0;
    for (int p = 0; p <= S.length() - K; p++) {
      if (S[p] == '-') {
        S = flip(S, p, K);
        flipCount++;
      } 
    }
    if (hasBlanks(S)) {
      cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << i+1 << ": " << flipCount << endl; 
    }
  }
}
