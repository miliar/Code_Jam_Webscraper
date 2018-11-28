#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>

#define _CRT_SECURE_NO_WARNINGS

using namespace std;

#define iinf 2000000000
#define linf 2000000000000000000LL
#define MOD (1000000007)
#define Pi 3.1415926535897932384
#define bit(mask,i) ((mask>>i)&1)

const string IMPOSSIBLE = "IMPOSSIBLE\n";
inline void case_print() {
	static int it = 0;
	it += 1;
	cout << "Case #" << it << ": ";
}


int dp[720*2 + 10][3][725]= {0};
#define inf 1000000

int main() {
	ios_base::sync_with_stdio(0);
	freopen("C-small-1-attempt0.in", "r",stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	int DAY = 720 * 2;
	
	while (T --> 0) {
		int n,k;
		cin >> n >> k;
		vector<double> a(n + 1, 0.0);
		double u;
		cin >> u;
		for (int i =1; i <= n; i ++) cin >> a[i];
		sort(a.begin() + 1, a.end(), greater<double>());
		a[0] = inf;
		double sum = a[n];
		int breaker = 0;
		for (int i = n - 1; i >= 0; i --) {
			double tmp = sum + u;
			if (tmp *1.0 / (n - i) > 1e-8 + a[i]) {
				sum += a[i];	
				continue;
			}
			breaker = i + 1;
			break;
		}
		
		double product = 1.0;
		sum += u;
		sum = sum * 1.0 / (n - breaker + 1);
		for (int i = 1; i < breaker; i ++) product *= a[i];
		for (int i = breaker; i <= n; i ++) product *= sum;
		case_print();
		cout.precision(10);
		cout << fixed << product << endl;
	}
	
	return 0;
}
