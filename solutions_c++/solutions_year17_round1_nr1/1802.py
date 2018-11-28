#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i=1; i<=t; i++) {
		int r,c;
		cin >> r >> c;
		char cake[r][c];
		vector<int> x,y;
		for (int j=0; j<r; j++) {
			string str;
			cin >> str;
			for (int k=0; k<c; k++) {
				cake[j][k] = str[k];
				if (cake[j][k] != '?') {
					x.push_back(j);
					y.push_back(k);
				}
			}
		}
		vector<int> X,Y;
		for (int j=0; j<x.size(); j++) {
			int a = x[j];
			int b = y[j];
			char kid = cake[a][b];
			X.push_back(a);
			Y.push_back(b);
			for (int k=b-1; k>=0; k--) {
				if (cake[a][k]=='?') {
					cake[a][k] = kid;
					X.push_back(a);
					Y.push_back(k);
				} else {
					break;
				}
			}
			for (int k=b+1; k<c; k++) {
				if (cake[a][k]=='?') {
					cake[a][k] = kid;
					X.push_back(a);
					Y.push_back(k);
				} else {
					break;
				}
			}
		}
		for (int j=0; j<X.size(); j++) {
			int a = X[j];
			int b = Y[j];
			char kid = cake[a][b];
			for (int k=a-1; k>=0; k--) {
				if (cake[k][b]=='?') {
					cake[k][b] = kid;
				} else {
					break;
				}
			}
			for (int k=a+1; k<r; k++) {
				if (cake[k][b]=='?') {
					cake[k][b] = kid;
				} else {
					break;
				}
			}
		}
		cout << "Case #" << i << ":" << endl;
		for (int j=0; j<r; j++) {
			for (int k=0; k<c; k++) {
				cout << cake[j][k];
			}
			cout << endl;
		}
	}
}