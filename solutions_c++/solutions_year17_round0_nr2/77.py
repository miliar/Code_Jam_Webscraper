#include <bits/stdc++.h>

using namespace std;

void runTestCase(int t) {
	long long n;
	cin >> n;
	
	vector<int> dig;
	while(n > 0) {
		dig.push_back(n % 10);
		n /= 10;
	}

	vector<int> ans(dig.size(), 9);
	
	for(int i = dig.size()-1; i >= 0; i--) {
		if(ans[i] >= dig[i]) {
			ans[i] = dig[i];
			if(i != dig.size()-1 && ans[i] < ans[i+1]) {
				ans[i+1]--;
				i+=2;
			}
		}
		else {
			if(i != dig.size()-1 && ans[i] < ans[i+1]) {
				ans[i+1]--;
				i+=2;
			}
			else {
				for(int j = 0; j < i; j++) {
					ans[j] = 9;
				}
				break;
			}
		}
	}

	long long ansl = 0;
	for(int i = ans.size()-1; i >= 0; i--) {
		ansl *= 10;
		ansl += ans[i];
	}

	cout << "Case #" << t << ": ";
	cout << ansl << endl;
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}

	return 0;
}
