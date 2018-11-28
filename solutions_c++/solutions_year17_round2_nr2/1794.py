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

string solve(ll N, ll R, ll O, ll Y, ll G, ll B, ll V)
{
	string ret = "";
	ll three_pairNum = min( min(R, Y), B );
	ll two_pairNum = 0;
	ll remained_colorNum = 0;

	if (R == three_pairNum) {
		two_pairNum = min(Y - three_pairNum, B - three_pairNum);
	}
	else if (Y == three_pairNum) {
		two_pairNum = min(R - three_pairNum, B - three_pairNum);
	}
	else {
		two_pairNum = min(R - three_pairNum, Y - three_pairNum);
	}
	remained_colorNum = max( max(R - three_pairNum - two_pairNum, Y - three_pairNum - two_pairNum), B - three_pairNum - two_pairNum);

	// define color
	ll maxNum = max( max(R, Y), B);
	string maxColor = "";
	string secondMaxColor = "";
	string minColor = "";
	if ( R == maxNum) {
		maxColor = 'R';
		if (Y >= B) {
			secondMaxColor = 'Y';
			minColor = 'B';
		}
		else {
			secondMaxColor = 'B';
			minColor = 'Y';
		}
	}
	else if (Y == maxNum) {
		maxColor = 'Y';
		if (R >= B) {
			secondMaxColor = 'R';
			minColor = 'B';
		}
		else {
			secondMaxColor = 'B';
			minColor = 'R';
		}
	}
	else {
		maxColor = 'B';
		if (R >= Y) {
			secondMaxColor = 'R';
			minColor = 'Y';
		}
		else {
			secondMaxColor = 'Y';
			minColor = 'R';
		}
	}

	// check 
	if (three_pairNum < remained_colorNum) {
		return "IMPOSSIBLE";
	}

	// create string
	string remain = maxColor;
	string two_pair = secondMaxColor + maxColor;
	string trhee_pair = secondMaxColor + maxColor + minColor;

	Rep(i, three_pairNum) {
		ret += trhee_pair;
		if ( i <  remained_colorNum ) {
			ret += remain;
		}
	}
	Rep(i, two_pairNum) {
		ret += two_pair;
	}

	return ret;
}

int main()
{
	int T = 0;
	ll N = 0;
	ll R, O, Y, G, B, V = 0;
	vector< string > ans;

	cin >> T;

	for( int t = 0; t < T; ++t ){
		cin >> N >> R >> O >> Y >> G >> B >> V;
		ans.push_back( solve(N, R, O, Y, G, B, V) );
	}

	Rep(i, ans.size()){
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	}

	// stop
	cin >> T;

	return 0;
}



