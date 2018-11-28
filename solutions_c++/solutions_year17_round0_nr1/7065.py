#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <stack>
#include <array>
#include <queue>
#include <fstream>
#include <functional>
#include <map>
#include <algorithm>
#include <unordered_set>
#include <ctime>
using namespace std;
int main()
{
	freopen("d:/codejam/A-large.in", "r", stdin);
	freopen("d:/codejam/ALarge.out", "w", stdout);
	int cas;
	cin >> cas;
	for (int i = 1; i <= cas;i++)
	{
		string str;
		int k;
		cin >> str >> k;
		int num_zero = 0;
		int num_one = 0;
		int n = str.size();
		int res = 0;
		int flag = 0;
		for (int ii = 0; ii < n;ii++)
		{
			if (str[ii] == '-')
			{
				if (ii + k > n)
				{
					flag = 1;
					printf("Case #%d: IMPOSSIBLE\n", i);
					break;
				}
				else
				{
					for (int j = ii; j < ii + k; j++)
					{
						if (str[j] == '-')str[j] = '+';
						else str[j] = '-';
					}
				}
				res++;
			}
		}
		if(!flag)
			printf("Case #%d: %d\n",i, res);
	}
}