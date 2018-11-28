#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
int t, n, k, j, m;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	while (j++ < t) {
		cin >> n >> k;
		priority_queue<int>q;
		q.push(n);
		for (int i = 0; i < k; ++i) {
			m = q.top();
			--m;
			q.pop();
			q.push(m / 2);
			q.push((m + 1) / 2);
		}
		cout << "Case #" << j << ": " << (m+1) / 2 << " " << m / 2 << endl;
	}
}