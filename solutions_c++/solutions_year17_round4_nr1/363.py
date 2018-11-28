#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

const int N_MAX = 200;
const int P_MAX = 10;
int N, P;
int groups[N_MAX];
int num_groups[P_MAX];

void init() {
  cin >> N >> P;
  for (int i = 0; i < P; i++)
    num_groups[i] = 0;

  for (int i = 0; i < N; i++) {
    cin >> groups[i];
    num_groups[groups[i] % P]++;
  }
}

int solve2() {
  return num_groups[0] + ((num_groups[1] + 1) / 2);
}

int solve3() {
  int n1 = num_groups[1], n2 = num_groups[2];
  int a = max(n1, n2);
  int b = min(n1, n2);
  return num_groups[0] + b + (a - b + 2) / 3;
}

int solve4() {
  int answer = 0;
  int n1 = num_groups[1], n2 = num_groups[2], n3 = num_groups[3];
  answer += num_groups[0] + n2 / 2;
  n2 %= 2;

  int a = max(n1, n3);
  int b = min(n1, n3);
  answer += b;
  a -= b;

  if (a >= 2 && n2 > 0) {
    n2--;
    a -= 2;
    answer++;
  }

  int leftover = a + n2;
  answer += (leftover + 3) / 4;
  return answer;
}

void solve_case(int t) {
  init();

  int answer;
  if (P == 2) {
    answer = solve2();
  } else if (P == 3) {
    answer = solve3();
  } else if (P == 4) {
    answer = solve4();
  } else {
    assert(false);
  }

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
