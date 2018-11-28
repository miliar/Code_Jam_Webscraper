	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <algorithm>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;
typedef long long ll;
typedef long double ld;

#define double ld

ll x[N], speed[N];
ll d, n;

bool check(double v)
{
	for(int i = 0; i < n; i++)
	{
		double me = d / v;
		double him = double(d - x[i]) / speed[i];
		if(me < him)
			return false;
	}
	return true;
}

int main()
{
	int _t = in();
	for(int _i = 1; _i <= _t; _i++)
	{
		printf("Case #%d: ", _i);
		cin >> d >> n;
		for(int i = 0; i < n; i++)
			cin >> x[i] >> speed[i];
		double L = 0, R = 1e17;
		for(int _t = 0; _t < 400; _t++)
		{
			double mid = (L + R)/2;
			if(check(mid))
				L = mid;
			else
				R = mid;
		}
		if(n == 1)
		{
			double chi = double(d) / (double(d - x[0]) / speed[0]);
			assert(abs(chi - L) <= 1e-6);
		}
		cout << setprecision(10) << fixed << L << endl;
	}
}
