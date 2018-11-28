#include <bits/stdc++.h>

using namespace std;

int T, R, C; 
char a[50][50];

int isempty(int i) {
	for(int j = 0; j < C; j ++) {
		if(a[i][j] != '?') {
			return 0;
		}
	}
	return 1;
}

void fill(int i) {
	int j = 0;
	while(a[i][j] == '?') j ++;
	for(int k = 0; k < j; k ++) a[i][k] = a[i][j];
	for(j = j+1; j < C; j ++) {
		if(a[i][j] == '?') {
			a[i][j] = a[i][j-1];
		}
	}
}

void copy(int i, int j) {
	for(int k = 0; k < C; k ++) {
		a[j][k] = a[i][k];
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >>  T;
	for(int cas = 1; cas <= T; cas ++) {
		cin >> R >> C;
		for(int i = 0; i < R; i ++) {
			cin >> a[i];
		}
		
		int i = 0;
		while(isempty(i)) i ++;
		fill(i);
		for(int k = 0; k < i; k ++) {
			copy(i, k);
		}
		for(i = i+1; i < R; i ++) {
			if(isempty(i)) {
				copy(i-1, i);
			} else {
				fill(i);
			}
		}
		
		cout << "Case #" << cas << ":" << endl;
		for(int i = 0; i < R; i ++) {
			cout << a[i] << endl;
		}
	}
	return 0;
}

