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





int main()
{
  int i,j,k,l,m,n;
  int testId, nTests;

  cin >> nTests;
  for(testId=1;testId<=nTests;testId++)
  {
    double D;
    int N;
    cin >> D >> N;
    double max_time = 0;

    //XXX  -- Read input --  XXX
    //XXX  -- Process input --  XXX
    for(i=0; i<N; i++)
    {
      double K, S;
      cin >> K >> S;
      double time = (D-K)/S;
      if (time > max_time) {
        max_time=time;
      }
    }

    double ans = D/max_time;
    //XXX  -- Print output --  XXX
    printf("Case #%d: %lf\n", testId, ans);
  }

  return 0;
}
