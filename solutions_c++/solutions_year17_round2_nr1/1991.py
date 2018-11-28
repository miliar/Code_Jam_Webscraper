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

const bool compare( const pair<ll, ll> & p1, const pair<ll, ll> & p2)
{
	if ( p1.second == p2.second)
	{
		return p1.first < p2.first;
	}
	else{
		return p1.second < p2.second;
	}
}

double solve( ll D, ll N, vector<ll> & K, vector<ll> & S)
{
	double ret = 0.0;
	double max_h = 0.0;

	Rep(i, N) {
		double hour = (double)(D - K[i]) / S[i];
		max_h = max(max_h, hour);
	}

	ret = (double)D / max_h;

	return ret;
}

int main()
{
	int T = 0;
	ll N = 0;
	ll D = 0;
	vector< double > ans;

	cin >> T;

	for( int t = 0; t < T; ++t ){
		cin >> D >> N;

		vector< ll > K(N);
		vector< ll > S(N);
		Rep(j, N) {
			cin >>K[j] >> S[j];
		}

		ans.push_back( solve(D, N, K, S) );
	}

	Rep(i, ans.size()){
//		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
		printf("Case #%d: %.6f\n", i + 1, ans[i]);
	}

	// stop
	cin >> T;

	return 0;
}



