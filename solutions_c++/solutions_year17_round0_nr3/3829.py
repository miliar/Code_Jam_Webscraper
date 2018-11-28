#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<LD> VLD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000001;
const LD EPS = 10e-9;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define abs(a) ((a)<0 ? -(a) : (a))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

struct Interval
{
	int begin, end;
};

bool operator<(const Interval& a, const Interval& b)
{
	int aLen = a.end-a.begin;
	int bLen = b.end-b.begin;
	
	if(aLen == bLen)
		return a.begin > b.begin;
		
	return aLen < bLen;
}

int T, n, k;

int main()
{
	cin >> T;
	FOR(t, 1, T)
	{
		cin >> n >> k;
		
		int maxLR = 0, minLR = 0;
		priority_queue<Interval> intervals;
		intervals.push({1, n});
		
		REP(i, k)
		{
			Interval curr = intervals.top();
			intervals.pop();
			
			//cout << "curr.begin = " << curr.begin << ", curr.end = " << curr.end << endl;
			
			int toOccupy = (curr.end+curr.begin)/2;
			maxLR = curr.end-toOccupy;
			minLR = toOccupy-curr.begin;
			
			if(curr.begin+1 == curr.end)
			{
				intervals.push({curr.end, curr.end});
			}
			else if(curr.begin < curr.end)
			{
				intervals.push({curr.begin, toOccupy-1});
				intervals.push({toOccupy+1, curr.end});
			}
		}
		
		cout << "Case #" << t << ": " << maxLR << ' ' << minLR << endl;
	}
	return 0;
}

