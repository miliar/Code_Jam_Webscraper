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
		int ac, aj;
		scanf("%d %d", &ac, &aj);
		vector<pair<int, int> > vac(ac), vaj(aj), v;
		for(int i = 0; i < ac; i++) scanf("%d %d", &vac[i].first, &vac[i].second);
		for(int i = 0; i < aj; i++) scanf("%d %d", &vaj[i].first, &vaj[i].second);
		sort(vac.begin(), vac.end());
		sort(vaj.begin(), vaj.end());
		if(ac + aj < 2 || (ac == 1 && aj == 1)) printf("Case #%d: 2\n", c);
		else
		{
			if(vac.size() > 0) v = vac;
			else v = vaj;
			if(v[1].first - v[0].second < 720 && v[0].first + 1440 - v[1].second < 720) printf("Case #%d: 4\n", c);
			else printf("Case #%d: 2\n", c);
		}
		c++;
	}
    return 0;
}

