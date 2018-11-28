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

string process_task() {
  string input;
  cin >> input;
  string output(input.size(), '9');
  int breakpoint = -1;
  for (int i = 0; i < input.size(); ++i) {
  	if (i == (input.size() - 1) || input[i] <= input[i + 1]) {
      output[i] = input[i];
    }
    else {
      output[i] = input[i] - 1;
      if (i > 0 && output[i] < output[i - 1]) {
        breakpoint = i;
      }
      break;
    }
  }

  if (breakpoint >= 0) {
    for (int i = breakpoint; i > 0; --i) {
      if (output[i] < output[i - 1]) {
        output[i] = '9';
        --output[i - 1];
      }
      else {
        break;
      }
    }
  }

  if (output[0] == '0') {
    output = string(output.begin() + 1, output.end());
  }
  return output;
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