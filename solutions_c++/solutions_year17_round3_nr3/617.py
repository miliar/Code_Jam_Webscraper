
//be naame khodaa

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <sstream>
#define fi first
#define se second
#define rep(i, x, n) for (int i = x; i < n; i++)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
using namespace std;
typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> VI;
typedef long double ld;

ld p[105];

int main()
{
	cout << setprecision(10) << fixed;
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++){
		int n, k;
		cin >> n >> k;
		ld u;
		cin >> u;
		for (int i = 0; i < n; i++)
			cin >> p[i];
		sort (p, p + n);
		p[n] = 1;
		for (int i = 0; i < n; i++){
			if (u <= (p[i+1] - p[i])*(i+1)){
				for (int j = 0; j < i+1; j++)
					p[j] += u/(i+1);
				break;
			}
			else{
				u -= (p[i+1] - p[i])*(i+1);
				for (int j = 0; j < i+1; j++)
					p[j] = p[i+1];
			}
		}
		ld res = 1;
		for (int i = 0; i < n; i++)
			res *= p[i];
		cout << "Case #" << it << ": " << res << '\n';
	}
	return 0;
}
