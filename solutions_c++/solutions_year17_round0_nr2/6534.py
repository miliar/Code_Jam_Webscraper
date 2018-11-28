/**********************************************
            Author : smiley007  
***********************************************/

//Data Structure Includes
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <stack>
#include <list>
#include <set>          
#include <map>
#include <unordered_set>

//Other Includes
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cctype>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <climits>
#include <iomanip>

using namespace std ;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<vvll> vvvll;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef vector<vpii> vvpii;
typedef vector<pll> vpll;
typedef vector<vpll> vvpll;
typedef vector<vvpll> vvvpll;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;

#ifdef LocalHost
    #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#endif

//Code Begins Here ------ >>>
int t, tt = 1;
ll n;

ll solve() {
	ll tmp = n;
	vi was;
	while (tmp > 0) {
		was.push_back(tmp % 10);
		tmp /= 10;
	}
	reverse(was.begin(), was.end());
	int sz = (int)was.size();
	while (true) {
		bool ok = true;
		for (int i = 0; i + 1 < sz; i++) {
			if (was[i] > was[i + 1]) {
				ok = false;
				was[i]--;
				for (int j = i + 1; j < sz; j++)
					was[j] = 9;

			}
		}
		if (ok)	break;
	}
	int idx = 0;
	for (int i = 0; i < sz; i++) if (was[i] != 0) {
		idx = i;
		break;
	} 
	ll res = 0;
	for (int i = idx; i < sz; i++) {
		res = 10 * res + was[i];
	}
	return res;
}

int main(){
    #ifdef LocalHost
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    
    scanf("%d", &t);
    while (tt <= t) {
        scanf("%lld", &n);
        cout << "Case #" << tt << ": " << solve() << "\n";
        tt++;
    }





    

    return 0;
}