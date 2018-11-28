#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <tuple>

using namespace std;

vector<tuple<int, int>> fill_xs(set<int> rows, set<int> cols, int size) {
  if (cols.find(size - 1) != cols.end()) {
    vector<tuple<int, int>> rax;
    for (int i = 0; i < size-1; ++i) {
      rax.push_back(make_tuple(i, size - 1 - i));
    }
    return rax;
  }
  vector<tuple<int, int>> rax;
  for (int i = 0; i < size; ++i) {
    if (rows.find(i) != rows.end()) continue;
    for (int j = 0; j < size; ++j) {
      if (cols.find(j) == cols.end()) {
        rows.insert(i);
        cols.insert(j);
        rax.push_back(make_tuple(i, j));
        break;
      }
    }
    if (rows.find(i) != rows.end()) continue;
  }
  return rax;
}

int main(int argc, char* argv[]) {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int n, m;
    cin >> n >> m;
    set<int> rows;
    set<int> cols;
    set<int> crosses;
    int already_there = 0;
    for (int j = 0; j < m; ++j) {
      string type;
      int ri, ci;
      cin >> type >> ri >> ci;
      if (type == "o" || type == "x") {
        rows.insert(ri - 1);
        cols.insert(ci - 1);
      } 
      if (type == "+" || type == "o") {
        crosses.insert(ci - 1);
        already_there++;
      }
    }
    if (n == 1) {
      if (rows.size() == 1  && crosses.size() == 1) {
        cout << "Case #" << i + 1 << ": 2 0" << endl;
      } else cout << "Case #" << i + 1<< ": 2 1" << endl << "o 1 1" << endl;
      continue;
    }

    cout << "Case #" << i + 1<< ": " << 3 * n - 2 << " " << 3 * n - 3 - already_there << endl;
    auto rowcopy = rows;
    auto colscopy = cols;
    vector<tuple<int, int>> xs = fill_xs(rowcopy, colscopy, n);
    for (int j = 0; j < n; ++j) {
      if (crosses.find(j) == crosses.end()) {
        bool found = false;
        for (auto x : xs) {
          if (get<0>(x) == 0 && j == get<1>(x)) found = true;
        }
        if (cols.find(j) != cols.end()) found = true;
        if (found) {
          cout << "o 1 " << j + 1 << endl;
        } else cout << "+ 1 " << j + 1 << endl;
      }
    }
    for (tuple<int, int> p : xs) {
      if (get<0>(p) != 0)
        cout << "x " << get<0>(p) + 1 << " " << get<1>(p) + 1 << endl;
    }
    for (int j = 1; j < n - 1; ++j) {
      cout << "+ " << n << " " << j + 1 << endl;
    }
  }
}
