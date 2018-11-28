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

const int MAX_N = 1005;

struct Horse
{
	int k;
	double s;	
}horses[MAX_N];

bool operator<(const Horse& a, const Horse& b)
{
	if(a.k == b.k)
		return a.s < b.s;
		
	return a.k > b.k;
}

int T, d, n, k;
double s, minTime;

int main()
{
	cout.precision(6);
	
	cin >> T;
	FOR(t, 1, T)
	{
		minTime = 0;
		
		cin >> d >> n;
		
		REP(i, n)
		{
			cin >> horses[i].k >> horses[i].s;
		}		
		sort(horses, horses+n);
		
		REP(i, n)
		{
			double currentTime = (d - horses[i].k)/horses[i].s;
			minTime = max(currentTime, minTime);
		}
		
		cout << "Case #" << t << ": " << fixed << d/minTime << endl;		
	}
	return 0;
}

