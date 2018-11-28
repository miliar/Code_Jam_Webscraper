#include <iostream>
#include <cstdio>

using namespace std;

const int MAX_N = 1000;

void Solve()
{
	int d, n, k[MAX_N], s[MAX_N];	
	int i, j;
	double h, max_hours;

	cin >> d >> n;
	for (i = 0; i < n; i++)
		cin >> k[i] >> s[i];

	for (i = 0; i < n; i++)
		for (j = i + 1; j < n; j++)
			if (k[i] < k[j])
			{
				swap(k[i], k[j]);
				swap(s[i], s[j]);
			}

	max_hours = (double)(d - k[0]) / s[0];
	for (i = 1; i < n; i++)
	{
		h = (double)(d - k[i]) / s[i];
		if (max_hours < h)
			max_hours = h;
	}

	printf("%f", d / max_hours);
}

int main()
{
	int T;
	cin >> T;
	for (int now = 1; now <= T; now++)
	{
		cout << "Case #" << now << ": ";
		Solve();
		cout << endl;
	}
	return 0;
}