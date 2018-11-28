#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <array>
#include <set>
#include <stack>
#include <map>

using namespace std;

template<typename T>
void print_answer(const T& answer) {
  static int case_idx = 1;
  stringstream ss;
  ss << "Case #" << case_idx << ": " << answer << endl;
  cout << ss.str();
  cerr << ss.str();
  ++case_idx;
}

double process_task() {
  int n, k;
  cin >> n >> k;
  double training;
  vector<double> units(n);
  cin >> training;
  for (int i = 0; i < n; ++i)
  {
    cin >> units[i];
  }

  sort(units.begin(), units.end());

  int last_idx = 1;

  const double epsilon = 0.0000000001;
  while (training > epsilon) {
    while (last_idx < n && units[0] == units[last_idx]) {
      ++last_idx;
    }

    double top = last_idx < n ? units[last_idx] : 1.0;
    double addition = min(top - units[0], training / last_idx);
    training -= addition * last_idx;

    for (int i = 0; i < last_idx; ++i) {
      units[i] += addition;
    }

    // cerr << "n = " << n << ", last_idx = " << last_idx << ", training = " << training <<endl;

  }

  double result = 1.0;
  for (int i = 0; i < n; ++i) {
    result *= units[i];
  }
  return result;
}

int main() {
    int task_count = 0;

    cin >> task_count;
    std::cerr << task_count << " <- task_count" << std::endl;

    for (int iter = 0; iter < task_count; ++iter) {
        auto result = process_task();
        print_answer(result);
    }

    return 0;
}