#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	std::ios_base::sync_with_stdio(0);
	int ttt;
	scanf("%d\n",&ttt);
	for (int tt = 1; tt <= ttt; tt++)
	{
		char pkk[1010] = { 0 };
		int k, cnt = 0;
		scanf("%s %d", &pkk, &k);
		int l = strlen(pkk);
		bool f = 1;
		for (int i = 0; i <= l - k && f; i++)
		{
			if (pkk[i] == '-')
			{
				cnt++;
				for (int j = 0; j < k; j++)
					if (pkk[i + j] == '-')
						pkk[i + j] = '+';
					else
					{
						pkk[i + j] = '-';
						if (i == l - k)
						{
							f = 0;
							break;
						}
					}
			}
		}
		for (int i = l - k + 1; i < l && f; i++)
		{
			if (pkk[i] == '-')
			{
				f = 0;
				break;
			}
		}
		if(f)
			cout << "Case #" << tt << ": " << cnt << endl;
		else
			cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
	}
	return 0;
}