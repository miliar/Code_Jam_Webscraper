
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

void change(string &s, int start, int k) {
	for (int i = 0; i < k; ++i)
	{
		s[ i + start ] = ((s[ i + start ] == '+')?'-':'+');
	}
}

int main(int argc, char const *argv[])
{
    int tc, test = 1;
    int  k;

    cin >> tc;
    while (tc--) {
    	string s;
    	cin >> s >> k;

    	// printf("%s===%d\n",s.c_str(), k );

    	int ans = 0;
    	int n = s.size();
    	for (int i = 0; i < n; i++)
    	{
			// printf("%c", s[n-1-i]);
			// continue;

    		if (s[i] != '+') {
    			if (i + k - 1 <  n){
    				change(s, i, k);
    				ans++;
    			}
    			// printf("L  => %d  => %s\n", i, s.c_str());
    		}

    		// printf("=======> %d %d\n",i, n-i );
    		int pos = n-i-1;
    		if (s[ pos ] != '+') {
    			if (pos - k + 1 >= 0){
    				change(s, pos - k + 1, k);
    				// printf("R  => %d  i:%d => %s\n", i - k + 1, i, s.c_str());
    				ans++;
    			}
    		}
    		// printf("=====> %d  %d  %c\n", i, n, s[n-i]);
    	}

    	for (int i = 0; i < n; ++i)
    	{
    		if (s[i] == '-'){
    			ans = -1;
    			break;
    		}
    	}

    	printf("Case #%d: ", test++);
    	if (ans >= 0){
    		printf("%d\n", ans);
    	} else {
    		printf("IMPOSSIBLE\n");
    	}
    }
    return 0;
}
