#define ull unsigned long long
#include <iostream>

using namespace std;

ull T, n, k;

ull r1, r2;

ull getpow(ull _n)
{
	ull r = 1LL;
	while (_n >= r) r *= 2LL;
	return r;
}
void solve()
{
	ull pw = getpow(k);
	ull dist = k - (pw / 2LL);
	r1 = r2 = n / pw;
	if (dist > (n % pw)) r1--;
	if (dist + (pw / 2LL) > (n%pw)) r2--;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> n >> k;
		solve();
		cout << "Case #" << i << ": " << r1 << " " << r2 << "\n";
	}
	return 0;

}