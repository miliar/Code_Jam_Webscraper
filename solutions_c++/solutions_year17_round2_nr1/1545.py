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
#define x first
#define y second
#define mp make_pair
#define pb push_back
const int N = (int)1e5 + 5, INF = (int)1e9;
const ld EPS = 1e-9;


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	cin >> T;
	cout.precision(10);
	for(int z = 1; z <= T; z++){
		cout << "Case #" << z << ": ";
		int n;
		ld d, mx = -1., k, s;
		cin >> d >> n;
		for(int i = 0; i < n; i++){
			cin >> k >> s;
			mx = max(mx, (d - k) / s);
		}
		cout << fixed << d / mx << "\n";
	}
	return 0;
}