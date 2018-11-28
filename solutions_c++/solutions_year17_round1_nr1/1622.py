#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <math.h>

using namespace std;

string solve(int R, int C) {
  vector< vector<char> > cake;
  cake.resize(R);
  set<int> blank;
  for (int i = 0 ; i < R; ++i) {
      cake[i].resize(C);
      bool isBlank = true;
      for (int j = 0; j < C; ++j) {
          cin >> cake[i][j];
          if (cake[i][j] != '?') isBlank = false;
      }
      if (isBlank) blank.insert(i);
  }

  for (int i = 0; i < R; ++i) {
      if (blank.find(i) != blank.end() && i == 0) continue;
      vector<int> fill_in;
      char lastChar;
      for (int j = 0; j < C; ++j) {
          if (cake[i][j] == '?') {
              fill_in.push_back(j);
          } else {
              lastChar = cake[i][j];
              for (int k = 0; k < fill_in.size(); ++k) {
                  cake[i][fill_in[k]] = lastChar;
              }
              fill_in.clear();
          }
      }
      if (!fill_in.empty()) {
          for (int k = 0; k < fill_in.size(); ++k) {
            cake[i][fill_in[k]] = lastChar;
          }
      }
  }

    vector<int> row_fill;
    vector<char> last_row;
  for (int i = 0; i < R; ++i) {
      if (blank.find(i) != blank.end()) {
          row_fill.push_back(i);
      } else {
          last_row = cake[i];
          for (int j = 0; j < row_fill.size(); ++j) {
              for (int k = 0; k < C; ++k) {
                  cake[row_fill[j]][k] = cake[i][k];
              }
          }
          row_fill.clear();
      }
  }

  if (!row_fill.empty()) {
          for (int j = 0; j < row_fill.size(); ++j) {
              for (int k = 0; k < C; ++k) {
                  cake[row_fill[j]][k] = last_row[k];
              }
          }
}

stringstream ss;
ss << endl;
for (int i = 0; i < R; ++i) {
  for (int j = 0; j < C; ++j) {
      ss << cake[i][j];
  }
  ss << endl;
}
  return ss.str();
}

int main() {

    ofstream fout;
    fout.open("output.txt");

    if (fout.is_open()) {
        int R;
        int C;

        int num_tests = 0;
        cin >> num_tests;

        unsigned count = 1;
        while ( count <= num_tests ) {
            cin >> R >> C;
            fout << "Case #" << count << ": ";
            fout << solve(R, C); 
            count++;
        }
        fout.close();
    } else {
        cout << "Can't open file!";
    }
    return 0;
}