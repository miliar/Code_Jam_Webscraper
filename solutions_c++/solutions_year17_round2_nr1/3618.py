#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

typedef pair<int, int> cavalo;

int main(){ _
	int t;
	cin >> t;
	cout << fixed << setprecision(6);
	for (int q = 1; q <= t; q++){
		int d, n, a, b;
		cin >> d >> n;
		double t = 0;
		for (int i = 0; i < n; i++){
			cin >> a >> b;
			t = max(t, 1.0*(d-a)/b);
		}
		cout << "Case #" << q <<": "
			 << 1.0*d/t << endl;
	}
	return 0;
}

