#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
	
	int test;
	string s;
	cin>>test;
	
	for (int testc = 1; testc <= test; testc++) {
		cin>>s;
		int k;
		cin >> k;
		int len = s.length();
		bool ok = true;
		int cnt = 0;
		for (int i = 0; i < len; i++) {
			if (s[i] == '-') {
				if (i > len - k) {
					ok = false;
					break;
				}
				cnt++;
				for (int j = i; j < i+k; j++) {
					s[j] = (s[j]=='-' ? '+' : '-');
				}
			}
			//cout << i << "  " << s << endl;
			
		}
		if (ok)
			cout << "Case #" << testc << ": " << cnt << endl;
		else
			cout << "Case #" << testc << ": IMPOSSIBLE" << endl;
	}
	return 0;
}

