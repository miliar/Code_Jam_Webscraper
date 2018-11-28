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

struct st
{
	int b, e, c;
};
bool cmp(st a, st b)
{
	if (a.b < b.b)
		return 1;
	return 0;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	std::ios_base::sync_with_stdio(0);
	int ttt;
	scanf("%d\n", &ttt);
	for (int tt = 1; tt <= ttt; tt++)
	{
		int ans = 1, n1,n2, t1=0, t2=0,b,e,mn = 1500;
		st ms[2880] = { 0 };
		cin >> n1 >> n2;
		for (int i = 1; i <= n1; i++)
		{
			cin >> ms[i].b >> ms[i].e;
			ms[i].c = 1;
			t1 += ms[i].e - ms[i].b;
		}
		for (int i = 1; i <= n2; i++)
		{
			cin >> ms[i+ n1].b >> ms[i + n1].e;
			ms[i + n1].c = 2;
			t2 += ms[i + n1].e - ms[i + n1].b;
		}
		sort(ms + 1, ms + n1 + n2 + 1, cmp);
		ms[n1 + n2 + 1] = ms[1];
		ms[n1 + n2 + 1].b += 1440;
		ms[n1 + n2 + 1].e += 1440;
		mn = n1 + n2 + 1;
		ans = 0;
		for (int i = 2; i <= mn; i++)
			if (ms[i].c != ms[i - 1].c)
				ans++;
		for (int i = 2; i <= mn; i++)
			if (ms[i].c == ms[i - 1].c)
			{
				if (ms[i].c == 1)
				{
					if (t1 + ms[i].b - ms[i-1].e <= 720)
						t1 += ms[i].b - ms[i-1].e;
					else
					{
						ans += 2;
						t2 = min(t2 + ms[i].b - ms[i-1].e, 720);
					}
				}
				else
					{
						if (t2 + ms[i].b - ms[i-1].e <= 720)
							t2 += ms[i].b - ms[i-1].e;
						else
						{
							ans += 2;
							t1 = min(t1 + ms[i].b - ms[i-1].e, 720);
						}
					}
			}
		if (ans == 0)
			ans = 2;
		cout << "Case #" << tt << ": " << ans << endl;
	
	}
	return 0;
}