#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORVEC(it,v) for (auto it=(v).begin(); it != (v).end(); ++it)
#define NUL(arr) memset(arr, 0, sizeof(arr));
#define SORT(x) sort((x).begin(), (x).end());

vector<int> s[1001]; // seats of passenger i
int z[1001]; // number of tickets sold for seat i

void solve()
{
	FOR(i,1001) s[i].clear();
	FOR(i,1001) z[i] = 0;
	int n, c, m;
	cin >> n >> c >> m;
	FOR(i,m) {
		int p, b;
		cin >> p >> b;
		s[b].push_back(p);
		++z[p];
	}
	int trains = max(s[1].size(), s[2].size());
	trains = max(trains, z[1]);
	int prom = 0;
	for (int i=1; i<=n; ++i) {
		if (z[i] > trains) prom += (z[i] - trains);
	}
	cout << trains << " " << prom;
}

int main()
{
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
