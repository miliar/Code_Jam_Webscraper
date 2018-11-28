#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <map>

using namespace std;

bool is_tidy(int n) {
	int prev = 9;
	while(n) {
		if(prev < (n%10)) {
			return false;
		}
		prev = (n % 10);
		n /= 10;
	}
	return true;
}

void solve(int n) {
	while(true) {
		if(is_tidy(n)) {
			cout << n << endl;
			return;
		}
		--n;
	}
}

int main() {
	int t = 0;
	cin >> t;
	for(int i = 0; i < t; i++) {
		int n;
		cin >> n;
		cout << "Case #" << (i+1) << ": ";
		solve(n);
	}
	return 0;
}
