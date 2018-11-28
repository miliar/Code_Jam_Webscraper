
/** Libr@ries **/
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>

/** System_Win_32 **/
#if ( WIN32 || __WIN32_ )
#define lld I64d
#endif
/** System **/
#define _ ios_base::sync_with_stdio(0);cin.tie(0);


/** Utilities **/
#define forit(i,v  )  for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define fori( i,a,b)  for (int i = (int)(a); i < (int)(b); i++)
#define forn( i, n )  fori( i, 0, n )
#define zeros( a )    memset(a, 0,sizeof(a))
#define null( a )     memset(a,-1,sizeof(a))
#define all( a )      (a).begin() , (a).end()
#define sqr( a )      ( (a)*(a) )
#define sz( a )       (a).size()
#define pb            push_back
#define mp            make_pair
#define F             first
#define S             second
#define PI            2*acos(0.0)
#define oo            0x7FFFFFFF
using namespace std;
typedef long long LL;


int op[ 10 ];
vector< LL > v;
void f(int id, int rem) {
	// printf("%d - %d\n", id, rem);
	if (id == 10 && rem == 0) {
		string ret = "";
		for (int i=0; i <= 10; i++){
			for (int j = 0; j < op[ i ]; ++j)
			{
				ret += '0' + i;
			}
		}

		LL val;
		sscanf(ret.c_str(), "%lld", &val);
		v.push_back(val);
		return;
	}
	if (id == 10) {
		return;
	}

	for (int i = 0; i <= rem; ++i)
	{
		op[id] = i;
		f(id+1, rem - i);
		op[id] = 0;
	}
}

int main(int argc, char const *argv[])
{

    for (int i = 1; i <= 18; ++i) {
    	f(1, i);
    }
    sort(v.begin(), v.end());


    int tc, t = 1;
    scanf("%d", &tc);

    while (tc--){
	    LL n = 132;
	    scanf("%lld", &n);
	    int pos = lower_bound(v.begin(), v.end(), n) - v.begin();

	    if (v[pos] > n){
	    	pos = (pos >0)?pos-1:pos;
	    }

	    printf("Case #%d: %lld\n", t++, v[pos]);
    }
    return 0;
}
