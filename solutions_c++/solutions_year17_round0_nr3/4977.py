#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
#define ll long long int
using namespace std;
const double _pi = acos(-1.0);
class mycomp
{
public:
	bool operator() (const pair<int, int>& a, const pair<int, int>& b) const
	{
		int c = a.second - 1 - a.first;
		int d = b.second - 1 - b.first;
		int cmin, cmax, dmin, dmax;
		if(c % 2 == 0)
		{
			cmin = c / 2 - 1;
			cmax = c / 2;
		}
		else cmin = cmax = c / 2;
		if(d % 2 == 0)
		{
			dmin = d / 2 - 1;
			dmax = d / 2;
		}
		else dmin = dmax = d / 2;
		if(cmin == dmin)
		{
			if(cmax == dmax) return a.first > b.first;
			else return cmax < dmax;
		}
		return cmin < dmin;
	}
};
int main()
{
    //freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int c = 1;
	while(t--)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		priority_queue<pair<int, int>, vector<pair<int, int> >, mycomp> q;
		q.push(make_pair(1, n + 2));
		int cmin = -1, cmax = -1;
		for(int i = 0; i < k; i++)
		{
			pair<int, int> p = q.top();
			q.pop();
			int c = p.second - 1 - p.first;
			int m;
			if(c % 2 == 0)
			{
				m = c / 2;
				cmin = c / 2 - 1;
				cmax = c / 2;
			}
			else 
			{
				m = c / 2 + 1;
				cmin = cmax = c / 2;
			}
			if(m > 1) q.push(make_pair(p.first, p.first + m));
			if(p.first + m < p.second - 1) q.push(make_pair(p.first + m, p.second));
		}
		printf("Case #%d: %d %d\n", c, cmax, cmin);
		c++;
	}
    return 0;
}
