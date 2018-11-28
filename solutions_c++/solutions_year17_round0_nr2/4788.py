
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

int a[100];

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++){
		ll n;
		cin >> n;
		ll ans = 0;
		int d = 0;
		while (n){
			a[d++] = n%10;
			n /= 10;
		}
		for (int i = 0; i <= d; i++){
			ll x = 0;
			bool b = true;
			for (int j = 0; j < i-1; j++)
				b &= (a[d-j-1] <= a[d-j-2]);
			if (d-i && i)
				b &= a[d-i] <= a[d-i-1]-1;
			if (b == false) continue;
			for (int j = 0; j < d; j++)
				x = x*10 + (j < i ? a[d-j-1] : (j == i ? a[d-j-1]-1 : 9));
			ans = max (ans, x);
		}
		ll x = 0;
		for (int i = 0; i < d-1; i++)
			x = x*10 + 9;
		ans = max (ans, x);
		cout << "Case #" << it << ": " << ans << '\n';
	}

	return 0;
}
