#include<bits/stdc++.h>
using namespace std;
const double PI = 3.141592653589793238463;
int func1(string s, int k) {
	int n = s.size();
	int a = 0;
	int tot = 1;
	for (int i = 0; i < n; ++i) {
		if (s[i] == '+') {
			a |= (1 << (n - i - 1));
		}
		tot *= 2;
	}
	tot--;
	int f = 0, x = 1;
	for (int i = 0; i < k; ++i) {
		f |= (1 << i);
		x *= 2;
	}
	x--;
	//cout<<tot<<" "<<x<<endl;
	vector<bool> visited(tot + 1, false);
	vector<int> parent(tot + 1, -1);
	queue<int> q;
	int g, d, l;
	q.push(a);
	visited[a] = true;
	while (!q.empty()) {
		d = q.front();
		//	cout<<d<<endl;
		q.pop();
		if (d == tot) {
			break;
		}
		for (int i = 0; i <= n - k; ++i) {
			g = d ^ (x << i);
			//	cout<<"g= "<<g<<endl;
			if (!visited[g]) {
				q.push(g);
				parent[g] = d;
				//	cout<<"parent of g="<<q.size()<<endl;
				visited[g] = true;
			}
		}
		d = -1;
	}
	int ans = -1;
	while (d != -1) {
		d = parent[d];
		ans++;
	}
	return ans;
}
int func2(string s, int k) {
	int n = s.size();
	vector<bool> a(n, 0);
	int tot = 1;
	for (int i = 0; i < n; ++i) {
		if (s[i] == '+') {
			a[i] = 1;
		}
	}
	int b = 0, e = n;
	while (a[b]) {
		b++;
	}
	int ans=0;
	while (b <=e-k) {
		ans++;
		for (int i = 0; i < k; ++i) {
			a[b+i]=!a[b+i];
		}
		while (a[b]) {
			b++;
		}
	}
	for (int i = 0; i < n; ++i) {
		if(!a[i]){
			return -1;
		}
	}
	return ans;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int t, k;
	string s;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> s >> k;
		//int ans = func1(s, k);
		cout << "Case #" << i << ": ";
		/*if (ans == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << ans;
		}
		cout<<"  ";*/
		int ans2 = func2(s, k);
		if (ans2 == -1) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << ans2 << endl;
		}
	}
	return 0;

}
