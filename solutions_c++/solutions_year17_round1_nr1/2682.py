#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;

bool is_up(char c) { return c>='A' && c<='Z'; }

string grid[25];

inline bool good(int at, int l, int r) {
  for (int i = l; i <= r; ++i)
    if (grid[at][i] != '?')
      return false;
  return true;
}

void print_grid(int r, int c) {
  for (int i = 0; i < r; ++i)
    cout << grid[i] << endl;    
}

int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    int r, c;
    cin >> r >> c;
    getc(stdin);
    for (int i = 0; i < r; ++i)
      getline(cin, grid[i]);
    //    cout << "--" << endl;
    //    print_grid(r, c);
    //    cout << "--" << endl;

    for (char C = 'A'; C <= 'Z'; ++C) {
      bool found = false;
      for (int i = 0; i < r && !found; ++i)
	for (int j = 0; j < c && !found; ++j)
	  if (grid[i][j] == C) {
	    found = true;
	    int L = j-1, R = j+1;
	    while (L>=0 && grid[i][L]=='?')
	      --L;
	    ++L;
	    while (R<c && grid[i][R]=='?')
	      ++R;
	    --R;
	    int T = i-1, B = i+1;
	    while (T>=0 && good(T, L, R))
	      --T;
	    ++T;
	    while (B<r && good(B, L, R))
	      ++B;
	    --B;
	    for (int a = T; a <= B; ++a)
	      for (int b = L; b <= R; ++b)
		grid[a][b] = grid[i][j];
	    /*	    cout << "------" << endl;
	    print_grid(r, c);
	    cout << "------" << endl;*/
	  }
    }
    printf("Case #%d:\n", rr);
    print_grid(r, c);
  }
  return 0;
}
