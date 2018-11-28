#include <iostream>
#include <fstream>
using namespace std;
int istidy(int n)
{
	int tidy;
	for (int k = n; k != 0; k /= 10)
	{
		int d = k % 10;
		int p = (k / 10) % 10;
		if (d >= p)
			tidy = 1;
		else
		{
			tidy = 0;
			break;
		}
	}
	return tidy;
}
void main()
{
	int x, t, i;
	long long int n;
	cin >> t;
	for (x = 1; x <= t; x++)
	{
		cin >> n;
		for (i = n; i >= 1; i--)
			if (istidy(i))
				break;
		cout << "Case #" << x << ": " << i << endl;
	}
	cin.get();
}