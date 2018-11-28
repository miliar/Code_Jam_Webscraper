#include <iostream>
#include <algorithm>
#include <cstdio>
#include <iomanip>

using namespace std;

struct horse{
	int x, speed;
};

int main()
{
	int t, I = 0;
	cin >> t;
		cout << setprecision(6) << fixed;
	while (t--)
	{
		I++;
		int d, n;
		cin >> d >> n;
		horse h[1001];
		long double he = 0, worst = -1;
		for (int i = 0; i < n; i++)
		{
			cin >> h[i].x >> h[i].speed;
			he = 1.0*(d - h[i].x) / h[i].speed;
			if (he > worst)
				worst = he;
		}
//		cout << d - h[0].x << endl;
//		cout << 1.0*(d-h[0].x)/h[0].speed << endl;;
//		cout << "Sec: " << worst << " and d: " << d  << endl;
		cout << "Case #" << I << ": ";
		long double ans = d / worst;
		cout << ans << endl;
//		cout << "ss" << endl;
	}
}
