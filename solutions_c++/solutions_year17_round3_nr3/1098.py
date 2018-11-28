#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <limits>
#include <queue>
#include <iomanip>

using namespace std;

int N, K;
double U;
vector<double> P;

double solve() {
  sort(P.begin(), P.end());

  double sum = 0;
  double total = 0;
  for (int i=0; i<N; i++) {
    sum += (1 - P[i]);
    total += P[i];
  }

  if (sum <= U) {
    return 1;
  }

  total += U;

  int avg_size = N;
  double avg = total / avg_size;

  for (int j=N-1; j>=0; j--) {
    if (P[j] >= avg) {
      // skip
      total -= P[j];
      avg_size--;
      avg = total / avg_size;
    } else {
      U -= avg - P[j];

      P[j] += avg - P[j];
    }
  }

  double res = 1;
  for (int j=0; j<N; j++) {
    res *= P[j];
  }
  return res;
}

int main() {
  int T;
  cin >> T;

  for (int i=0; i<T; i++) {
    cin >> N >> K;

    P = vector<double> (N);

    cin >> U;

    for (int j=0; j<N; j++) {
      cin >> P[j];
    }

    double result = solve();

    cout << std::fixed;

    cout << "Case #" << (i+1) << ": " << std::setprecision(6) << result << endl;
  }

  return 0;
}

