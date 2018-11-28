#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;

bool increasing(ull n) {
	vector<int> v;
	int a, f;
	while(n) {
		a = n%10;
		n /= 10;
		v.push_back(a);
	}
	reverse(v.begin(),v.end());
	return is_sorted(v.begin(), v.end());
}

ull solve(ull n) {
	while(n) {
		if(increasing(n)) return n;
		n--;
	}
	return 0;
}

int a, i;
ull n;
int main() {
	cin >> a;
	i = 0;
	while(a--) {
		cin >> n;
		printf("Case #%d: ",++i);
		cout << solve(n) << endl;
	}
	return 0;
}
