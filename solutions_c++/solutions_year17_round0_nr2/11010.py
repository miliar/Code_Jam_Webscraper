#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	int T;
	int t;
	long long int N;
	long long int mult;
	int digits_n[18];
	int digits_a[18];
	long long int answer;
	
	cin >> T;
	
	for (t=0;t<T;t++)
	{
		cin >> N;
		answer = 0;
		mult = 1;
		for (int i=0;i<18;i++)
		{
			digits_n[i] = N%10;
			N = N/10;
			digits_a[i] = 0;
		}
		
		for (int i=0;i<17;i++)
		{
			if ( digits_n[i] < digits_n[i+1] )
			{
				for (int j=0;j<=i;j++)
				{
					digits_a[j] = 9;
				}
				digits_n[i+1] = digits_n[i+1]-1;
			}
			else
			{
				digits_a[i] = digits_n[i];
			}
		}		
		cout << "Case #" << t+1 << ": ";
		bool bZeroes = true;
		for (int i=17;i>=0;i--)
		{
			if ( bZeroes )
			{
				if ( digits_a[i] > 0 )
				{
					bZeroes = false;
					cout << digits_a[i];
				}
			}
			else
			{
				cout << digits_a[i];
			}
		}
		cout << endl;
		
	}
		
	return 0;
}