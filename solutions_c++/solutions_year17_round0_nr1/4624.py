#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	string s;
	int T, k;
	cin >> T;

	for(int i=1; i<=T; i++) {
		cin >> s; cin >> k; 
		vector<int> v;
		int n = s.size();
		for(int j=0; j<n; j++) {
			if (s[j] == '+') {
				v.push_back(1);
			} else {
				v.push_back(0);
			}
		}

		int flip = 0;
		int cur = 0;

		for(int j=0; j<=n-k; j++) {
			if (v[j] == 0)	{
				for(int x=j; x<j+k; x++) v[x] = 1 - v[x];
				flip ++;
			}	
		}

		bool success = true;
		for(int j=n-k; j<n; j++) {
			if (v[j] == 0) success = false;
		}

		if (success) {
			cout << "Case #" << i << ": " << flip << endl;
		} else { 
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
	}
}