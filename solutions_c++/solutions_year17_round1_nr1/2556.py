#include <bits/stdc++.h>
using namespace std;

char cake[25][25];

int main() {
	int t; cin >> t;

	for(int C=1; C<=t; C++) {
		string ans = "";
		
		int r, c; cin >> r >> c;
		
		bool empty[r];
		for(int i=0; i<r; i++) {
			empty[i] = true;
		}
		
		for(int i=0; i<r; i++) {
			string s; cin >> s;
			for(int j=0; j<c; j++) {
				cake[i][j] = s[j];
				if( s[j] != '?' ) {
					empty[i] = false;
				}
			}
		}
		
		for(int i=0; i<r; i++) {
			if( !empty[i] ) {
				
				for(int j=1; j<c; j++) {
					if( cake[i][j] == '?' && cake[i][j-1] != '?' ) {
						cake[i][j] = cake[i][j-1];
					}
				}
				
				for(int j=c-2; j>=0; j--) {
					if( cake[i][j] == '?' && cake[i][j+1] != '?' ) {
						cake[i][j] = cake[i][j+1];
					}
				}
				
			}
		}
		
		for(int i=1; i<r; i++) {
			if( empty[i] && !empty[i-1] ) {
				for(int j=0; j<c; j++) {
					cake[i][j] = cake[i-1][j];
				}
				empty[i] = false;
			}
		}
		
		for(int i=r-2; i>=0; i--) {
			if( empty[i] && !empty[i+1] ) {
				for(int j=0; j<c; j++) {
					cake[i][j] = cake[i+1][j];
				}
				empty[i] = false;
			}
		}
		
		cout << "Case #" << C << ":" << endl;
		
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				cout << cake[i][j];
			}
			cout << endl;
		}
	}
}