#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

int N, P;
int r[102];
vector<int> q[102]; //qualities
int a[102];
int n[102], n1[102], n2[102];

int ff() {
	int num = 1;
	int ans = 0;
	while (true) {
		for (int i = 0; i < N; ++i ) {
			n[i] = r[i] * num;
			n1[i] = n[i] - (n[i]+9) / 10;
			n2[i] = n[i] + n[i] / 10;
			if (n1[i] > q[i][P-1]) return ans;
		}
		bool flag = false;
		for (int i = 0; i < N; ++i ) {
			while (q[i][a[i]] < n1[i]) ++a[i];
			if (q[i][a[i]] > n2[i]) {
				++num;
				flag = true;
				break;
			}
		}
		if (flag) continue;
		++ans;
		for (int i = 0; i < N; ++i ) {
			++a[i];
			if (a[i]>=P) return ans;
		}
	}
}

void solve() {
	cin >> N >> P;
	for (int i = 0; i < N; ++i ) cin >> r[i];
	for (int i = 0; i < N; ++i ) {
		q[i].clear();
		int x; 
		for (int j = 0; j < P; ++j ) {
			cin >> x;
			q[i].push_back(x);
		}
		sort(q[i].begin(), q[i].end());
		a[i] = 0;
	}
	cout << ff();
}

int main(int argc, char *argv[]) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int testNum;
	cin >> testNum;
	for (int testid = 0; testid < testNum; ++testid ) {
		cout << "Case #" << testid+1 << ": ";
		solve();
		cout << endl;
	}
}