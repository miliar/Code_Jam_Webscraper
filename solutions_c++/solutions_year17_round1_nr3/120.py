#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

#define cin fin
#define cout fout

ifstream fin("a.in");
ofstream fout("a.out");

long long hd, ad, hk, ak, b, d;

long long f(long long hd, long long h, long long ak, long long b, long long ad, long long hk)
{
	long long ans = (hk - 1) / ad + 1;
	for(int i = 1;; i++)
	{
		ad += b;
		long long xx = (hk - 1) / ad + 1 + i;
	//	cout << xx << " " << ans << endl;
		if(xx > ans) break;
		if(xx < ans) ans = xx;
	}
	if(ak <= 0)
		return ans;
	if(ans <= (h - 1) / ak + 1)
		return ans;
	long long x = ans;
	ans++;
	x -= (h - 1) / ak;
	long long c = ((hd - 1) / ak);
	ans += (x - 2) / (c - 1);
	return ans;
}

long long calc()
{
	if(ad >= hk) return 1;
	if(ak - d >= hd) return -1;
	if(ad * 2 < hk && ad + b < hk && (ak - d) + (ak - d - d) >= hd) return -1;
	if(ad * 2 >= hk || ad + b >= hk) return 2;
	long long ans = -1;
	long long t = 0, h = hd, a = ak;
	long long rd = 1000000;
	if(d != 0 && 2*(ak / d + 1) < rd)
		rd = 2*(ak / d + 1);
	if(d == 0)
		rd = 1;
	for(int i = 1; i <= rd; i++)
	{
		if(h <= a - d)
		{
			t++;
			h = hd - a;
		}
		else if(i != 1)
		{
			t++;
			a -= d;
			if(a > 0) h -= a;
		}
	//	cout << a << ":" << h << endl;
		if(a * 2 >= hd) continue;
		long long anst = t + f(hd, h, a, b, ad, hk);
		if(ans == -1)
			ans = anst;
		else
		{
			ans = min(anst, ans);
		}
	}
	return ans;
}

int main()
{
	int Test;
	cin >> Test;
	for(int t = 1; t <= Test; t++)
	{
		cin >> hd >> ad >> hk >> ak >> b >> d;
		
		long long ans = calc();
		if(ans == -1)
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << t << ": " << ans << endl;
	}
	
	return 0;
}

