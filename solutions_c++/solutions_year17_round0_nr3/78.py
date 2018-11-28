#include <bits/stdc++.h>

using namespace std;

void runTestCase(int t) {
	long long n, k;
	cin >> n >> k;

	long long y, z;
	if(k == 1) {
		n--;
		y = n - n/2;
		z = n/2;
	}
	else if(k == 2) {
		n--;
		long long l = n - n/2;
		l--;
		y = l - l/2;
		z = l/2;
	}
	else {
		map<long long, long long> ivals;
		ivals[n]++;
		while(k > 0) {
			auto it = ivals.end();
			it--;
			long long ival = it->first;

			long long ct;
			if(it->second < k) {
				k -= it->second;
				ct = it->second;
				it->second = 0;
			}
			else {
				it->second -= k;
				ct = k;
				k = 0;
			}

			if(it->second == 0) {
				ivals.erase(it);
			}

			ival--;
			ivals[ival/2] += ct;
			ivals[ival - ival/2] += ct;
			y = max(ival/2, ival-ival/2);
			z = min(ival/2, ival-ival/2);
		}
	}

	cout << "Case #" << t << ": ";
	cout << y << " " << z << endl;
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}

	return 0;
}
