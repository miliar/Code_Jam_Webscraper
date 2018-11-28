#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

bool lessThan(string aaa, string abc) {
	
}

int main() {
	int t; cin >> t;
	for(int c=1; c<=t; c++) {
		string s; cin >> s;
		int n = s.length();
		
		char ans[ n ];
		for(int i=0; i<n; i++) {
			char model = s[i];
			bool ok = true;
			for(int j=i+1; j<n; j++) {
				ok = (model <= s[j]);
				if(model < s[j]) {
					ok = true;
					break;
				} else if(model > s[j]) {
					ok = false;
					break;
				}
			}
			if(ok) {
				ans[i] = model;
			} else {
				ans[i] = model-1;
				for(int j=i+1; j<n; j++) {
					ans[j] = '9';
				}
				break;
			}
		}
		
		cout << "Case #" << c << ": ";
		bool doneLZeroes = false;
		for(int i=0; i<n; i++) {
			if( !doneLZeroes ) {
				if( ans[i] == '0' ) {
					continue;
				} else {
					doneLZeroes = true;
					cout << ans[i];
				}
			} else {
				cout << ans[i];
			}
		}
		cout << endl;
	}
}