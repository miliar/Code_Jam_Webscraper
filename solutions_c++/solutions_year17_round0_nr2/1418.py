#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ofstream file("Ali.txt.txt");
	int t,i=1;
	cin >> t;
	while (t--){
		file << "Case #" << i << ": ";
		long long n, a, b;
		cin >> n;
		a = 10; b = 1;
		while (a < n)
		{
			long long x = n % b;
			n /= b;
			int d = n % 10;
			if (d == 0)
			{ 
				n--;
				n *= b;
				n += b-1;
			}
			else
			{
				n *= b;
				n += x;
			}
			a *= 10; b *= 10;

		}
		a = 10; b = 1;
		while (a < n)
		{
			long long x = n%a;
			n /= b;
			int d1 = n % 10;
			n /= 10;
			int d2 = n % 10;
			if (d2>d1)
			{
				n--;
				n *= a;
				n += (a - 1);
			}
			else
			{
				n *= a;
				n += x;
			}
			a *= 10; b *= 10;
		}
		file << n << endl;
		i++;
	}
	 system("pause");
}