#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstdlib>
#include <cstdio>

using namespace std;

char num[20];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%s", num);
		int len = strlen(num);
		for (int j = len - 1; j > 0; j--)
		{
			if (num[j - 1] > num[j])
			{
				num[j - 1]--;
				for (int k = j; k < len; k++)
					num[k] = '9';
			}
		}
		int off = 0;
		while (num[off] == '0')
			off++;
		printf("Case #%d: %s\n", i + 1, num + off);
	}
	return 0;
}