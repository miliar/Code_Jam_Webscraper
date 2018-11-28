#include <iostream>
#include <string>
#include <queue>

using namespace std;

typedef long long ll;

int numbits(ll a) {
	int count = 0;
	while (a > 0) {
		count++;
		a = a >> 1;
	}
	return count;
}

int main() {

	
	int t; cin >> t;
	int cas = 1;
	while (t--) {
		cout << "Case #" << cas << ": ";
		cas++;
		
		ll n, k; cin >> n >> k;

		int tier = numbits(k);
		ll pos = k - (1 << (tier - 1)); // gives zero-indexed position in the tier
		ll sum = (n + 1) - (1 << tier);

		ll upper = n;
		ll lower = n;
		bool bigger = true;
		for (int i = 0; i < tier; i++) {
			if (upper % 2 == 0 && lower % 2 == 1)
				bigger = false;
			if (upper % 2 == 1 && lower % 2 == 0)
				bigger = true;
			lower = (lower - 1) / 2;
			upper = upper / 2;
		}

		if (bigger) {
			ll base = upper + lower;
			ll bigger_count = sum - (1 << (tier - 1)) * (base); // this gives how many in the tier are the larger combination
			if (pos <= bigger_count - 1)
				cout << upper << " " << upper << endl;
			else
				cout << upper << " " << lower << endl;
		}
		else {
			ll base = lower + lower;
			ll bigger_count = sum - (1 << (tier - 1)) * (base);
			if (pos <= bigger_count - 1)
				cout << upper << " " << lower << endl;
			else
				cout << lower << " " << lower << endl;
		}

	}

	return 0;
}