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
char buf[1010];
int main()
{
    //freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int c = 1;
	while(t--)
	{
		int k;
		scanf("%s %d", buf, &k);
		string s = buf;
		vector<int> v(s.size(), 0);
		int res = 0;
		for(int i = 0; i < s.size(); i++)
		{
			if((v[i] % 2) != 0)
			{
				if(s[i] == '-') s[i] = '+';
				else s[i] = '-';
			}
			if(s[i] == '-')
			{
				if(i+k <= s.size())
				{
					for(int j = i + 1; j < i+k; j++) v[j]++;
					res++;
				}
				else
				{
					res = -1;
					break;
				}
			}
		}
		if(res == -1) printf("Case #%d: IMPOSSIBLE\n", c);
		else printf("Case #%d: %d\n", c, res);
		c++;
	}
    return 0;
}
