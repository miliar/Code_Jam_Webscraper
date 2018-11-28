#include <algorithm>
#include <bitset>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

struct ColChar {
  int col;
  char ch;
};

int findFirstRow(const std::vector<std::string> &grid, const int &startRow) {
  // std::cout << "findfirstRow for " << startRow << std::endl;
  int ROWS = grid.size();
  int COLS = grid[0].length();
  // std::cout << ROWS << ' ' << COLS << std::endl;
  for (int r=startRow;r<ROWS;++r) {
    // std::cout << "r " << r << std::endl;
    bool allQuestions = true;
    for (int c=0;c<COLS;++c) {
      if (grid[r][c] != '?') {
        allQuestions = false;
        break;
      }
    }
    if (!allQuestions) {
      return r;
    }
  }
  return -1;
}

std::string getString(const std::string &gridRow) {
  // std::cout << "getString for " << gridRow << std::endl;
  int L = gridRow.length();
  std::vector<ColChar> v;
  for (int i=0;i<L;++i) {
    if (gridRow[i] != '?') {
      char c = gridRow[i];
      ColChar colChar {i, c};
      v.push_back(colChar);
    }
  }

  std::stringstream ss {};
  int prev = 0;
  for (const ColChar &cc : v) {
    for (int i=prev;i<=cc.col;++i) {
      ss << cc.ch;
    }
    prev = cc.col+1;
  }
  ColChar cc2 = v.back();
  for (int i=cc2.col+1;i<L;++i) {
    ss << cc2.ch;
  }
  // std::cout << ss.str() << std::endl;
  return ss.str();
}

std::vector<std::string> computeResult(const std::vector<std::string> &grid) {
  int ROWS = grid.size();
  std::vector<std::string> result {};
  int startRow = 0;
  while (true) {
    int firstRow = findFirstRow(grid, startRow);
    if (firstRow != -1) {
      std::string fillstring = getString(grid[firstRow]);
      for (int i=0;i<=firstRow-startRow;++i) {
        result.push_back(fillstring);
      }
      startRow = firstRow + 1;
    } else {
      std::string fillstring = result.back();
      // fill in rows from [startrow to rows-1] inclusive with fillstring (or just last row)
      for (int i=startRow;i<ROWS;++i) {
        result.push_back(fillstring);
      }
      return result;
    }
  }
}

int main() {
  std::ifstream fin {"A-large.in"};
  std::ofstream fout {"A-large.out"};

  // there will be some amount of blank space on top
  // then the left most in the first row, you should just go up to the first element.
  // if there's something in the same row, then go right til it gets there, otherwise go all the way down
  int T;
  fin >> T;

  for (int i=1;i<=T;++i) {
    int rows, columns;
    fin >> rows >> columns;
    std::vector<std::string> v {};
    std::string s;
    for (int row=0;row<rows;++row) {
      fin >> s;
      v.push_back(s);
    }

    std::vector<std::string> result = computeResult(v);
    fout << "Case #" << i << ':' << std::endl;
    for (const std::string &s : result) {
      fout << s << std::endl;
    }
  }
  return 0;
}
