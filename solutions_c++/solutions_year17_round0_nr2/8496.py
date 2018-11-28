#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	string str;
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		cin >> str;
		
		printf("Case #%d: ", i + 1);
		
		int mini[18], ans[18];
		for (int j = str.length() - 1; j >= 0; j--) {
			if (j == str.length() - 1) {
				mini[j] = str[j] - '0';
			} else {
				mini[j] = min(mini[j + 1], str[j] - '0');
			}
		}
		
		bool isPivotFound = false;
		bool isZeroFound = false;
		
		long long ans1 = 0;
		
		for (int j = 0; j < str.length() - 1; j++) {
			int num = str[j] - '0';
			if (num > mini[j + 1]) {
				isPivotFound = true;
				if (num - 1 <= 0) {
					isZeroFound = true;
					break;
				}
				ans[j] = num - 1;
				for (int k = j + 1; k < str.length(); k++) {
					ans[k] = 9;
				}
				
				int last = num - 1;
				for (int k = j - 1; k >= 0; k--) {
					last = min(str[k] - '0', last);
					ans[k] = last;
				}
				break;
			}
		}
		
		if (isPivotFound) {
			if (isZeroFound) {
				ans1 = 0;
			} else {
				for (int i = 0; i < str.length(); i++) {
					ans1 *= 10;
					ans1 += ans[i];
				}
			}
		} else {
			cout << str << "\n";
			continue;
		}
		
		isPivotFound = false;
		isZeroFound = false;
		
		long long ans2 = 0;
		
		for (int j = str.length() - 2; j >= 0; j--) {
			int num = str[j] - '0';
			if (num > mini[j + 1]) {
				isPivotFound = true;
				if (num - 1 <= 0) {
					isZeroFound = true;
					break;
				}
				ans[j] = num - 1;
				for (int k = j + 1; k < str.length(); k++) {
					ans[k] = 9;
				}
				
				int last = num - 1;
				for (int k = j - 1; k >= 0; k--) {
					last = min(str[k] - '0', last);
					ans[k] = last;
				}
				break;
			}
		}
		
		if (isPivotFound) {
			if (isZeroFound) {
				ans2 = 0;
			} else {
				for (int i = 0; i < str.length(); i++) {
					ans2 *= 10;
					ans2 += ans[i];
				}
			}
		} else {
			cout << str << "\n";
			continue;
		}
		
		int maxi = max(ans1, ans2);
		if (maxi == 0) {
			for (int i = 0; i < str.length() - 1; i++) {
				printf("9");
			}
			printf("\n");
		} else {
			printf("%I64d\n", max(ans1, ans2));
		}
	}
}
