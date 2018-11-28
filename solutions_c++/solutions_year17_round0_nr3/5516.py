#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i=1; i<=T; i++) {
		int n, k;
		cin >> n >> k;
		priority_queue<int> q;
		q.push(n);
		--k;
		while (k--) {
			int s = q.top();
			q.pop();
			int a = (s-1)/2;
			int b = s-1-a;
			if (b > 0) q.push(b);
			if (a > 0) q.push(a);
		//for (auto i : q) cout << i << " ";
		//cout << endl;
		}
		//for (auto i : q) cout << i << " ";
		//cout << endl;
		cout << "Case #" << i << ": " << q.top()-1 - (q.top()-1)/2 << " " << (q.top()-1)/2 << endl;
	}
	return 0;
}
