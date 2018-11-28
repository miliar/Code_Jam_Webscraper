#include <iostream>
#include <vector>
#include <string>
using namespace std ;
const int MAXN = 100 ;
vector<string> c ;
void recur(int r0, int c0, int r1, int c1) {
  int ra = -1, ca = -1 ;
  for (int i=r0; i<r1; i++) {
    for (int j=c0; j<c1; j++) {
      if (c[i][j] != '?') {
	if (ra < 0) {
	  ra = i ;
	  ca = j ;
	} else {
	  if (i != ra) {
	    recur(r0, c0, min(i, ra)+1, c1) ;
	    recur(min(i, ra)+1, c0, r1, c1) ;
	  } else {
	    recur(r0, c0, r1, min(j, ca)+1) ;
	    recur(r0, min(j, ca)+1, r1, c1) ;
	  }
	  return ;
	}
      }
    }
  }
  if (ra < 0) {
    cerr << "Oops" << endl ;
    return ;
  }
  char cc = c[ra][ca] ;
  for (int i=r0; i<r1; i++) {
    for (int j=c0; j<c1; j++) {
      c[i][j] = cc ;
    }
  }
}
int main() {
   int T, R, C ;
   string s ;
   cin >> T ;
   for (int kase=1; kase<=T; kase++) {
      cin >> R >> C ;
      c = vector<string>(R) ;
      for (int i=0; i<R; i++) {
	cin >> c[i] ;
      }
      recur(0, 0, R, C) ;
      cout << "Case #" << kase << ":" << endl ;
      for (int i=0; i<R; i++)
	cout << c[i] << endl ;
   }
}
