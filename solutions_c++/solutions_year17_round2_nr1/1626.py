#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

typedef vector<int> VI;

const int MAX_N = 1005;

void solve() {
  int K, D;
  cin >> D >> K;
  double t = 0;
  for (int i = 0; i < K; i++) {
    int k, s;
    cin >> k >> s;
    double t_ = ((double)(D - k)) / s;
    t = max(t, t_);
  }
  double res = D/t;
  printf("%lf", res);
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
