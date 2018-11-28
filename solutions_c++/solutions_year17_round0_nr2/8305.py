#include <iostream>
#include <map>
#include <math.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	int Case = 1;
	while( t--)
	{
		long long int n;
		cin >> n;
		map<int, int> num;
		int digits = floor( log10( n ) );
		int d = 0;
		while( n)
		{
			num[digits-d] = n%10;
			n /=10;
			d++;
		}
		bool started = false;
		for( int i = 0; i < d-1; i++)
		{
			if( i < d-1)
			{
				if( num[i] > num[i+1])
				{
					num[i]--;
					for( int j = i+1; j < d; j++)
						num[j] = 9;
					i = -1;
				}
			}
		}
		int i = 0;
		while( !num[i])
			i++;
		cout << "Case #" << Case++ << ": " ;
		for( ; i < d; i++)
			cout << num[i];
		cout << endl;
	}
	return 0;
}