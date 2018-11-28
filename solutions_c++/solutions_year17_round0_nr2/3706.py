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

int T;
string n;

string removeZeros(const string& s)
{
	string res;
	
	int idx = 0;
	while(s[idx] == '0') idx++;
	
	return s.substr(idx);
}

int main()
{
	cin >> T;
	FOR(t, 1, T)
	{
		cin >> n;
		
		string res;
		res += n[n.size()-1];
		
		FORD(i, n.size()-2, 0)
		{
			if(n[i] <= res[0])
			{
				res = n[i] + res;
			}				
			else
			{
				int resSize = res.size();
				
				res = string(resSize, '9');
				res = char(n[i]-1) + res;		
			}
		}
		
		res = removeZeros(res);
		
		cout << "Case #" << t << ": " << res << endl;
		
	}
	return 0;
}

