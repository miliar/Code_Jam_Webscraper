#include <iostream>
#include <vector>
#include <string>
#define ll long long int
using namespace std;


int main()
{
	iostream::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		int d, n;
		cin >> d >> n;
		vector<double> hor(n);
		double max = 0;
		for (int i = 0; i < n; i++)
		{
			int a, b;
			cin >> a >> b;
			int tg = d - a;
			hor[i] = (double)(d - a) / (double)b;
			if (hor[i] > max) {
				max = hor[i];
			}
		}
		cout << "Case #" << q+1 << ": " << fixed << d/max << "\n";

	}
	return 0;
}

