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
		long long n, k, cmin, cmax, tmp;
		cin >> n >> k;
		long long ms[200] = { 0 };
		long long cms[200] = { 0 };
		bool fl;
		ms[1] = n;
		cms[1] = 1;
		int i = 2, p = 1, l = 1;
		while (p != i)
		{
			if (ms[p] % 2)
			{
				tmp = ms[p] / 2ll;
				fl = 0;
				for (int j = p + 1; j < i; j++)
					if (ms[j] == tmp)
					{
						cms[j] += cms[p] * 2ll;
						fl = 1;
						break;
					}
				if (!fl)
				{
					ms[i] = tmp;
					cms[i] += cms[p] * 2ll;
					i++;
				}
			}
			else if (ms[p] != 0)
			{
				
				tmp = ms[p] / 2ll;
				fl = 0;
				for (int j = p + 1; j < i; j++)
					if (ms[j] == tmp)
					{
						cms[j] += cms[p];
						fl = 1;
						break;
					}
				if (!fl)
				{
					ms[i] = tmp;
					cms[i] += cms[p];
					i++;
				}
				
				tmp = ms[p] / 2ll  - 1ll;
				fl = 0;
				for (int j = p + 1; j < i; j++)
					if (ms[j] == tmp)
					{
						cms[i] += cms[p];
						fl = 1;
						break;
					}
				if (!fl)
				{
					ms[i] = tmp;
					cms[i] += cms[p];
					i++;
				}
			}
			p++;
			l++;
		}
		for (int i = 1; i < l; i++)
			for (int j = i+1; j < l; j++)
				if (ms[i] < ms[j])
				{
					tmp = ms[i];
					ms[i] = ms[j];
					ms[j] = tmp;
					tmp = cms[i];
					cms[i] = cms[j];
					cms[j] = tmp;
				}
		long long sm = 0;
		for (int i = 1; i < l; i++)
		{
			sm += cms[i];
			if (sm >= k)
			{
				p = i;
				break;
			}
		}
		if (ms[p] % 2)
			cmax = cmin = ms[p] / 2;
		else
		{
			cmax = ms[p] / 2;
			cmin = cmax - 1;
		}
		cout << "Case #" << tt << ": " << cmax <<' '<< cmin  << endl;
		
	}
	return 0;
}