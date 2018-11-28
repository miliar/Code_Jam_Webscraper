#include <bits/stdc++.h>
using namespace std;

string num;
int t;

int main() {
	cin >> t;
	for (int testcase = 1; testcase <= t; testcase++) {
		cin >> num;

		for (int i = num.size() - 1; i > 0; i--) {
			if (num[i] < num[i - 1]) {
			
				num[i - 1] -= 1;
				for (int j = i; j < num.size(); j++) {
					num[j] = '9';
				}
				
			}
		}

		printf("Case #%d: %lld\n", testcase, stoll(num));
	}
}