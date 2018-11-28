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
		double u;
		scanf("%lf", &u);
		int u2 = (u + 0.00001) * 10000;
		multiset<int> s;
		for(int i = 0; i < n; i++)
		{
			double d;
			scanf("%lf", &d);
			s.insert((d + 0.00001) * 10000);
		}
		while(u2--)
		{
			multiset<int>::iterator it = s.begin();
			int a = (*it);
			if(a >= 10000) break;
			a++;
			s.erase(it);
			s.insert(a);
		}
		multiset<int>::iterator it = s.begin();
		double res = 1.0;
		while(it != s.end())
		{
			res *= double((*it)) / 10000.0;
			++it;
		}
		printf("Case #%d: %.14lf\n", c, res);
		c++;
	}
    return 0;
}

