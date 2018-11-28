#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define vec vector
#define ll long long

int main(void)
{
	int T;
	cin >> T;
	rep(t, T) {
		ll n, k;
		cin >> n >> k;

		cout << "Case #" << t + 1 << ": ";

		int p = 1;
		while(1) {
			if (k < (1LL << p)) break;
			p++;
		}
		k -= (1LL << (p - 1)) - 1;
		ll keep = 1LL << p;
		ll small = (n + 1 - keep) / keep;
		ll num = (n + 1 - keep) % keep;
		if (num > keep / 2) {
			if (k <= num - keep / 2) cout << small + 1 << " " << small + 1 << endl;
			else cout << small + 1 << " " << small << endl;
		} else if (num == keep / 2) {
			cout << small + 1 << " " << small << endl;
		} else {
			if (k <= num) cout << small + 1 << " " << small << endl;
			else cout << small << " " << small << endl;
		}
	}
	return 0;
}

