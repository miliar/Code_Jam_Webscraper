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

const LL INF = 1000000001*LL(1000000);
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

const int MAX_N = 105;

LL dist[MAX_N][MAX_N], d;
int T, n, q;
double minTime[MAX_N][MAX_N], minTimeOverall[MAX_N], e[MAX_N], s[MAX_N];

int main()
{
	cout.precision(6);
	
	cin >> T;
	FOR(t, 1, T)
	{
		REP(i, MAX_N)
		{
			REP(j, MAX_N)
			{
				dist[i][j] = INF;
				minTime[i][j] = INF;	
			}
			dist[i][i] = 0;
			minTimeOverall[i] = INF;
		}
		minTime[0][0] = 0;
		minTimeOverall[0] = 0;
		
		cin >> n >> q;
		REP(i, n)
		{
			cin >> e[i] >> s[i];
		}
		
		REP(i, n)
		{
			REP(j, n)
			{
				cin >> d;
				
				if(j == i+1)
				{
					dist[i][j] = d;	
				}	
			}
		}
		
		while(q--)
		{
			cin >> d >> d;
		}
		
		REP(i, n)
		{
			FOR(j, i+2, n-1)
			{
				dist[i][j] = dist[i][j-1] + dist[j-1][j];
			}
		}
		
		FOR(c, 1, n-1)
		{
			REP(h, c)
			{
				if(dist[h][c] > e[h])
				{
					continue;
				}
				
				minTime[c][h] = minTimeOverall[h] + dist[h][c]/s[h];
				
				minTimeOverall[c] = min(minTimeOverall[c], minTime[c][h]);				
			}
		}
		
		cout << "Case #" << t << ": " << fixed << minTimeOverall[n-1] << endl;
	}
	return 0;
}

