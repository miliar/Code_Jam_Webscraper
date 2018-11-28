#include <string>
#include <iostream>

using namespace std;

void go() {
	string s;
	cin >> s;
	int k;
	cin >> k;
	int n;
	n = s.length();
	int res = 0;
	for(int i = 0; i < n-k+1; i++) {
		if(s[i]=='-') {
			res++;
			for(int j = 0; j < k; j++) {
				if(s[i+j]=='+') s[i+j]='-';
				else s[i+j] = '+';
			}
		}
	}
	for(int i = n-k+1; i < n; i++) {
		if(s[i]=='-') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << res << endl;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(0);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		go();
	}
	return 0;
}


