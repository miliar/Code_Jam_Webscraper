#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <climits>
#include <cassert>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

ull T;

char peak_first_col(int row,vector< vector<char> > &cake) {
  for(auto &&c:cake[row]){
    if(c != '?')
      return c;
  }
  return '?';
}

char peak_first_row(int col,int rowlimit,vector< vector<char> > &cake) {
  for(int r=0;r<rowlimit;++r){
    if(cake[r][col]!='?')
      return cake[r][col];
  }
  return '?';
}


int main (int argc, char const *argv[])
{
  cin >> T;
  for (int t = 0; t < T; t++) {
    int r,c; cin >> r >> c;
    vector< vector<char> > cake;
    for (int i = 0; i < r; i++) {
      cake.push_back(vector<char>());
      for (int j = 0; j < c; j++) {
        char initial; cin >> initial;
        cake[i].push_back(initial);
      }
    }
    for (int i = 0; i < r; i++) {
      char last = peak_first_col(i, cake);
      if(last=='?') continue;
      for(int j = 0; j < c; j++) {
        if(cake[i][j]==last||cake[i][j]=='?') {
          cake[i][j]=last;
        } else {
          last=cake[i][j];
        }
      }
    }

    for (int j = 0; j < c; j++) {
      char last = peak_first_row(j, r, cake);
      assert(last!='?');
      for (int i = 0; i < r; i++) {
        if(cake[i][j]==last||cake[i][j]=='?') {
          cake[i][j]=last;
        } else {
          last=cake[i][j];
        }
      }
    }
    cout << "Case #" << t+1 << ":" << endl;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        cout << cake[i][j];
      }
      cout << endl;
    }

  }

  return 0;
}
