
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
const int maxn = 1005;
const ld PI = 3.14159265359;

pii a[maxn];

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	cout << setprecision(10) << fixed;
	for (int it = 1; it <= t; it++){
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> a[i].fi >> a[i].se;
		sort (a, a + n);
		multiset <ld> s;
		ld ans = 0, sum = 0;
		for (int i = 0; i < n; i++){
			ld surf = PI*a[i].fi*a[i].fi;
			ld side = PI*2*a[i].fi*a[i].se;
			ans = max (ans, surf + side + sum);
			sum += side;
			s.insert(side);
			if (s.size() > k-1){
				sum -= (*s.begin());
				s.erase(s.begin());
			}
		}
		cout << "Case #" << it << ": " << ans << '\n';
	}
	return 0;
}
