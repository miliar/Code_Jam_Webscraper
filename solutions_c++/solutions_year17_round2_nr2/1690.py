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
bool pred(pair<int, char> a, pair<int, char> b)
{
	return a.first < b.first;
}
char ar[1010];
int main()
{
    //freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int c = 1;
	while(t--)
	{
		int n, r, o, y, g, b, v;
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		for(int i = 0; i < n; i++) ar[i] = 0;
		vector<pair<int, char> > v2;
		v2.push_back(make_pair(r, 'R'));
		v2.push_back(make_pair(y, 'Y'));
		v2.push_back(make_pair(b, 'B'));
		sort(v2.begin(), v2.end(), pred);
		char a3 = v2[0].second;
		int i3 = v2[0].first;
		char a2 = v2[1].second;
		int i2 = v2[1].first;
		char a1 = v2[2].second;
		int i1 = v2[2].first;
		if(i1 > n / 2 && n > 1)
		{
			printf("Case #%d: IMPOSSIBLE\n", c);
			c++;
			continue;
		}
		int j = 0;
		while(i1--)
		{
			ar[j] = a1;
			j += 2;
		}
		for(int i = 0; i < n; i++)
		{
			if(ar[i] == 0)
			{
				if(i2 > i3) 
				{
					ar[i] = a2;
					i2--;
				}
				else
				{
					ar[i] = a3;
					i3--;
				}
			}
		}
		bool b2 = true;
		for(int i = 1; i < n-1; i++)
		{
			if(ar[i] == ar[i-1] || ar[i] == ar[i+1])
			{
				b2 = false;
				break;
			}
		}
		if(ar[0] == ar[n-1]) b2 = false;
		if(!b2) printf("Case #%d: IMPOSSIBLE\n", c);
		else
		{
			printf("Case #%d: ", c);
			for(int i = 0; i < n; i++) printf("%c", ar[i]);
			printf("\n");
		}
		c++;
	}
    return 0;
}
