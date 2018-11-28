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
const int UNI_TYPES = 6;

struct Unicorn
{
	char color;
	int count;
}unicorns[UNI_TYPES];

bool operator<(const Unicorn& a, const Unicorn& b)
{
	if(a.count == b.count)
		return a.color < b.color;
		
	return a.count < b.count;
}

int T;
int n, r, o, y, g, b, v;

string unicornColors = "ROYGBV";

int main()
{	
	cin >> T;
	FOR(t, 1, T)
	{
		cin >> n;
		
		vector<Unicorn> unicorns;
		string stalls(n, 0);
		Unicorn temp;
		
		FORE(it, unicornColors)
		{
			temp.color = *it;
			cin >> temp.count;
			
			unicorns.push_back(temp);	
		}	
		sort(unicorns.begin(), unicorns.end());
		
		int idx = 0;
		bool possible = true;
		
		while(unicorns.rbegin()->count--)
		{
			if(idx >= n-1)
			{
				possible = false;
				break;
			}
			
			stalls[idx] = unicorns.rbegin()->color;
			
			idx += 2;	
		}
		unicorns.pop_back();
		
		if(!possible)
		{
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			
			continue;		
		}
		
		if(stalls[n-2] == 0)
			idx = n-2;
		else
			idx = n-1;
				
		while(unicorns.rbegin()->count--)
		{
			if(stalls[idx] != 0)
				idx--;

			if(idx < 0)
			{
				break;
			}
			
			stalls[idx] = unicorns.rbegin()->color;
			
			idx -= 2;	
		}
		unicorns.pop_back();
		
		while(!unicorns.empty())
		{
			for(int i = 0; i < n; ++i)
			{
				if(unicorns.rbegin()->count == 0)
				{
					break;
				}
				
				if(stalls[i] == 0)
				{
					stalls[i] = unicorns.rbegin()->color;
					unicorns.rbegin()->count--;	
				}	
			}
			
			unicorns.pop_back();	
		}	
		
		cout << "Case #" << t << ": " << stalls << endl;
	}
	return 0;
}

