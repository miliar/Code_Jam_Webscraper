#include<iostream>
#include<string>
#include<vector>

using namespace std;

void printArray(vector<vector<char> > v, int r, int c) {
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      cout << v[i][j];
    }
    cout << endl;
  }
}

bool isQuestion(vector<vector<char> > v, int ii, int ji, int ie, int je) {
  for (int i = ii; i <= ie; i++) {
    for (int j = ji; j <= je; j++) {
      if (v[i][j] != '?') {
        return false;
      }
    }
  }
  return true;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int r;
    cin >> r;
    int c;
    cin >> c;
    vector<vector<char> > cake;
    for (int i = 0; i < r; i++) {
      string s;
      cin >> s;
      vector<char> line;
      for (int j = 0; j < c; j++) {
        line.push_back(s[j]);
      }
      cake.push_back(line);
    }
    vector<vector<char> > result;
    for (int i = 0; i < r; i++) {
      vector<char> line;
      for (int j = 0; j < c; j++) {
        line.push_back(cake[i][j]);
      }
      result.push_back(line);
    }
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (cake[i][j] != '?') {
          result[i][j] = '?';
          int jmin = j - 1;
          while (jmin >= 0 && isQuestion(result, i, jmin, i, j)) {
            jmin--;
          }
          jmin++;
          int imin = i - 1;
          while (imin >= 0 && isQuestion(result, imin, jmin, i, j)) {
            imin--;
          }
          imin++;
          int jmax = j + 1;
          while (jmax < c && isQuestion(result, imin, jmin, i, jmax)) {
            jmax++;
          }
          jmax--;
          int imax = i + 1;
          while (imax < r && isQuestion(result, imin, jmin, imax, jmax)) {
            imax++;
          }
          imax--;
          // cout << imin << " " << jmin << " " << imax << " " << jmax << " " << cake[i][j] << endl;
          for (int ii = imin; ii <= imax; ii++) {
            for (int jj = jmin; jj <= jmax; jj++) {
              result[ii][jj] = cake[i][j];
            }
          }
        }
      }
    }
    cout << "Case #" << t << ":" << endl;
    printArray(result, r, c);
  }
}
