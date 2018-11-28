#include <iostream>
#include <cstdio>

using namespace std;

int t;
int d, n, k;
double ans, s;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> t;
	
	for (int l = 0; l < t; l++) {
		cin >> d >> n;
		ans = 1e14;
		for (int i = 0; i < n; i++) {
			cin >> k >> s;
			if (k < d)
				ans = min(ans, d * s / (d - k));
		}	
			
		cout << "Case #" << l + 1 << ": ";
		printf("%.6lf", ans);
		cout << endl;
	}
	
	
	return 0;
}
