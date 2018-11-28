#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
#include <iostream>
using namespace std;

fstream in, out;

int T;
int R, C;

vector<vector<char> > grid;
vector<vector<char> > ans;
vector<int> idx_rows;

bool is_empty(int row) {
  bool ret = true;
  for (int j = 0; j < C; ++j) {
    if (grid[row][j] != '?') {
      return false;
    }
  }
  return ret;
}

char get_char(int col_idx, int row_idx) {
  for (int j = col_idx; j < C; ++j) {
    if (grid[row_idx][j] != '?') {
      return grid[row_idx][j];
    }
  }
  for (int j = col_idx - 1; j >=0; --j) {
    if (grid[row_idx][j] != '?') {
      return grid[row_idx][j];
    }
  }
}

int main() {
  in.open("A-large.in", fstream::in);
  out.open("proba-large.out", fstream::out);

  in >> T;
  for (int i = 0; i < T; ++i) {
    in >> R >> C;
    //    cout << "Case " << i << " R, C= " << R << " " << C << endl;
    grid.clear();
    ans.clear();
    idx_rows.clear();
    
    for (int j = 0; j < R; ++j) {
      grid.push_back(vector<char>(C));
      ans.push_back(vector<char>(C));
      string input;
      in >> input;
      for (int k = 0; k < C; ++k) {
        grid[j][k] = input[k];
      }
    }

    for (int j = 0; j < R; ++j) {
      if (!is_empty(j)) {
        idx_rows.push_back(j);
      }
    }

    int curr_row = 0;
    int curr_idx = 0;
    while (curr_row < R) {
      //      cout << curr_row << " " << curr_idx << " " << idx_rows[curr_idx] << endl;
      for (int j = 0; j < C; ++j) {
        char next = get_char(j, idx_rows[curr_idx]);
        ans[curr_row][j] = next;
      }
      ++curr_row;
      if (curr_row > idx_rows[curr_idx] && curr_idx < idx_rows.size() - 1) {
        ++curr_idx;
      }
    }
    
    out << "Case #" << i + 1 << ": " << endl;
    for (int j = 0; j < R; ++j) {
      for (int k = 0; k < C; ++k) {
        out << ans[j][k];
      }
      out << endl;
    }
  }
    
  in.close();
  out.close();
  return 0;
}
