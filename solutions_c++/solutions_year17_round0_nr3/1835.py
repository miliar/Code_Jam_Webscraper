#include <iostream>
#include <string>
#include <queue>
#include <math.h>

using namespace std;

unsigned long long ipow(unsigned long long base, int exp)
{
	unsigned long long result = 1ULL;
	while (exp)
	{
		if (exp & 1)
		{
			result *= base;
		}
		exp >>= 1;
		base *= base;
	}
	return result;
}
int main()
{
	int t, ct;
	freopen("a.in", "r", stdin);
	cin >> ct;
	for (t = 1; t <= ct; t++)
	{
		cout << "Case #" << t << ": ";
		unsigned long long n, k, t;

		cin >> n >> k;
		int x;
		for (int i = 0; i < 72; i++) {
			if (ipow(2, i) <= k &&ipow(2, i + 1) > k) {
				x = i;
				break;
			}
		}
		unsigned long long y = ipow(2, x);
		//unsigned long long S = (n+y-1) / y;
		//int d = n - y*S + 1;
		
		unsigned long long d = n %y  + 1;
		unsigned long long S = (n+1-d) / y;
		if (d < k-(y-1)) S = S - 1;
		
		//if (d < k - (y - 1)) S = S - 1;
		if (S%2 == 1) {
			cout << S / 2 << " " << S / 2 << endl;
		}
		else 
		cout << S/2 <<" "<< S/2-1 << endl;
	}
	return 0;
}
