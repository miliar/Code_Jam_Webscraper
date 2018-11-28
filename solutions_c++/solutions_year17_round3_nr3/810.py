#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;
#define x first
#define y second
#define mp make_pair
#define pb push_back
const int N = (int)1e3 + 5, INF = (int)1e9;
const ld EPS = 1e-9;

ld p[N];

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	cin >> T;
	cout.precision(10);
	for(int z = 1; z <= T; z++){
		cout << "Case #" << z << ": ";
		int n, k;
		ld u;
		cin >> n >> k >> u;
		for(int i = 0; i < n; i++)
			cin >> p[i];
		sort(p, p + n);
		p[n++] = 1.;
		for(int i = 0; i < n - 1; i++){
			ld c = min(u, (p[i + 1] - p[i]) * (i + 1)) / (i + 1);
			for(int j = 0; j <= i; j++)
				p[j] += c;
			u -= c * (i + 1);
		}
		ld ans = 1.;
		for(int i = 0; i < n - 1; i++)
			ans *= p[i];
		cout << fixed << ans << "\n";
	}
	return 0;
}