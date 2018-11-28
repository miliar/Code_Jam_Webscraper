#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <map>

using namespace std;

map<long long, long long> m;

void f(long long n, long long k)
{
	m.clear();
	m[n - n] = 1;

	while (k)
	{
		for (auto &el : m) {
			long long x1 = (n - el.first) / 2;
			long long x2 = (n - el.first - 1) / 2;

			if (el.second >= k) {
				cout << x1 << " " << x2 << endl;
				return;
			}
			else {
				k -= el.second;
				m[n - x1] += el.second;
				m[n - x2] += el.second;
				m.erase(el.first);
			}
			break;
		}
	}
	cout << "aaa" << endl;
}

void solve()
{
	long long n, k;
	cin >> n >> k;
	f(n, k);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		clock_t start = clock();
		printf("Case #%d: ", test);
		solve();
		clock_t finish = clock();
		cerr << "Test" << test << ": " << (finish - start + .0) / CLOCKS_PER_SEC << endl;
	}


	return 0;
}