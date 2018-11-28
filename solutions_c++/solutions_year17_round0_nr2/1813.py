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

void solve()
{
	string n;
	cin >> n;
	for (int i=n.size() - 1; i > 0; --i) {
		if (n[i] < n[i-1]) {
			n[i] = '9';
			for (int j=i+1; j<(int)n.size(); ++j) n[j] = '9';
			--n[i-1];
		}
	}
	if (n[0] == '0') n = n.substr(1);
	cout << n;
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
