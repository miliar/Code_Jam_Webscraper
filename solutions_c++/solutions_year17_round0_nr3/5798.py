// Khaled Alam - KhaledAlam.net
// Google Code Jam 2017 | Problem C
#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	long long tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t) {
		long long a, b;
		cin >> a >> b;
		int y = a, z = a;
		priority_queue<long long>q;
		q.push(a);
		for (int i = 1; i <= b; i++) {
			int len = q.top();
			q.pop();
			z = len % 2 == 0 ? len / 2 - 1 : len / 2, y = len / 2;
			q.push(y), q.push(z);
		}
		cout << "Case #" << t << ": " << y << ' ' << z<< '\n';
	}
}
