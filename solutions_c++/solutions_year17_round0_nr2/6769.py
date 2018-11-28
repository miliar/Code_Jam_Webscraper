#include <bits/stdc++.h>

using namespace std;

#define LL long long

int main()
{
	ios::sync_with_stdio(false);
	vector<int> digit;
	int t;
	cin>>t;
	for(int cs = 1; cs <= t; cs++)
	{
		LL n;
		cin>>n;
		LL res = 0;
		digit.clear();
		while(n>0)
		{
			digit.push_back(n%10);
			n/=10;
		}
		int len = digit.size(), carry = 0, pos=-1;
		for(int i=0;i<len;i++)
		{
			digit[i] += carry;
			carry = 0;
			if(digit[i]<0)
			{
				pos = i;
				carry = -1;
				continue;
			}
			for(int j=i+1;j<len;j++)
			{
				if(digit[i] < digit[j])
				{
					pos = i;
					carry = -1;
					break;
				}
			}
		}
		for(int i=len-1;i>=0;i--)
		{
			if(i>pos)
			{
				res = res * 10 + digit[i];
			}
			else
			{
				res = res * 10 + 9;
			}
		}
		cout<<"Case #"<<cs<<": "<<res<<'\n';
	}
	return 0;
}
