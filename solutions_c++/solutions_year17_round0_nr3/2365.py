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

void update_map(map<long long, long long>& track, long long stalls, long long count) {
  if (stalls == 0) {
    return;
  }
  auto it = track.find(stalls);
  if (it != track.end()) {
    it->second += count;
  } else {
    track[stalls] = count;
  }
}

string get_answer(long long stalls) {
  auto rem = stalls - 1;
  auto left = rem / 2;
  auto right = rem - left;
  return to_string(right) + " " + to_string(left);
}

string process_task() {
  long long stalls, people;
  cin >> stalls >> people;
  map<long long, long long> track;

  long long actors = people - 1;
  track[stalls] = 1;
  while(actors > 0) {
    auto it = track.rbegin();
    if (actors < it->second) {
      break;
    }

    auto curr_stall = it->first;
    auto curr_people = it->second;
    track.erase(next(it).base());
    actors -= curr_people;
    auto rem = curr_stall - 1;
    auto left = rem / 2;
    auto right = rem - left;
    if (left == right) {
      update_map(track, left, curr_people * 2);
    }
    else {
      update_map(track, left, curr_people);
      update_map(track, right, curr_people);
    }

  }

  if (track.empty()) {
    throw 1;
  }
  return get_answer(track.rbegin()->first);
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