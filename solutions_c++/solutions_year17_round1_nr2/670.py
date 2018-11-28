#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#define ll long long

using namespace std;

int n, p;
int R[100], Q[100][100];
int ptr[100];

int roundUp(int q, int r) {
	return (q + r - 1) / r;
}

int getUp(int Q, int R) {
	int l = 0;
	int r = 1e9;
	while (l < r) {
		int cen = (l + r + 1) / 2;
		ll mincost = (ll)cen * R;
		mincost *= 9;
		if (mincost <= Q * 10) l = cen;
		else r = cen - 1;
	}
	return l;
}

int getFloor(int Q, int R) {
	int l = 1;
	int r = 1e9;
	while (l < r) {
		int cen = (l + r) / 2;
		ll maxcost = (ll)cen * R;
		ll mincost = maxcost * 9;
		maxcost *= 11;
		if (maxcost < Q * 10) l = cen + 1;
		else r = cen;
	}
	return l;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output", "w", stdout);

	int t, testnum = 1;
	cin >> t;
	while (t--) {
		cin >> n >> p;
		for (int i = 0; i < n; ++i) 
			cin >> R[i];
		for (int i = 0; i < n; ++i) {
			for (int q = 0; q < p; ++q)
				cin >> Q[i][q];
			sort(Q[i], Q[i] + p);
		}
		cout << "Case #" << testnum++ << ": ";

		/*
		cerr << "---\n";
		for (int i = 0; i < n; ++i)
			for (int q = 0; q < p; ++q) {
				cerr << "- " << Q[i][q] << ' ' << R[i] << ' ' << getFloor(Q[i][q], R[i]) << ' ' << getUp(Q[i][q], R[i]) << "\n";
			}
		cerr << "---\n";
		*/
		

		for (int i = 0; i < n; ++i)
			ptr[i] = 0;
		int kits = 0;
		bool end = 0;
		while (!end) {
			int min_ = 0;
			bool skip = 0;
			for (int i = 0; i < n; ++i) {
				min_ = max(min_, getFloor(Q[i][ptr[i]], R[i]));
				//cout << ptr[i] << ' ';
			}
			//cout << ": " << min_ << "\n";
			for (int i = 0; i < n && !end; ++i) {
				//cout << getUp(Q[i][ptr[i]], R[i]) << ' ' << i << ' '  << ptr[i] << "\n";
				while (getUp(Q[i][ptr[i]], R[i]) < min_) {
					++ptr[i];
					if (ptr[i] == p) end = 1;
				}
				if (getFloor(Q[i][ptr[i]], R[i]) > min_) {
					skip = 1;
					break;
				}
			}
			if (end) break;
			if (skip) continue;
			++kits;
			for (int i = 0; i < n; ++i) {
				ptr[i]++;
				if (ptr[i] == p) end = 1;
			}
		}
		cout << kits << "\n";
	}

	return 0;
}

/*
6
2 1
500 300
900
660
2 1
500 300
1500
809
2 2
50 100
450 449
1100 1101
2 1
500 300
300
500
1 8
10
11 13 17 11 16 14 12 18
3 3
70 80 90
1260 1500 700
800 1440 1600
1700 1620 900
*/