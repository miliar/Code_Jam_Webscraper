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

ll gcd(ll a, ll b)
{
	// a >= b
	if (b > a) swap(a, b);
	if (b == 0) return a;
	return gcd(a % b, b);
}

ll lcm(ll a, ll b)
{
	return a * b / gcd(a, b);
}

const bool compare0( const pair<ll, ll> & p1, const pair<ll, ll> & p2)
{
	if ( p1.first == p2.first ) {
		return p1.second < p2.second;
	}
	else{
		return p1.first  < p2.first;
	}
}

const bool compare1(const pair<ll, ll> & p1, const pair<ll, ll> & p2)
{
	return (p1.first * p1.second) < (p2.first * p2.second);
}

const bool reverse_compare1(const pair<ll, ll> & p1, const pair<ll, ll> & p2)
{
	return (p1.first * p1.second) > (p2.first * p2.second);
}

double solve(ll N, ll K, vector< pair<ll, ll> > & rh)
{
	double ret = 0.0;
	double ret1 = 0.0, ret2 = 0.0;
	double max_tmp = 0.0;
	vector< pair<ll, ll> > cpy_rh = rh;

	Rep(i, N) {
		// decide MAX(R^2 * PI) + 2 PI * R
		double tmp = 2 * PI * rh[i].first * rh[i].second;
		tmp += rh[i].first * rh[i].first * PI;

		// remove
		vector< pair<ll, ll> >::iterator itr = (rh.begin() + i);
		itr = rh.erase(itr);

		// decide remain
		sort(rh.begin(), rh.end(), reverse_compare1);
		for (ll j = 0; j < K - 1; ++j) {
			tmp += 2 * PI * rh[j].first * rh[j].second;
		}
		ret = max(tmp, ret);

		// restore
		rh = cpy_rh;
	}

	return ret;
}

int main()
{
	int T = 0;
	ll N = 0;
	ll K = 0;
	vector< double > ans;

	cin >> T;
	for( int t = 0; t < T; ++t ){
		cin >> N >> K;
		vector< pair<ll, ll> > rh(N);	// R, H
		Rep(j, N) {
			cin >> rh[j].first >> rh[j].second;
		}
		ans.push_back( solve(N, K, rh) );
	}

	Rep(i, ans.size()){
//		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
		printf("Case #%d: %.9f\n", i + 1, ans[i]);
	}

	// stop
	cin >> T;

	return 0;
}



