#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <climits>
#include <sstream>
#include <queue>
#include <unordered_map>

using ll = long long;
using namespace std;
const int kNInf = INT_MIN;

void register_size(priority_queue<ll> &section_sizes, unordered_map<ll, ll> &section_counter, ll size)
{
    if (section_counter.count(size) > 0) {
      ++section_counter[size];
    } else {
      section_counter[size] = 1;
      section_sizes.push(size);
    }
}

pair<ll, ll> solve_test(int stall_num, int person_num)
{
  priority_queue<ll> section_sizes;
  unordered_map<ll, ll> section_counter;

  section_sizes.push(stall_num);
  section_counter[stall_num] = 1;

  pair<ll, ll> res;
  for (ll i = 0; i < person_num; ++i) {
    auto largest_size = section_sizes.top();

    ll pos = (largest_size - 1) / 2LL;
    // unregister the split section
    if (section_counter[largest_size] == 1) {
      section_counter.erase(largest_size);
      section_sizes.pop();
    } else {
      --section_counter[largest_size];
    }

    // register the two new sections
    if (pos > 0) {
      register_size(section_sizes, section_counter, pos);
    }

    if (pos < largest_size - 1) {
      register_size(section_sizes, section_counter, largest_size - 1 - pos);
    }

    res.first = max(pos, largest_size - 1 - pos);
    res.second = min(pos, largest_size - 1 - pos);
  }
  return res;

}

pair<ll, ll> solve_test(string &line)
{
    istringstream ss(line);
    string val;

    getline(ss, val, ' ');
    int stall_num = stoi(val);
    getline(ss, val, ' ');
    int person_num = stoi(val);

    return solve_test(stall_num, person_num);
}

int main(int argc, char **argv)
{
  string line;
  ifstream in_file(argv[1]);

  getline(in_file, line);
  int test_num = stoi(line);

  for (int i = 0; i < test_num; ++i) {
    getline(in_file, line);
    auto res = solve_test(line);
    cout << "Case #" << i + 1 << ": " << res.first << " " << res.second << endl;
  }
}
