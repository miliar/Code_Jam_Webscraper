#include <iostream>
#include <cmath>
#include <string.h>
using namespace std;
int main()
{
	long long a,b;
	int t,num[20],ti=0,top;
	bool c;
	cin>>t;
	while(t--)
	{
		memset(num,0,sizeof(num));
		cin>>a;
		b=a,ti++;
		top=log10(a)+1;
		for(int i=1;b>0;b/=10,i++)num[i]=b%10;
		c=1;
		while(c)
		{
			c=0;
			for(int i=1;i<=top;i++)
			{
				if(num[i]<num[i+1])
				{
					c=1;
					if(num[i]==0)for(int i2=i;i2<top&&num[i2]<1;i2++)num[i2]=9,num[i2+1]--;
					else num[i]--;
					for(int i2=i-1;i2>0;i2--)num[i2]=9;
					if(num[top]==0)top--;
				}
			}
		}
		cout << "Case #"<<ti<<": ";
		for(int i=top;i>=1;i--)cout << num[i];
		cout << "\n";
	}
}
