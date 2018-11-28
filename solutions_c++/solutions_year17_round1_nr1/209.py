#include<bits/stdc++.h> 
using namespace std;
int x[300005];
vector<int> v[300005];
multiset<int> r;
int main() {
	int n;
	cin >> n;
	int s = 0;
	for (int i = 0; i<n; ++i) {
		scanf("%d", &x[i]);
		r.insert(x[i]);
	}
	for (int i = 0; i<n - 1; ++i) {
		int a, b;
		scanf("%d%d", &a, &b);
		a--;
		b--;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	int minn = 2e9;
	for (int i = 0; i<n; ++i) {
		int maxx = x[i];
		r.erase(r.find(x[i]));
		for (int j = 0; j<v[i].size(); ++j) {
			maxx = max(maxx, x[v[i][j]] + 1);
			r.erase(r.find(x[v[i][j]]));
		}
		if (!r.empty()) maxx = max(maxx, (*r.rbegin()) + 2);
		r.insert(x[i]);
		for (int j = 0; j<v[i].size(); ++j) {
			r.insert(x[v[i][j]]);
		}
		minn = min(minn, maxx);
	}
	cout << minn << endl;
}