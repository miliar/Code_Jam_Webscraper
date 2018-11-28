#include <bits/stdc++.h>
using namespace std;

#define LL long long int

int main() {
	LL n, t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		vector<int> v;
		cin >> n;
		while(n > 0) {
			v.push_back(n % 10);
			n /= 10;
		}
		reverse(v.begin(), v.end());
		int start = (int)v.size();
		for(int j = 0; j < (int)v.size()-1; j++) {
			if(v[j] > v[j+1]) {
				start = j;
				break;
			}
		}
		if (start != (int)v.size()) {
			int j = start+1;
			while(j < (int)v.size()) v[j++] = 9;
			while(start >= 0) {
				v[start]--;
				if(v[start] != 0) break;
				else if (start > 0) v[start] = 9;
				start--;
			}
		}
		cout << "Case #" << i << ": ";
		int j = 0;
		while(v[j] == 0) j++;
		while( j < (int)v.size() ) cout << v[j++];
		cout << endl;
	}
	return 0;
}