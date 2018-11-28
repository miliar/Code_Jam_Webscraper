#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	int t,n,k,test,le,i,count,prev=0,j,flag;
	char str[10000];
	cin>>t;
	for(test=1;test<=t;test++)
	{
		count=0;
		cin>>str>>k;
		le=strlen(str);
		flag=1;
		for(i=0;i<le;i++)
		{
			if(str[i]=='-')
			{
				if((i+k)<=le)
				{
					count++;
					for(j=i;j<(i+k);j++)
						if(str[j]=='+')
							str[j]='-';
						else
							str[j]='+';
				}
				else
				{
					flag=0;
					break;
				}
			}
		}
		if(flag)
			cout<<"Case #"<<test<<":"<<" "<<count<<"\n";
		else
			cout<<"Case #"<<test<<":"<<" IMPOSSIBLE\n";

	}
	return 0;
}