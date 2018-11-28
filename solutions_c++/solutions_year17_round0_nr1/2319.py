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

long long process_task() {
  string input;
  int flip;
  cin >> input >> flip;
  string pancakes(input.size(), '0');
  for (int i = 0; i < input.size(); ++i) {
  	pancakes[i] = input[i] == '+' ? 1 : 0;
  }

  int flip_count = 0;
  for (int i = 0; i < pancakes.size() - flip + 1; ++i) {
  	if (!pancakes[i]) {
  		++flip_count;
  		for (int j = i; j < i + flip; ++j) {
  			pancakes[j] ^= 1;
  		}
  	}
  }

  for (int i = pancakes.size() - flip + 1; i < pancakes.size(); ++i) {
  	if (!pancakes[i]) {
  		return -1;
  	}
  }
 
  return flip_count;
}


int main() {
    int task_count = 0;

    cin >> task_count;
    std::cerr << task_count << " <- task_count" << std::endl;

    for (int iter = 0; iter < task_count; ++iter) {
        long long result = process_task();
        print_answer(result >= 0 ? to_string(result) : "IMPOSSIBLE");
    }

    return 0;
}