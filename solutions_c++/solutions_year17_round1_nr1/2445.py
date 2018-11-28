#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstring>



//#define INCLUDE_LP

#ifdef INCLUDE_LP
  #include "lp_lib.h"
#else
  #if defined (__GNUC__) && (__GNUC__ <= 2)
  #include <hash_map>
  #include <hash_set>
  #else
  #include <ext/hash_map>
  #include <ext/hash_set>
  using namespace __gnu_cxx;
  #endif
#endif



using namespace std;

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
//#include <boost/regex.hpp>



#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1e17



void print(int R, int C, char m[][30]) {
  int i, j;
  for (i=0; i<R; i++) {
    for (j=0; j<C; j++) {
      cout << m[i][j];
    }
    cout << endl;
  }
}

void copyRow(int fromRow, int toRow, int C, char m[][30]) {
  int i;
  for (i=0; i<C; i++) {
    m[toRow][i] = m[fromRow][i];
  }
}

int main()
{
  int i,j,k,l,m,n;
  int testId, nTests;

  cin >> nTests;
  for(testId=1;testId<=nTests;testId++)
  {
    int num;
    int R, C;
    char m[30][30];

    //XXX  -- Read input --  XXX
    cin >> R >> C;
    for (i=0; i<R; i++) {
      for (j=0; j<C; j++) {
        cin >> m[i][j];
      }
    }

    //TODO cout << "input is:" << endl;
    //TODO print(R,C,m);


    //XXX  -- Process input --  XXX
    for (i=0; i<R; i++) {
      bool prevFound = false;
      char prevChar = ' ';
      for (j=0; j<C; j++) {
        if (m[i][j] != '?') {
          prevFound = true;
          prevChar = m[i][j];
        } else {
          if (prevFound) {
            m[i][j] = prevChar;
          }
        }
      }

      prevFound = false;
      for (j = C-1; j >= 0; j--) {
        if (m[i][j] != '?') {
          prevFound = true;
          prevChar = m[i][j];
        } else {
          if (prevFound) {
            m[i][j] = prevChar;
          }
        }
      }

      //cout << "after iter :" << i << endl;
      //print(R,C,m);
    }

    //TODO cout << "after horizontal:" << endl;
    //TODO print(R,C,m);

    //TODO cout << "do vertical now " << endl;
    bool prevFound = false;
    int prevRow = -1;
    for (i = 0; i < R; i++) {
      if (m[i][0] != '?') {
        prevFound = true;
        prevRow = i;
      } else if (prevFound) {
        copyRow(prevRow, i, C, m);
      }
    }

    //TODO cout << "after vertical1 :" << i << endl;
    //TODO print(R,C,m);

    prevFound = false;
    prevRow = -1;
    for (i = R-1; i >= 0; i--) {
      if (m[i][0] != '?') {
        prevFound = true;
        prevRow = i;
      } else if (prevFound) {
        copyRow(prevRow, i, C, m);
      }
    }
    //XXX  -- Print output --  XXX
    printf("Case #%d: \n",testId);
    print(R,C,m);
  }

  return 0;
}
