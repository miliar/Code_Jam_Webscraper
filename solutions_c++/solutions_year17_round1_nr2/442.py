#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

const int N_MAX = 100, P_MAX = 100;
int N, P;
int recipe[N_MAX];
int packages[N_MAX][P_MAX]; // type, package #

int cursors[N_MAX];

void init() {
  cin >> N >> P;
  for (int i = 0; i < N; i++)
    cin >> recipe[i];
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < P; j++)
      cin >> packages[i][j];
  }

  for (int i = 0; i < N; i++) {
    cursors[i] = 0;
    sort(packages[i], packages[i] + P);
  }
}

// returns success or not
bool make_kit(int servings) {
  for (int i = 0; i < N; i++) {
    int cur = cursors[i];
    if (cur >= P) return false;

    int min_amt = (servings * recipe[i] * 9 + 9) / 10;
    int max_amt = (servings * recipe[i] * 11) / 10;

    while (cur < P && packages[i][cur] < min_amt)
      cur++;
    cursors[i] = cur;
    if (cur == P || packages[i][cur] > max_amt) // too large
      return false;
  }

  for (int i = 0; i < N; i++)
    cursors[i]++;
  // cout << "success " << servings << endl;
  return true;
}



void solve_case(int t) {
  init();

  int servings = 1;
  int kits = 0;
  while (cursors[0] < P) {
    bool success = make_kit(servings);
    if (success)
      kits++;
    else
      servings++;
  }

  cout << "Case #" << t << ": " << kits << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
