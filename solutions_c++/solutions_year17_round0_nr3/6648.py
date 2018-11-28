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

pair<ll, ll> solve( ll N, ll K )
{
	pair<ll, ll> ret = make_pair(0, 0);// (max, min)
	string curr_bathroom = "";

	// initialize
	curr_bathroom.push_back('0');
	Rep(i, N) {
		curr_bathroom.push_back('.');
	}
	curr_bathroom.push_back('0');

	// calc each person
	Rep(i, K) {
		ll decide_bathroomNum = -1;
		ll decide_bathroomNum_first = -1;
		vector< pair<ll, ll> > saved_minmax(N + 2);// min, max

//		if (i == K - 1) {
//			printf("Last person \n");
//		}

		Rep(j, N + 2) {
			if (curr_bathroom[j] == '.') {
				// empty j-th bathroom
				if(decide_bathroomNum_first == -1) decide_bathroomNum_first = j;

				// search left
				ll left = 0;
				for (ll m = j - 1; m >= 0; --m ) {
					if (curr_bathroom[m] == '.') {
						left++;
					}
					else if (curr_bathroom[m] == '0') {
						break;
					}
				}
				// search right
				ll right = 0;
				for (ll m = j + 1; m < N + 2; ++m) {
					if (curr_bathroom[m] == '.') {
						right++;
					}
					else if (curr_bathroom[m] == '0') {
						break;
					}
				}

				ll tmp_min = min(left, right);
				ll tmp_max = max(left, right);
				saved_minmax[j] = make_pair(tmp_min, tmp_max);
			}
			else {
				saved_minmax[j] = make_pair(-1, -1);
			}
		}

		// decide bathroom
		vector< pair<ll, ll> > sorted_minmax = saved_minmax;
		sort(sorted_minmax.begin(), sorted_minmax.end());

		Rep(j, N + 2) {
			if (sorted_minmax[N + 1].first == saved_minmax[j].first
			&&	sorted_minmax[N + 1].second == saved_minmax[j].second) {
				decide_bathroomNum = j;
			}
		}

		if (decide_bathroomNum == -1) {
			decide_bathroomNum = decide_bathroomNum_first;
		}

		// ret_val
		ret = make_pair(saved_minmax[decide_bathroomNum].second, saved_minmax[decide_bathroomNum].first);

		// decide which bathroom
		curr_bathroom[decide_bathroomNum] = '0';
	}

	return ret;
}

int main()
{
	int T = 0;
	ll N = 0;
	ll K = 0;
	vector< pair<ll, ll> > ans;

	cin >> T;

	for( int t = 0; t < T; ++t ){
		cin >> N >> K;
		ans.push_back( solve(N, K) );
	}

	Rep(i, ans.size()){
		cout << "Case #" << i + 1 << ": " << ans[i].first << " " << ans[i].second << endl;
	}

	// stop
	cin >> T;

	return 0;
}



