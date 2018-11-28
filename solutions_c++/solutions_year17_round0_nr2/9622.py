#include <iostream>

using namespace std;


int main()
{
	int t;
	long long n;
	cin >> t;

	for(int i=1; i<=t; ++i)
	{
		cin >> n;
		long long m=n, result=0;

		int dj=9;
		long long ten=1;
		for(int j=0; j<=18; ++j)
		{
			if (m==0) break;
			if (m%10 > dj)
			{
				result = ten-1;
				dj = m%10 - 1;
				result+=dj*ten;
			}
			else
			{
				dj=m%10;
				result += ten*dj;
			}
			ten*=10;
			m/=10;
		}

		cout << "Case #" << i << ": " << result << endl;
	}
}
