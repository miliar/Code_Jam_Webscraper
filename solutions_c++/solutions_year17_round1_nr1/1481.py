#include <bits/stdc++.h>
using namespace std;

int h, w, e[30];
char a[30][30];

void exec(int t) {
	cin >> h >> w;
	for (int i=0; i<h; i++)
		cin >> a[i];

	for (int i=0; i<h; i++) {
		for (int j=0; j<w; j++) {
			if (a[i][j] != '?') {
				for (int k=j-1; k>=0 and a[i][k] == '?'; k--) a[i][k] = a[i][j];
				for (int k=j+1; k<w and a[i][k] == '?'; k++) a[i][k] = a[i][j];
			}
		}
	}

	for (int i=0; i<h; i++) {
		e[i] = 1;
		for (int j=0; j<w; j++) if (a[i][j] != '?') e[i] = 0;
	}
	for (int i=0; i<h; i++) if (e[i]) {
		int k = i;
		while (e[k] and k>=0) k--;
		if (k<0) k = 0;
		while (e[k] and k<h) k++;
		for (int j=0; j<w; j++) a[i][j] = a[k][j];
	}

	cout << "Case #" << t << ":\n";

	for (int i=0; i<h; i++)
		cout << a[i] << '\n';
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);


	int t;
	scanf("%d", &t);
	for (int i=1; i<=t; i++) exec(i);
}
