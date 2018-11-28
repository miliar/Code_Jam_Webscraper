#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int t, n;
	double d, st, hsp, ht, slow = 0, asp;
	cin >> t;
	for(int c = 1; c <= t; c++)
	{
		slow = 0;
		cin >> d >> n;
		for(int i = 0; i < n; i++)
		{
			cin >> st >> hsp;
			ht = (d - st) / hsp;
			if(ht > slow)
			{
				slow = ht;
			}
		}
		printf("Case #%d: %.6lf\n", c, d / slow);
	}
}
