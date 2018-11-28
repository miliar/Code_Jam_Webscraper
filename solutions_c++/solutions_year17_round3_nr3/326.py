	//g++ -std=c++0x your_file.cpp -o your_program
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <iomanip>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

const int N = 55;

const double eps = 1e-11;

long double a[N];

void solve() {
	int n, k;
	cin >> n >> k;
	long double c;
	cin >> c;
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
	}
	sort (a + 1, a + n + 1);
	long double ans = 1;
	for (int i = 1; i <= n; i++) {
		ans *= a[i];
	}
	long double cur, sum, curr;
	for (int i = 1; i <= n; i++) {
		cur = a[i];
		sum = 0;
		for (int j = 1; j < i; j++) {
			sum += a[i] - a[j];
		}
		if (sum - c > eps) {
			break;
		}
		sum = c - sum;
		cur += sum / i;
		if (cur - 1 > eps) {
			cur = 1;
		}
		curr = cur;
		for (int j = 1; j < i; j++) {
			cur *= curr;
		}
		for (int j = i + 1; j <= n; j++) {
			cur *= a[j];
		}
		if (cur - ans > eps) {
			ans = cur;
		}
	}
	cout << fixed;
	cout << setprecision(9) << ans << endl;
}

int main() {
	freopen (fname"C-small-1-attempt0.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		solve();
	}
	return 0;
}
