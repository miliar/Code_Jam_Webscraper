#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool is_happy_side_up(char c);
string solve(string s, int k);

string solve(string s, int k) {
  vector<bool> happy_side_up(s.length());
  transform(s.begin(), s.end(), happy_side_up.begin(),
            [](char c) { return c == '+'; });
  int flip_count = 0;
  for (int i = 0; i < happy_side_up.size() - k + 1; ++i) {
    if (!happy_side_up[i]) {
      for(int j = 0; j < k; ++j) {
        int flip_ind = i + j;
        happy_side_up[flip_ind] = !happy_side_up[flip_ind];
      }

      ++flip_count;
    }
  }
  return all_of(happy_side_up.begin(), happy_side_up.end(),
                [] (bool state) { return state; }) ? to_string(flip_count) : "IMPOSSIBLE";
}

int main(int argc, char **argv) {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    string s;
    int k;
    cin >> s >> k;
    cout << "Case #" << i + 1 << ": " << solve(s, k) << endl;
  }
  return 0;
}