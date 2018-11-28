#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<array>


using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		char num[20];
		cin>>num;
		int len=strlen(num);
		for(int i=len-1;i>0;--i)
		{
			if(num[i]<num[i-1])
			{
				if(num[i-1]=='0')
				{
					num[i-1]='9';
				}
				else
				{
					num[i-1] -= 1;
				}
				for(int j=i;j<len;j++)
				{
					num[j]='9';
				}
			}
		}
		cout<<"Case #"<<t<<": ";
		for(int i=0;i<len;i++)
		{
			if(num[i]!='0')
			{
				cout<<num[i];
			}
		}
		cout<<endl;
	}
	return 0;
}