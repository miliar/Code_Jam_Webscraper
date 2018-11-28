#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, p, t, r[55];
int x[55][55];
int y[55][55][2];
int pos[55];

void doit(int abcd) {
	cout << "Case #" << abcd+1 << ": ";
	cin >> n >> p;
	for (int i = 0; i < n; ++i)
		cin >> r[i];
	
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < p; ++j)
			cin >> x[i][j];
		sort(x[i], x[i]+p);
	}

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < p; ++j)
			y[i][j][1] = (10*x[i][j])/(9*r[i]), y[i][j][0] = (10*x[i][j]+11*r[i]-1)/(11*r[i]);

	for (int i = 0; i < n; ++i)
		pos[i] = 0;

	int ct = 0;
	
	while(true) {
		bool z = 1;
		for (int i = 0; i < n; ++i)
			if (pos[i] == p)
				z = 0;
		if (z == 0)
			break;
		
		int mini = 0, maxi = 10000000;
		for (int i = 0; i < n; ++i) {
			mini = max(mini, y[i][pos[i]][0]);
			maxi = min(maxi, y[i][pos[i]][1]);
		}

		if (mini <= maxi) {
			++ct;
			for (int i = 0; i < n; ++i)
				pos[i]++;
			continue;
		}

		int ind = -1;
		maxi = 10000000;

		for (int i = 0; i < n; ++i)
			if (y[i][pos[i]][1] < maxi)
				maxi = y[i][pos[i]][1], ind = i;
		pos[ind]++;
	}

	cout << ct << endl;
}

int main() {
	cin >> t;
	for (int i = 0; i < t; ++i)
		doit(i);
}