#include <iostream>
#include <string>

using namespace std;

typedef unsigned long long ull;

int main()
{
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++)
	{
		ull N, K;
		cin >> N >> K;
		
		ull n = N, c1 = 1, c2 = 0, r1, r2;
		
		while (true)
		{
			if (K <= c1)
			{
				r1 = n / 2;
				r2 = (n - 1) / 2;
				break;
			}
			K -= c1;
			
			if (K <= c2)
			{
				r1 = (n - 1) / 2;
				r2 = (n - 2) / 2;
				break;
			}
			K -= c2;
			
			if (n % 2)
				c1 = 2 * c1 + c2;
			else
				c2 = 2 * c2 + c1;

			n /= 2;
		}
			
		cout << "Case #" << t << ": " << r1 << " " << r2 << "\n";
	}
	
	return 0;
}

