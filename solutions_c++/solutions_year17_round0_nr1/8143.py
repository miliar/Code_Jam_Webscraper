#include <iostream>
#include <utility>
#include <limits.h>
#include <fstream>
#include <string>
#include <string.h>
#include <queue>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <cmath>
#include <functional>

using namespace std;
int main()
{
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		char arr[1005];
		scanf("%s", arr);
		int s;
		int cnt = 0;
		scanf("%d", &s);
		int len = strlen(arr);
		for (int a = 0; a <= len - s; a++)
		{
			if (arr[a] == '-')
			{
				cnt++;
				for (int b = a; b<a + s; b++)
				{
					if (arr[b] == '-')
						arr[b] = '+';
					else if (arr[b] == '+')
						arr[b] = '-';
				}
			}
		}
		bool flag = false;
		for (int a = 0; a<len; a++)
		{
			if (arr[a] == '-')
				flag = true;
		}
		if (flag)
			printf("Case #%d: IMPOSSIBLE\n", i);
		else
			printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}