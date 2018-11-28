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
const int N = (int)1e2 + 5, INF = (int)1e9;
const ld EPS = 1e-9;
ld e[N], s[N], l[N], p[N], d[N];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	cin >> T;
	cout.precision(10);
	for(int z = 1; z <= T; z++){
		int n, q;
		ld x;
		cin >> n >> q;
		for(int i = 0; i < n; i++)
			cin >> e[i] >> s[i];
		p[0] = 0.;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++){
				cin >> x;
				if(j == i + 1){
					l[j] = x;
					p[j] = p[i] + x;
				}
			}
		cin >> x >> x;
		d[0] = 0.;
		for(int i = 1; i < n; i++){
			d[i] = 1e15;
			for(int j = i - 1; j >= 0; j--)
				if(e[j] >= p[i] - p[j])
					d[i] = min(d[i], d[j] + (p[i] - p[j]) / s[j]);
		}
		
		cout << fixed << "Case #" << z << ": " << d[n - 1] << "\n";
	}
	return 0;
}