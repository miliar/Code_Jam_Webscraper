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
        char num[30];
        cin >> num;
        //int len=strlen(num);

        //XXX  -- Process input --  XXX
        //cout << "input" << num << endl;
        int prev_ptr = -1;
        int prev_val = 0;
        bool fix_it=false;
        int i = 0;
        for (; num[i]!='\0'; i++) {
          int val = num[i]-'0';
          if (val > prev_val) {
            prev_val=val;
            prev_ptr=i;

          } else if (val == prev_val) {
            // nothing
          } else {  // val < prev_val
            fix_it=true;
            break;
          }
        }

        assert(prev_ptr>=0 && prev_ptr<i);
        assert(num[prev_ptr] > '0');

        if (fix_it) {
          num[prev_ptr]--;
          for(int j=prev_ptr+1; num[j]!='\0'; j++) {
            num[j]='9';
          }
        }

        //XXX  -- Print output --  XXX
        cout << "Case #" << testId << ": ";
        for (i=0; num[i]!='\0'; i++) {
          if (num[i]!='0') break;
        }
        for (; num[i]!='\0'; i++) {
          cout << num[i];
        }
        cout << endl;
    }

    return 0;
}
