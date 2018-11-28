//g++ -std=c++0x your_file.cpp -o your_program
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

inline void solve() {
	priority_queue <pair <int, int> > q;
	int n, k;
	cin >> n >> k;
	q.push(mp(n, -1));
	int len, l, mid;
	int ans1, ans2;
	for (int i = 1; i <= k; i++) {
		len = q.top().F;
		l = -q.top().S;
		q.pop();
//		cout << len << " " << l << endl;
		mid = l + (len + 1) / 2 - 1;
		ans1 = mid - l;
		ans2 = l + len - mid - 1;
		q.push(mp(ans1, -l));
		q.push(mp(ans2, -(mid + 1)));
	}
	cout << max(ans1, ans2) << " " << min(ans1, ans2) << endl;
}

int main() {
	freopen (fname"C-small-2-attempt0.in.txt", "r", stdin);
	freopen (fname"out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++) {
		cout << "Case #" << Case << ": ";
		solve();
	}
	return 0;
}
