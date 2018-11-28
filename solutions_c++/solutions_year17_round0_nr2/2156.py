#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

int v[30], lg;
long long n;

int main()
{
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		cin >> n;

		lg = 0;
		while (n != 0)
			v[++lg] = n % 10, n /= 10;

		int poz;
		for (poz = lg - 1; poz >= 1; poz--)
			if (v[poz] < v[poz + 1])
				break;

		if (poz != 0)
		{
			for (int i = 1; i <= poz; i++)
				v[i] = 9;

			v[++poz] --;
			while (v[poz] < v[poz + 1] && poz < lg)
				v[poz] = 9, v[++poz] --;

			while (v[lg] == 0)
				lg--;
		}

		cout << "Case #" << i << ": ";
		for (int i = lg; i >= 1; i--)
			cout << v[i];
		cout << '\n';
	}
	cin >> n;
	return 0;
}