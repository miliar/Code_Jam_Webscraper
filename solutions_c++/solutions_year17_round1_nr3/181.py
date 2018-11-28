#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

int a[105][105][105][105];
int b, d, init,ttt=0;
int oo = 1000000000;

int f(int hd, int ad, int hk, int ak)
{
	if (a[hd][ad][hk][ak])
		return a[hd][ad][hk][ak];
	a[hd][ad][hk][ak] = oo;
	if (ad >= hk)
		return a[hd][ad][hk][ak] = 1;
	if (hd > ak)
	{
		a[hd][ad][hk][ak] = min(a[hd][ad][hk][ak], 1 + f(hd-ak, ad, hk-ad, ak));
		a[hd][ad][hk][ak] = min(a[hd][ad][hk][ak], 1 + f(hd-ak, min(ad + b, hk), hk, ak));
	}
	if (init - ak > hd)
		a[hd][ad][hk][ak] = min(a[hd][ad][hk][ak], 1 + f(init-ak, ad, hk, ak));
	if (hd > ak-d && ak > 0)
		a[hd][ad][hk][ak] = min(a[hd][ad][hk][ak], 1 + f(hd-max(ak - d,0), ad, hk, max(ak - d,0)));
	return a[hd][ad][hk][ak];
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	cin>>T;
	for (int t = 1; t <= T; t++)
	{
		ttt++;
		int hd, ad, hk, ak, tmp;
		cin>>hd>>ad>>hk>>ak>>b>>d;
		init = hd;
		memset(a,0,sizeof(a));
		tmp = f(hd, ad, hk, ak);
		if (tmp == oo)
			cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<t<<": "<<tmp<<endl;	
	}
	return 0;
}