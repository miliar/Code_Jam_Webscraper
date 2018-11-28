#include <iostream>
#include <string>
#include <cstdio>
using namespace std;


int peeps[1001];

void solve(int CASE) {
  string pancakes;
  int k;

  cin >> pancakes >> k;

  int flips = 0;
  for (int i = 0; i + k <= pancakes.size(); i++) {
    if (pancakes[i] == '-') {
      flips++;
      for (int j = 0; j < k; j++) {
        pancakes[i+j] = pancakes[i+j] == '-' ? '+' : '-';
      }
    }
  }

  bool possible = true;
  for (auto c : pancakes) {
    if (c == '-') {
      possible = false;
    }
  }

  if (!possible)
    printf("Case #%d: IMPOSSIBLE\n", CASE);
  else
    printf("Case #%d: %d\n", CASE, flips);
}

int main() {
  int T;

  cin >> T;

  for (int i = 1; i <= T; i++) {
    solve(i);
  }

  return 0;
}
