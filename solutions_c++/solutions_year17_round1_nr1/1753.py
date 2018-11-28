#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <deque>

#include <cassert>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <functional>
#include <string>
#include <tuple>
#include <utility>

#include <iostream>
#include <sstream>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl

typedef long long tint;
typedef unsigned long long utint;


int main(){
  tint T; cin >> T;
  forn(CASE, T) {
    tint R, C; cin >> R >> C;
    vector<vector<char> > cake(R, vector<char>(C));
    int firstRow = R;
    forn(i,R) {
      forn(j,C) {
        cin >> cake[i][j];
        if (cake[i][j] != '?') {
          firstRow = min(firstRow, i);
        }
      }
    }
    ///
    forn(i,R) {
      char lastLet = '?';
      int lastCol = -1;
      forn(j,C) {
        if (cake[i][j] != '?') {
          lastLet = cake[i][j];
          forsn(k,lastCol+1,j) {
            cake[i][k] = lastLet;
          }
          lastCol = j;
        }
      }
      //debug(lastCol);
      forsn(j,lastCol+1,C) {
        cake[i][j] = lastLet;
      }
    }
    ///
    forn(i,firstRow) {
      forn(j,C) {
        cake[firstRow-i-1][j] = cake[firstRow-i][j];
      }
    }
    forsn(i,firstRow,R) {
      if (cake[i][0] == '?') {
        forn(j,C) {
          cake[i][j] = cake[firstRow][j];
        }
      } else { 
        firstRow = i; 
      }
    }
    ///
    cout << "Case #" << CASE+1 << ": \n";
    forn(i,R){
      forn(j,C) {
        cout << cake[i][j];
      }cout << endl;
    }
  }
	return 0;
}
