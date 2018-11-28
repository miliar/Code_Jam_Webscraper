#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <unordered_map>
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
	ull n, k;
	cin >> n >> k;
	unordered_map<ull,ull> spaces;
	spaces[n] = 1;
	priority_queue<ull> q;
	q.push(n);
	ull last = n + 1;
	vector<pair<ull,ull>> order;
	while (!q.empty()) {
		ull c = q.top(); q.pop();
		if (c >= last) continue;
		last = c;
		order.push_back(make_pair(c, spaces[c]));
		ull smaller = (c - 1) / 2;
		ull larger = c - smaller - 1;
		spaces[larger] += spaces[c];
		spaces[smaller] += spaces[c];
		if (larger > 2) q.push(larger);
		if (larger != smaller && smaller > 2) q.push(smaller);
	}
	FORVEC(ii, order) {
		if (ii->first <= 2) break;
		//cout << "There are " << ii->second << " spaces of size " << ii->first << endl;
		if (k <= ii->second) {
			ull smaller = (ii->first - 1) / 2;
			ull larger = ii->first - smaller - 1;
			cout << larger << " " << smaller;
			return;
		}
		k -= ii->second;
	}
	//cout << "There are " << spaces[2] << " spaces of size 2" << endl;
	//cout << "There are " << spaces[1] << " spaces of size 1" << endl;
	if (k <= spaces[2]) {
		cout << "1 0";
	} else {
		cout << "0 0";
	}
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
