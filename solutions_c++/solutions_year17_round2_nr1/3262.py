#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <vector>
#define pb push_back
#define mp make_pair
#define ll long long
#define ld long double
#define bg begin
#define ed end
#define ft first
#define sc second
#define sz size
using namespace std;

vector<ld> v;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++)
	{
		ld d;
		ll n;
		cin >> d >> n;
		while (n--)
		{
			ld i, j;
			cin >> i >> j;
			v.pb((d-i)/j);
		}
		ld ans = 0.00;
		//for (int i = 0; i < v.sz(); i++) cout << v[i] << " ";
		//cout << endl;
		for (ll i = 0; i < v.sz(); i++)
			if (v[i] > ans) ans = v[i];
		cout << "Case #" << tc << ": ";
		ans = d/ans;
		cout << fixed;
		cout << setprecision(6);
		cout << ans << endl;
		v.clear();
	}
	return 0;
}