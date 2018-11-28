#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

void solve(int t)
{
	long long d,n;
	cin >> d >> n;
	pair<long long,long long> a[n];

	for (int i=0; i<n; i++)
		cin >> a[i].first >> a[i].second;

	sort(a,a+n);

	int k=n-1;
	for (int i=n-2; i>=0; i--)
		if ((d-a[k].first)*a[i].second < (d-a[i].first)*a[k].second)
			k=i;

//	cout << k << " " << a[k].first << " " << a[k].second << endl;
	cout.setf(ios::fixed,ios::floatfield);
	cout << "Case #" << setprecision(0) << t << ": " << setprecision(6) << (d/((double)(d-a[k].first)/a[k].second)) << endl;
}

int main()
{
	int t;
	cin >> t;

	for (int i=1; i<=t; i++)
		solve(i);

//	solve(1);
}
