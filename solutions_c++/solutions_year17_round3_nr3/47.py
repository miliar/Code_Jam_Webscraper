#include <bits/stdc++.h>

using namespace std;

const int N = 51;
const double EPS = 1e-9;

int n;
int k;
double u;
double p[N];

double SolveSimpleCase() {
  while (true) {
    vector<int> min_positions;
    double min_value = 1.0;
    double second_min_value = 1.0;

    for (int i = 0; i < n; ++i) {
      if (p[i] > second_min_value - EPS) {
        continue;
      }

      if (p[i] > min_value + EPS) {
        second_min_value = p[i];
        continue;
      }

      if (p[i] > min_value - EPS) {
        min_positions.push_back(i);
        continue;
      }

      second_min_value = min_value;
      min_value = p[i];
      min_positions = {i};
    }

    double delta = min(u / min_positions.size(), second_min_value - min_value);
    if (min_positions.size() == 0 || delta < EPS) {
      break;
    }

    for (int i : min_positions) {
      p[i] += delta;
      u -= delta;
    }
  }

  double result = 1.0;
  for (int i = 0; i < n; ++i) {
    result *= p[i];
  }

  return result;
}

void SolveSingleCase(int case_id) {
  cin >> n >> k;
  cin >> u;
  for (int i = 0; i < n; ++i) {
    cin >> p[i];
  }

  double answer;
  if (n == k) {
    answer = SolveSimpleCase();
  } else {
    answer = -1.0;
  }

  cout << "Case #" << case_id << ": " << answer << "\n";
}

int main() {
  cout << fixed << setprecision(12);
  cerr << fixed << setprecision(12);
  int cases_num; cin >> cases_num;

  for (int i = 0; i < cases_num; ++i) {
    SolveSingleCase(i + 1);
  }

  return 0;
}
