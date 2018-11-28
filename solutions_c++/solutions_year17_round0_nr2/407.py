#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

const int D_MAX = 30;
int D;
int digits[D_MAX];

void init() {
  D = 0;
  long long N;
  int tmp[D_MAX];
  cin >> N;
  while (N > 0) {
    tmp[D] = N % 10;
    N /= 10;
    D++;
  }
  for (int i = 0; i < D; i++)
    digits[i] = tmp[D - i - 1];
}


bool works(int x[]) {
  for (int i = 0; i < D - 1; i++)
    if (x[i] < x[i+1])
      return false;
  return true;
}

void solve_case(int t) {
  init();

  int run_start = 0;
  for (int i = 1; i < D; i++) {
    if (digits[i] == digits[run_start])
      continue;
    if (digits[i] > digits[run_start]) {
      run_start = i;
      continue;
    }
    digits[run_start]--;
    for (int j = run_start + 1; j < D; j++)
      digits[j] = 9;
    break;
  }

  cout << "Case #" << t << ": ";
  if (digits[0] > 0)
    cout << digits[0];
  for (int i = 1; i < D; i++)
    cout << digits[i];
  cout << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
