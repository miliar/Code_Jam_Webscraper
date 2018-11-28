#include <iostream>
#include <string>
using namespace std;
typedef long long ll;

void output(int num, ll arg1, ll arg2) {
	cout << "Case #" << num << ": " << arg1 << " " << arg2 << endl;
}

void solve(int num, ll n, ll k) {

	int digit = 0; ll tmp_k = k;
	for (; tmp_k != 0; tmp_k >>= 1)digit++;

	int dividor = 1 << (digit - 1);
	int quot = (n - (dividor - 1)) / dividor, rest = (n - (dividor - 1)) % dividor;

	ll k_rest = k - (dividor - 1);

	ll maximum, minimum;
	if (k_rest == 0) {
		maximum = quot + 1; minimum = quot;
	}else if (k_rest <= rest) {
		maximum = quot / 2 + quot % 2; minimum = quot / 2;
	}
	else {
		maximum = (quot - 1) / 2 + (quot + 1) % 2; minimum = (quot - 1) / 2;
	}

	output(num, maximum, minimum);
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		ll n, k;
		cin >> n >> k;
		solve(i, n, k);
	}
}