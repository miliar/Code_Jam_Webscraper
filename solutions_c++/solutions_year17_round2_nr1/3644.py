#include <iostream>
#include<string>
#include<stdlib.h>
#include<limits.h>
#pragma warning(disable :4996)
using namespace std;
long double a[6000006], b[6000006], c[6000006], d[6000006];
/*int compare(const void * a, const void * b)
{

	order *orderA = (order *)a;
	order *orderB = (order *)b;

	return (orderB->price - orderA->price);
}*/
string s;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("ou.txt", "w", stdout);
	int t, i1 = 0;
	cin >> t;
	while (t--) {
		long double ans, ma,sp, n, m, d;
		int i, j, k;
		cin >> d >> n;
		for (i = 0; i < n; i++)
			cin >> a[i]>>b[i];
		ans = 500000000000000000;
		std::cout.precision(20);
		for (i = 0; i < n; i++)
		{
			m = d - a[i];
			if (m > 0) {
				sp = m / b[i];
				m = d / sp;
				if (m < ans) {
					ans = m;
					//ma = d / ans;
				}
			}
		}
		i1++;
		cout << "Case #" << i1 << ": " <<ans << endl;
	}
	return 0;
}