#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
typedef long long int ll;
int main()
{
	int t;
	scanf("%d",&t);
	int i;
	for(i=1;i<=t;i++)
	{
		ll n;
		scanf("%lld",&n);
		ll temp = n;
		string s;
		while(temp>0)
		{
			int val = temp%10;
			char ch = (char)val + 48;
			s.push_back(ch);
			temp = temp/10;
		}
		ll size = s.length();
		ll pos = size;
		ll j;
		for(j=0;j<(size/2);j++)
		{
			char temp = s[j];
			s[j] = s[size-j-1];
			s[size-j-1] = temp;
		}
		for(j=size-2;j>=0;j--)
		{
			if(s[j]>s[j+1])
			{
				if(s[j]!='0')
				{
					s[j]--;
				}
				pos = j+1;
			}
		}
		ll k = 0;
		for(j=pos;j<size;j++)
		{
			s[j] = '9';
		}
		for(j=0;j<size;j++)
		{
			if(s[j]!='0')
			{
				k = j;
				break;
			}
		}
		printf("Case #%d: ",i);
		for(j=k;j<size;j++)
		{
			cout<<s[j];
		}
		cout<<endl;
	}
	return 0;
}