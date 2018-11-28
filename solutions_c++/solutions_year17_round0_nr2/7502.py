#include<bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin>>t;

	long long n;
	for(int tc = 1; tc <= t; tc++)
	{
		cin>>n;
		long long temp = n;
		int d = 0, digits[20];
		while(temp > 0)
		{
			digits[d++] = temp%10;
			temp /= 10;
		}
		int s = -1, x;
		for(int i = d-2; i >= 0; i--)
		{
			if(digits[i] < digits[i+1])
			{
				s = i+1;
				break;
			}	
		}
		if(s != -1)
		{
			x = s;
			for(int j = s+1; j < d; j++)
			{
				if(digits[j] != digits[s])
				{
					x = j;
					break;
				}
			}
			if(x == s)
				x = d;
			if(x != -1)
			{
				x--;
				digits[x]--;
				for(int i = x-1; i >= 0; i--)
					digits[i] = 9;
			}
		}

		cout<<"Case #"<<tc<<": ";
		for(int i = d-1; i >= 0; i--)
		{
			if(digits[i] != 0)
			{
				s = i;
				break;
			}
		}
		for(int i = s; i >= 0; i--)
			cout<<digits[i];
		cout<<endl;
	}

	return 0;
}