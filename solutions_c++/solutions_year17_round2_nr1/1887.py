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
		int d, n;
		scanf("%d %d", &d, &n);
		double t = 0.0;
		while(n--)
		{
			int k, s;
			scanf("%d %d", &k, &s);
			t = max(t, double(d-k) / double(s));
		}
		if(t > 0.0) printf("Case #%d: %.14lf\n", c, double(d) / t);
		else printf("Case #%d: 0\n", c);
		c++;
	}
    return 0;
}
