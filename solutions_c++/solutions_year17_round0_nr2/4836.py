#include<iostream>
#include <string.h>
using namespace std;
int main()
{
	int t;
	long long int n;
	cin>>t;
	int digits[20];
	int ans_digit[20];
	for(int ti =1;ti<=t;ti++)
	{
		cin>>n;
		for(int i=0;i<20;i++)
		{
			digits[i] = 0;
			ans_digit[i] = 0;
		}
		int j = 0;
		while(n)
		{
			digits[j] = n%10L;
			n=n/10L;
			j++;
		}
		int latest_index = 19;
		int k = 0;
		for( k = 19;k>0;k--)
		{
			if(digits[k] < digits[ k-1 ] )
			{
				latest_index = k;
				ans_digit[k] = digits[k];
			}				
			else if( digits[k] == digits[ k-1 ] )
				ans_digit[k] = digits[k];
			else
			{
				ans_digit[latest_index-1] = digits[latest_index-1] - 1;
				for(k=latest_index-2;k>=0;k--)
					ans_digit[k] = 9;
			}
		}
		if( k == 0 )
			ans_digit[0] = digits[0];
		long long int ans = 0;
		long long int mult = 1;
		for(k=0;k<19;k++)
		{
			ans += ans_digit[k]*mult;
			mult *=10L;
		}
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
	return 0;
}