#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	int t,i,j,test,len;
	cin>>t;
	char str[100];
	for(test=1;test<=t;test++)
	{
		cin>>str;
		len=strlen(str);
		for(i=0;i<len-1;i++)
		{
			if(str[i]>str[i+1])
			{
				str[i]=str[i]-1;
				for(j=i+1;j<len;j++)
				{
					str[j]='9';
				}

			
				j=i;
				while(str[j]<str[j-1] && j>0)
				{
					str[j]='9';
					str[j-1]-=1;
					j--;
				}
				break;
			}
		}
		
		cout<<"Case #"<<test<<": ";
		if(str[0]!='0')
			cout<<str[0];
		for(i=1;i<len;i++)
			cout<<str[i];
		cout<<"\n";

	}
	return 0;
}