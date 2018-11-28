#include <string>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	freopen("text.txt", "w", stdout);
	long long tc; scanf("%lld", &tc);
	for (long long t = 1; t <= tc; t++) {
		string str,dap;
		cin >> str;
		for (long long i = 1; i < (long long)str.size(); i) {
			long long ans = str[0] - '0';
			bool flag = false;
			for (long long j = 1; j < (long long)str.size(); j++) {
				if (flag) {
					dap += '9';
				}
				else {
					ans *= 10LL;
					if (str[j - 1] > str[j]) {
						flag = true;
						ans--;
					}
					else {
						ans += str[j] - '0';
					}
				}
			}
			string s1 = "";
			dap += (ans % 10) + '0';
			ans /= 10;
			while (ans) {
				s1 += (ans%10) + '0';
				ans /= 10;
			}
			reverse(s1.begin(), s1.end());
			str = "";
			if (!flag) {
				while (!s1.empty()) {
					dap += s1.back();
					s1.pop_back();
				}
			}
			else str = s1;
		}
		printf("Case #%lld: ", t);
		if (str.size() == 1) printf("%c", str[0]);
		for (long long i = (long long)dap.size() - 1; i >= 0; i--) {
			printf("%c", dap[i]);
		}
		printf("\n");
	}

}