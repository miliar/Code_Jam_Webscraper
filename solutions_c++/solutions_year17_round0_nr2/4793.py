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
char buf[110];
int main()
{
    //freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int c = 1;
	while(t--)
	{
		scanf("%s", buf);
		string s = buf;
		bool b = true;
		while(b)
		{
			b = false;
			for(int i = 0; i < s.size() - 1; i++)
			{
				if(s[i] > s[i+1])
				{
					s[i]--;
					for(int j = i + 1; j < s.size(); j++) s[j] = '9';
					b = true;
					break;
				}
			}
		}
		while(s.size() > 0 && s[0] == '0') s = s.substr(1);
		if(s.size() == 0) s = "0";
		printf("Case #%d: %s\n", c, s.c_str());
		c++;
	}
    return 0;
}
