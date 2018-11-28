////////////////////////////////////////////////////////////////////
// This source code is for Visual Studio
////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <stack>
#include <functional>
#include <iomanip>
#include <string>
#include <cstring>
#include <deque>
#include <math.h>

#define	numberof(a)	(sizeof(a) / sizeof(a[0]))
#define	INF		UINT32_MAX
#define Rep(i,n) for(int i = 0; i < (n); ++i )

using namespace std;

typedef vector< vector<int> > MAT;
typedef pair<int, int> PINT;
typedef long long ll;
typedef uint32_t u32;
typedef uint64_t u64;
typedef int32_t s32;
typedef int64_t s64;

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

ll solve( string N )
{
	string ret_str = N;
	ll len = N.length();

	Rep(i, len - 1) {
		int curr_num = N[i] - '0';
		int next_num = N[i + 1] - '0';

		// judge not tidy
		if (next_num < curr_num) {
			char search_num = N[i];
			int start_index = 0;

			// search
			for (int j = i; j >= 0; --j) {
				if (N[j] != N[i]) {
					break;
				}
				// update
				start_index = j;
			}

			int target = N[start_index] - '0';
			ret_str[start_index] = (target - 1) + '0';
			for (int j = start_index + 1; j < len; ++j ) {
				ret_str[j] = '9';
			}
			break;
		}
	}

	return atoll(ret_str.c_str());
}

int main()
{
	int T = 0;
	string N = "";
	vector< ll > ans;

	cin >> T;

	for( int t = 0; t < T; ++t ){
		cin >> N;
		ans.push_back( solve(N) );
	}

	Rep(i, ans.size()){
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	}

	// stop
	cin >> T;

	return 0;
}



