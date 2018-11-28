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

struct hh
{
	double pos;
	double s;
	double t;
} ;

bool cmp(hh a, hh b)
{
	if (a.pos - b.pos < -eps)
		return 1;
	return 0;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	std::ios_base::sync_with_stdio(0);
	int ttt;
	scanf("%d\n",&ttt);
	for (int tt = 1; tt <= ttt; tt++)
	{
		hh ms[1010];
		int n;
		double d, mv;
		cin>> d >> n;
		for (int i = 1; i <= n; i++)
		{ 
			cin >> ms[i].pos >> ms[i].s;
			ms[i].t = (d - ms[i].pos) / ms[i].s;
		}
		sort(ms + 1, ms + n + 1, cmp);
		double mx = -d;
		for (int i = n; i > 0; i--)
		{
			if (ms[i].t - mx > eps)
				mx = ms[i].t;
			else if (ms[i].t - mx < -eps)
				ms[i].t = mx;
		}
		mv = d / mx;
		cout.precision(9);
		cout << "Case #" << tt << ": ";
		printf("%.8lf", mv);
		cout<< endl;
		
	}
	return 0;
}