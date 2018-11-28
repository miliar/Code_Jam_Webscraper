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
double ar[1010][1010][2];
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
		vector<pair<int, int> > v(n);
		for(int i = 0; i < n; i++) scanf("%d %d", &v[i].first, &v[i].second);
		sort(v.begin(), v.end(), greater<pair<int, int> >());
		for(int i = 1; i <= n; i++)
		{
			double s = _pi * double(v[i-1].first) * double(v[i-1].first);
			double s2 = 2 * _pi * double(v[i-1].first) * double(v[i-1].second);
			for(int j = 1; j <= k && j <= i; j++)
			{
				ar[i][j][0] = ar[i-1][j][0];
				ar[i][j][1] = ar[i-1][j][1];
				for(int l = i-1; l >= 0; l--)
				{
					double c = ar[l][j-1][0];
					if(c == 0.0) c = s;
					if(ar[i][j][0] + ar[i][j][1] < c + ar[l][j-1][1] + s2)
					{
						ar[i][j][0] = c;
						ar[i][j][1] = ar[l][j-1][1] + s2;
					}
				}
			}
		}
		printf("Case #%d: %.14lf\n", c, ar[n][k][0] + ar[n][k][1]);
		c++;
	}
    return 0;
}

