#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <array>
#include <set>
#include <stack>

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

inline int dist(int start, int finish) {
  int diff = (finish - start + 1440) % 1440;
  if (diff == 0)
    diff = 1440;
  return diff;  
}

int process_task() {
  int l, r;
  cin >> l >> r;
  if (max(l, r) <= 1) {
    for (int i = 0; i < (l + r) * 2; ++i) {
      int a;
      cin >> a;
    }
    return 2;
  } else {
    int shift_count = max(l, r);
    vector<pair<int, int>> shifts(shift_count);
    for (int i = 0; i < shift_count; ++i) {
      cin >> shifts[i].first >> shifts[i].second;
    }

    if (shifts.size() == 1) {
      return 2;
    }
    if (dist(shifts[0].first, shifts[1].second) <= 720 || 
          dist(shifts[1].first, shifts[0].second) <= 720) {
      return 2;
    }
    return 4;
  }
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