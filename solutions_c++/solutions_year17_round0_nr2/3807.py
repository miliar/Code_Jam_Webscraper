#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
	lli t,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		char str[21];
		cin>>str;
		int i,k,l;
		for(i=0;i<strlen(str)-1;i++)
		{
			if(str[i]>str[i+1])
			{
				char ch=str[i];
				for(l=i;l>=0;l--)
				{
					if(str[l]==ch)
					continue;
					else
					break;
				}
				l++;
				str[l]=str[l]-1;
				for(k=l+1;k<strlen(str);k++)
				str[k]='9';
				break;
			}
		}
		if(str[0]=='0')
		i=1;
		else
		i=0;
		cout<<"Case #"<<j<<": ";
		for(;i<strlen(str);i++)
		cout<<str[i];
		cout<<endl;
	}
	return 0;
}
