
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

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	cout << setprecision(10) << fixed;
	for (int it = 1; it <= t; it++){
		ll d, n, k, s;
		cin >> d >> n;
		ld res;
		for (int i = 0; i < n; i++){
			cin >> k >> s;
			ld cur = (1.0)*d*s/(d-k);	
			if (i == 0 || cur < res)
				res = cur;
		}
		cout << "Case #" << it << ": " << res << '\n';
	}
	return 0;
}
