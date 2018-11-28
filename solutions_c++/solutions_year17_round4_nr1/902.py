#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int t;
vector < int > a;
int n, p;
int x;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> t;
	
	for (int l = 0; l < t; l++) {
		cin >> n >> p;
		a.clear();
		a.resize(p);
		for (int i = 0; i < n; i++) {
			cin >> x;
			a[x % p]++;
		}
		
		//~ cout << a[0] << ' ' << a[1] << ' ' << a[2] << ' ' << a[3] << endl;
		int ans = 0;
		if (p == 2)
			ans = a[0] + (a[1] + 1) / 2;
		else if (p == 3) {
			if (a[1] > a[2])
				ans = a[0] + a[2] + (a[1] - a[2] + 2) / 3;
			else
				ans = a[0] + a[1] + (a[2] - a[1] + 2) / 3;
			}
		else if (p == 4) {
			if (a[1] >= a[3])
				if (a[2] % 2 == 0)
					ans = a[0] + a[3] + a[2] / 2 + (a[1] - a[3] + 3) / 4;
				else
					ans = a[0] + a[3] + a[2] / 2 + (a[1] - a[3] + 5) / 4;
			else
				if (a[2] % 2 == 0)
					ans = a[0] + a[1] + a[2] / 2 + (a[3] - a[1] + 3) / 4;
				else
					ans = a[0] + a[1] + a[2] / 2 + (a[3] - a[1] + 5) / 4;
		}
			
		cout << "Case #" << l + 1 << ": ";
		cout << ans;
		cout << endl;
	}	
	
	return 0;
}
