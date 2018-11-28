#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

#define eps 1e-6


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	std::ios_base::sync_with_stdio(0);
	int ttt;
	scanf("%d\n",&ttt);
	for (int tt = 1; tt <= ttt; tt++)
	{
		int n, r, o, y, g, v, b;
		int m1, m2, m3;
		int k, l, t;
		char cm1, cm2, cm3;
		char sans[1010] = { 0 };
		bool fl = 1;

		cin >> n >> r >> o >> y >> g >> b >> v;

		if (r >= y)
		{
			if (y >= b)
			{
				m1 = r; m2 = y; m3 = b;
				cm1 = 'R'; cm2 = 'Y'; cm3 = 'B';
			}
			else
			{
				if(r >= b)
				{
					m1 = r; m2 = b; m3 = y;
					cm1 = 'R'; cm2 = 'B'; cm3 = 'Y';
				}
				else
				{
					m1 = b; m2 = r; m3 = y;
					cm1 = 'B'; cm2 = 'R'; cm3 = 'Y';
				}
			}
		}
		else
		{
			if (r >= b)
			{
				m1 = y; m2 = r; m3 = b;
				cm1 = 'Y'; cm2 = 'R'; cm3 = 'B';
			}
			else
			{
				if (y >= b)
				{
					m1 = y; m2 = b; m3 = r;
					cm1 = 'Y'; cm2 = 'B'; cm3 = 'R';
				}
				else
				{
					m1 = b; m2 = y; m3 = r;
					cm1 = 'B'; cm2 = 'Y'; cm3 = 'R';
				}
			}

		}

		if (m1 > m2 + m3)
			fl = 0;
		else if (m1 == m2 + m3)
		{
			for (int i = 0; i < 2*m2; i += 2)
			{
				sans[i] = cm1;
				sans[i + 1] = cm2;
			}
			for (int i = 2*m2; i < n; i += 2)
			{
				sans[i] = cm1;
				sans[i + 1] = cm3;
			}
		}
		else
		{
			k = m3 + m2 - m1;
			for (int i = 0; i < 3 * k; i+=3)
			{
				sans[i] = cm1;
				sans[i + 1] = cm2;
				sans[i + 2] = cm3;
			}
			l = m2 - k;
			for (int i = 3*k; i < 3 * k + 2*l; i += 2)
			{
				sans[i] = cm1;
				sans[i + 1] = cm2;
			}
			for (int i = 3 * k + 2 * l; i < n; i += 2)
			{
				sans[i] = cm1;
				sans[i + 1] = cm3;
			}
		}
		if(fl)
			cout << "Case #" << tt << ": "<< sans << endl;
		else
			cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}