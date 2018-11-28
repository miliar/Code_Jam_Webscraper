#include <bits/stdc++.h>
using namespace std;

#define endl "\n"

vector <int> num;
int64_t r;

bool init_check() {
	int s = num.size();
	for(int i = 0; i < s - 1; i++) {
		if(num[i] > num[i+1]) return false;
	}
	return true;
}

void solve(int64_t n) {
	// filling the digits in a vector
	num.clear();
	while(n) {
		r = n % 10;
		n /= 10;
		num.push_back(r);
	}
	
	r = num.size();
	if(r == 1) {
		cout << num[0] << endl;
		return;
	}

	reverse(num.begin(), num.end());
	if(init_check()) {
		for(int i = 0; i < r; i++) {
			cout << num[i];
		}
		cout << endl;
		return;
	}

	for(int i = r-1; i > 0; i--) {
			while (num[i] < num[i-1] && num[i-1] > 0) {
				num[i-1]--;
				num[i] = 9;
			}
	}

	while(!init_check()){
		for(int i = r-1; i > 0; i--) {
			while (num[i] < num[i-1] && num[i-1] > 0) {
				num[i] = 9;
			}
		}
	}

	// passing through the leading 0s
	int i = 0;
	while(num[i] == 0) {
		i++;
	}

	// the actual number
	for(i; i < r; i++) {
		cout << num[i];
	}
	cout << endl;
}

int main() {
	ios_base :: sync_with_stdio(false);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	int64_t n;
	cin >> t;

	for(int z = 1; z <= t; z++) {
		cin >> n;
		cout << "Case #" << z << ": ";
		solve(n);
	}
}
