#include <iostream>
#include <string>
using namespace std;

int main() {
	int t, i1, i2, len_s, max_s, i3, i4, i5;
	string s, ans, ans1;
	cin >> t;
	for (i1 = 0; i1 < t; i1++) {
		cin >> s;
		len_s = s.size();
		max_s = '1';
		ans = "";
		ans1 = "";
		for (i2 = 0; i2 < len_s; i2++) {
			if (s[i2] >= max_s) {
				max_s = s[i2];
				ans += s[i2];
			} else {
				for (i3 = ans.size() -1; i3 >= 0; i3--) {
					if (i3 == 0) {
						i5 = '0';
					} else {
						i5 = ans[i3-1];
					}
					if (i5 <= ans[i3]-1) {
						ans[i3]--;
						break;
					}
				}
				i4 = i3;
				for(i3 = 0; i3 <= i4; i3++) {
					ans1 += ans[i3];
				}
				ans = ans1;
				
				for(i3 = i4+1; i3 < len_s; i3++) {
					ans += '9';
				}
				break;
			}
		}
		// remove 0 from starting and print
		for (i2 = 0; i2 < ans.size(); i2++) {
			if (ans[i2] != '0') {
				i3 = i2;
				break;
			}
		}
		cout << "Case #" << i1+1 << ": ";
		for (i2 = i3; i2 < ans.size(); i2++) {
			cout << ans[i2];
		}
		cout << endl;
		
	}
	return 0;
}
