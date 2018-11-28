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
pll a[N];
bool cmp(pll a, pll b) {
	return a.x * a.y > b.x * b.y;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	cin >> T;
	cout.precision(10);
	for(int z = 1; z <= T; z++){
		int n, k;
		cin >> n >> k;
		for(int i = 0; i < n; i++)
			cin >> a[i].x >> a[i].y;
		sort(a, a + n, cmp);
		ll s = 0, mx = -1;
		for(int i = 0; i < k; i++)
			s += 2 * a[i].x * a[i].y;
		for(int i = 0; i < n; i++){
			ll c = a[i].x * a[i].x;
			if(i < k)
				c += s;
			else
				c += 2 * a[i].x * a[i].y - 2 * a[k - 1].x * a[k - 1].y + s;
			mx = max(mx, c);
		}
		cout << "Case #" << z << ": ";
		cout << fixed << mx * M_PI << "\n";
	}
	return 0;
}