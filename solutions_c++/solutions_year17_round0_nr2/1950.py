#include <bits/stdc++.h>
using namespace std;

vector<unsigned long long> v;

void build() {
	queue<unsigned long long> q;
	queue<int> q2;
	for(int i = 1; i <= 9; i++) {
		v.push_back(i);
		q.push(i);
		q2.push(1);
	}

	for( ; ; ) {
		long long u = q.front(); q.pop();
		int r = q2.front(); q2.pop();
		if(r == 19) break;

		for(int i = u % 10; i <= 9; i++) {
			unsigned long long val = u * 10 + i;
			q.push(val);
			q2.push(r + 1);
			v.push_back(val);
		}
	}
}

int main() {
	build();

	int t , kase = 0;
	cin >> t;
	for( ; t--; ) {
		unsigned long long n;
		cin >> n;
		cout << "Case #" << ++kase << ": " << *(upper_bound(v.begin() , v.end() , n) - 1) << endl;
	}
	return 0;
}