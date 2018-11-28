#include <iostream>
#include <vector>
#include <tuple>

using namespace std;


void print_vec(vector<tuple<int, int, char>> v) {
  int end = get<1>(v[0]);
  int j = 0;
  for (int i = 0; i < v.size();) {
    cout << get<2>(v[i]);
    if (j == end) {
      ++i;
      if (i < v.size()) {
        end = get<1>(v[i]);
      }
    }
    ++j;
  }
  cout << endl;
}


int main() {
  int t, R, C;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> R >> C;
    cout << "Case #" << i << ": " << endl;
    
    vector<tuple<int, int, char> > c_ranges;
    vector<vector<tuple<int, int, char> > > r_ranges;

    for (int r = 0; r < R; ++r) {
      c_ranges.clear();
      char ch = ' ';
      char ch_old = ' ';
      int ch_old_index = 0;
      for (int c = 0; c < C; ++c) {
        cin >> ch;
        if (ch != '?') {
          if (ch_old != ' ') {
            c_ranges.push_back(make_tuple(ch_old_index, c - 1, ch_old));
            ch_old_index = c;
          }
          ch_old = ch;
        }
      }
      if (ch_old != ' ') {
        c_ranges.push_back(make_tuple(ch_old_index, C - 1, ch_old));
      }
      r_ranges.push_back(c_ranges);
    }

    vector<tuple<int, int, char> > selected_row;
    int j = 0; 
    while (r_ranges[j].size() == 0) {
      ++j;
    }
    selected_row = r_ranges[j];
    for (int k = 0; k < j; ++k) {
      r_ranges[k] = selected_row;
    }
    
    for (; j < R; ++j) {
      if (r_ranges[j].size() == 0) {
        r_ranges[j] = selected_row;
      } else {
        selected_row = r_ranges[j];
      }
    }

    for (int k = 0; k < R; ++k) {
      print_vec(r_ranges[k]);
    }
  }

  return 0;
}
