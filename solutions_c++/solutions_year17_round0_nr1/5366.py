#include <bits/stdc++.h>

using namespace std;

#define dbg(x) (cout<<#x<<" = "<<(x)<<'\n')

unordered_map<string, int> dist;

void revert(char& c) {
  c = (c == '+' ? '-' : '+');
}

int solve(string& pancakes, int& K) {
  int N = pancakes.size();
  int count = 0;

  for (int i = 0; i < N - K + 1; ++i) {
    if (pancakes[i] == '-') {
      ++count;
      for (int j = i; j < i + K; ++j) {
        revert(pancakes[j]);
      }
    }
  }

  for (auto c : pancakes) {
    if (c == '-') {
      return -1;
    }
  }

  return count;
}

int main() {
  cin.sync_with_stdio(false);

  int num_cases;
  cin >> num_cases;

  int K;
  string pancakes;
  for (int case_index = 1; case_index <= num_cases; ++case_index) {
    cin >> pancakes >> K;

    int sol = solve(pancakes, K);

    cout << "Case #" << case_index << ": ";

    if (sol == -1) {
      cout << "IMPOSSIBLE";
    } else {
      cout << sol;
    }

    cout << '\n';
  }


  return 0;
}
