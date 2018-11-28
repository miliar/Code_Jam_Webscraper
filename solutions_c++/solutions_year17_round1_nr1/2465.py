#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void expand(vector<string> &cake, char initial, int i, int j) {
  // Expand horizontally
  int x = j - 1;
  while(x >= 0 && cake[i][x] == '?') {
      cake[i][x] = initial;
      --x;
  }
  int left = x + 1;

  x = j + 1;
  while(x < cake[i].length() && cake[i][x] == '?') {
      cake[i][x] = initial;
      ++x;
  }
  int right = x;

  // Expand vertically
  x = i - 1;
  while(x >= 0 && all_of(cake[x].begin() + left,
                         cake[x].begin() + right,
                         [] (char initial_at) { return initial_at == '?'; })) {
    for (int y = left; y < right; ++y) {
      cake[x][y] = initial;
    }
    --x;
  }
  x = i + 1;
  while(x < cake.size() && all_of(cake[x].begin() + left,
                                  cake[x].begin() + right,
                         [] (char initial_at) { return initial_at == '?'; })) {
    for (int y = left; y < right; ++y) {
      cake[x][y] = initial;
    }
    ++x;
  }
}

void decorate(vector<string> &cake) {
  vector<bool> expanded(26, false);
  for (int i = 0; i < cake.size(); ++i) {
    for (int j = 0; j < cake[i].length(); ++j) {
      char initial = cake[i][j];
      int expanded_ind = initial - 'A';
      if (initial != '?' && !expanded[expanded_ind]) {
        expand(cake, initial, i, j);
        expanded[expanded_ind] = true;
      }
    }
  }
}

int main(int argc, char **argv) {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int r, c;
    cin >> r >> c;
    vector<string> cake(r);
    for (int i = 0; i < r; ++i) {
        cin >> cake[i];
    }
    cout << "Case #" << i + 1 << ": "<< endl;
    decorate(cake);
    for (const auto &row : cake) {
      cout << row << endl;
    }
  }
  return 0;
}