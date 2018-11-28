#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <bitset>
#include <string>
#include <vector>
#include <iomanip>
#include <gmpxx.h>

using namespace std;


void solve(int _case) {
	cout << "Case #" << _case << ": ";
	mpf_class d, n;
	
	// il tempo massimo di arrivo!
	mpf_class maxT = 0;
	for(cin >> d >> n; n > 0; --n) {
		mpf_class k, s, t;
		cin >> k >> s;
		t = (d-k)/s;
		maxT = max(maxT, t);
	}
	
	d /= maxT;
	
	cout << fixed << setprecision(6) << d << endl;
}

int main() {
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i)
		solve(i);
}
