#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
using namespace std;

template<class P0, class P1> ostream &operator<<(ostream &os, const pair<P0, P1> &p) { return os << "(" << p.first << "," << p.second << ")"; }
template<class T> void dump(const T &t) { cerr << "["; for (auto it = t.begin(); it != t.end(); ++it) cerr << " " << *it; cerr << " ]" << "\n"; } 

#if 0
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/cpp_dec_float.hpp>
using namespace boost::multiprecision;
#define Integer cpp_int
#define Rational cpp_rational
#define Float cpp_dec_float_50
#endif

string nice = ".+xo";

void trace(vector<string> &g) {
  int n = g.size();
  for (int i = 0; i < n; ++i) {
    string s = g[i];
    for (int j = 0; j < n; ++j)
      if (s[j] < 4)
	s[j] = nice[s[j]];
    cerr << s << "\n";
  }
}

int n;
vector<string> grid;
vector<string> allowed;

int scores[4] = { 0, 1, 1, 2 };
void updateAllowed(int i0, int j0) {
  int i, j, del;
  if (grid[i0][j0] & 2) {
    for (i = 0; i < n; ++i) if (i!=i0) allowed[i][j0] &= ~2;
    for (j = 0; j < n; ++j) if (j!=j0) allowed[i0][j] &= ~2;
  }
  if (grid[i0][j0] & 1) {
    for (del = 1; del <= n; ++del) {
      if (i0+del < n && j0+del < n) allowed[i0+del][j0+del] &= ~1;
      if (i0+del < n && j0-del >= 0) allowed[i0+del][j0-del] &= ~1;
      if (i0-del >= 0 && j0+del < n) allowed[i0-del][j0+del] &= ~1;
      if (i0-del >= 0 && j0-del >= 0) allowed[i0-del][j0-del] &= ~1;
    }
  }
}

int main(void) {
  int T; cin >> T;
  
  for (int iCase = 1; iCase <= T; ++iCase) {
    cout << "Case #" << iCase << ":";

    int m; cin >> n >> m;
    grid.clear();
    grid.resize(n, string(n, 0));
    while (--m >= 0) {
      string s;
      int i, j;
      cin >> s >> i >> j;
      for (int k = 0; k < 4; ++k)
	if (s[0]==nice[k])
	  grid[i-1][j-1] = k;
    }
    vector<string> grid0 = grid;
    
    if (n <= 6) {
      cerr << iCase << ":\n";
      trace(grid);
      cerr << "-----\n";
    }

    allowed.clear();
    allowed.resize(n, string(n, 3)); // 1 for +, 2 for x, 3 for both (i.e., an o)
    
    int i0, j0, i, j;
    for (i0 = 0; i0 < n; ++i0)
      for (j0 = 0; j0 < n; ++j0)
	updateAllowed(i0, j0);
    //=============================================================

    // Greedy x's

    for (i0 = 0; i0 < n; ++i0)
      for (j0 = 0; j0 < n; ++j0) {
	if (allowed[i0][j0] & 2) {
	  grid[i0][j0] |= 2;
	  updateAllowed(i0, j0);
	}
      }

#if 0
    // Not greedy +'s b/c diagonals not the same size---this should be ok for small version (optimal bishops)
    for (i0 = 0; i0 < n; ++i0) if (i0==0 || i0==n-1)
      for (j0 = 0; j0 < n; ++j0) {
	if (allowed[i0][j0] & 1) {
	  grid[i0][j0] |= 1;
	  updateAllowed(i0, j0);
	}
      }
#else
    // Just a stab: work greedily inward from boundary
    
    for (int del = 0; del <= n/2; ++del) {
      i0 = del;
      for (j0 = del; j0 < n-del; ++j0)
	if (allowed[i0][j0] & 1)
	  if (!(grid[i0][j0] & 1)) {
	    grid[i0][j0] |= 1;
	    updateAllowed(i0, j0);
	  }
      
      j0 = n-1 - del;
      for (i0 = del; ++i0 < n-del; )
	if (allowed[i0][j0] & 1) 
	  if (!(grid[i0][j0] & 1)) {
	    grid[i0][j0] |= 1;
	    updateAllowed(i0, j0);
	  }

      i0 = n-1 - del;
      for (j0 = n - del; --j0 >= del; )
	if (allowed[i0][j0] & 1)
	  if (!(grid[i0][j0] & 1)) {
	    grid[i0][j0] |= 1;
	    updateAllowed(i0, j0);
	  }
      
      j0 = del;
      for (i0 = n-del; --i0 >= del; )
	if (allowed[i0][j0] & 1)
	  if (!(grid[i0][j0] & 1)) {
	    grid[i0][j0] |= 1;
	    updateAllowed(i0, j0);
	  }
    }	
#endif



    //==============================================================
    int score = 0, chgCount = 0;
    for (i = 0; i < n; ++i)
      for (j = 0; j < n; ++j) {
	score += scores[grid[i][j]];
	if (grid[i][j]!=grid0[i][j]) ++chgCount;
      }
    cout << " " << score << " " << chgCount << "\n";

    for (i = 0; i < n; ++i)
      for (j = 0; j < n; ++j)
	if (grid[i][j]!=grid0[i][j]) 
	  cout << nice[grid[i][j]] << " " << i+1 << " " << j+1 << "\n";

    if (n <= 6) {
      trace(grid);
      cerr << "=====\n";
    }
  }

  return 0;
}
