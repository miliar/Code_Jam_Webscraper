#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

const int N_MAX = 2000;
int N, K;
int pancakes[N_MAX];
bool flips[N_MAX];

void init() {
  string S;
  cin >> S >> K;
  N = S.length();
  assert(K <= N);
  for (int i = 0; i < N; i++) {
    pancakes[i] = (S[i] == '+' ? 0 : 1);
    flips[i] = false;
  }
  // try to make them all 0
}

void solve_case(int t) {
  init();

  for (int i = 0; i < K; i++) {
    for (int j = i; j + K < N; j += K) {
      if (pancakes[j] == 1) {
        flips[j] ^= true;
        flips[j+1] ^= true;
        pancakes[j] = 0;
        pancakes[j + K] = 1 - pancakes[j + K];
      }
    }
  }

  if (pancakes[N - K] == 1) {
    flips[N - K] ^= true;
    for (int i = N - K; i < N; i++)
      pancakes[i] = 1 - pancakes[i];
  }

  for (int i = 0; i < N; i++) {
    if (pancakes[i] != 0) {
      cout << "Case #" << t << ": IMPOSSIBLE\n";
      return;
    }
  }

  int answer = 0;
  for (int i = 0; i < N; i++)
    if (flips[i])
      answer++;
  cout << "Case #" << t << ": " << answer << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
