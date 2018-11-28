#include <stdio.h>
#include <string.h>
#include <cstring>
#include <string.h>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	int T, N;
	scanf("%d", &T);
	char* num=new char[20];
	string snum;
	for(int i=1;i<=T;i++)
	{
		cin>>snum;
		int L=snum.length();
		for(int j=0;j<snum.length();j++)
			num[j]=snum[j];
		int j=0;
		
		for(j=1;j<L;j++)
		{
			if(num[j]<num[j-1])
			{
				for(int k=j;k<L;k++)
					num[k]='9';
				bool borrow=true;
				for(int k=j-1;k>=0 && borrow;k--)
				{
					if(num[k]=='0')
						num[k]='9';
					else
					{
						num[k]--;
						if(num[k]<num[k-1])
						{
							num[k]='9';
						}
						else
							borrow=false;
					}
				}
			}
		}
		
		cout<<"Case #"<<i<<": ";
		int k=0;
		while(k<L && num[k]=='0')
			k++;
		if(k==L)
			cout<<0;
		while(k<L)
		{
			cout<<num[k];
			k++;
		}
		cout<<endl;
	}
	return 0;
}
