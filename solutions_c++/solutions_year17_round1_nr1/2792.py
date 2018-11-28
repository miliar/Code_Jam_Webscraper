#include <bits/stdc++.h>

using namespace std;

int main() {
  int t;
  cin >> t;

  for (int a = 0; a < t; a++) {
    int r, c;
    cin >> r >> c;
    char grid[r][c];
    vector< pair<int, int> > myVec;

    for (int i = 0; i < r; i++) {
      string ss;
      cin >> ss;
      for (int j = 0; j < c; j++) {
	grid[i][j] = ss[j];
	if (grid[i][j] != '?') {
	  myVec.push_back(make_pair(i,j));
	}
      }
    }

    int currentRow = 0, currentColumn = 0;
    for (int i = 0; i < myVec.size()-1; i++) {
      int rr, cc;
      rr = myVec[i].first;
      cc = myVec[i].second;

      char cur = grid[rr][cc];

      if (myVec[i+1].first == rr) {
	for (int j = currentRow; j <= rr; j++) {
	  for (int k = currentColumn; k <= cc; k++) {
	    grid[j][k] = cur;
	  }
	}
	currentColumn = cc + 1;
      }
      else {
	for (int j = currentRow; j <= rr; j++) {
	  for (int k = currentColumn; k < c; k++) {
	    grid[j][k] = cur;
	  }
	}
	currentRow = rr + 1;
	currentColumn = 0;
      }


    }
    
    int rr, cc;
    rr = myVec[myVec.size()-1].first;
    cc = myVec[myVec.size()-1].second;
    char cur = grid[rr][cc];
    for (int j = currentRow; j <= rr; j++) {
      for (int k = currentColumn; k < c; k++) {
	grid[j][k] = cur;
      }
    }
    currentRow = rr + 1;
    currentColumn = 0;
    if (rr != c) {
      for (int i = currentRow; i < r; i++) {
	for (int j = 0; j < c; j++) {
	  grid[i][j] = grid[i-1][j];
	}
      }
    }


    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
	if (grid[i][j] != '?'){
	  
	}
      }
    }
    
    cout << "Case #" << a+1 << ":" << endl;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
	cout << grid[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}
