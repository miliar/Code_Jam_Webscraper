#include <bits/stdc++.h>

using namespace std;

int main() {
	int _T;
	cin >> _T;
	for(int _t = 1; _t <= _T; _t++) {
		cout << "Case #" << _t << ": ";
		long long n, k;
		cin >> n >> k;
		map <long long, long long, greater <long long> > Q;
		Q.insert(make_pair(n, 1));
		while (!Q.empty()) {
			pair <long long, long long> u = *Q.begin();
			//cout << u.first << " " << u.second << endl;
			Q.erase(Q.begin());
			long long v = u.first;
			if (u.second >= k) {
				cout << v / 2 << " " << (v - 1) / 2 << "\n";
				break;
			}
			else {
				k -= u.second;
				map <long long, long long>::iterator it = Q.find((v - 1) / 2);
				if (it == Q.end())
					Q.insert(make_pair((v - 1) / 2, u.second));
				else
					it->second += u.second;
				it = Q.find(v / 2);
				if (it == Q.end())
					Q.insert(make_pair(v / 2, u.second));
				else
					it->second += u.second;
			}
		}
	}
	return 0;
}