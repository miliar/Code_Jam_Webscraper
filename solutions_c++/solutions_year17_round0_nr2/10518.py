#include<bits/stdc++.h>
using namespace std;
int main ()
{
	long long arr[1005];
	long long ans = 0, mx;
	for (long long i=1;i<=1000;i++)
	{
		long long temp, digit;
		temp = i;
		digit = temp%10;
		while (temp >= 1)
		{
			if (temp%10 <= digit)
			{
				digit = temp%10;
				temp = temp/10;
			}
			else 
			{
				temp = -1;
			}
		}
		if (temp != -1) arr[i] = i;
		else arr[i] = arr[i-1];
	}
	long long T, N;
	cin >> T;
	for (long long i=1;i<=T;i++)
	{
		cin >> N;
		printf("Case #%lld: %lld\n", i, arr[N]);
	}
	return 0;
}