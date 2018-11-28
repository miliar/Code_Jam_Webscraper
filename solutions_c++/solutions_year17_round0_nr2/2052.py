#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("output.txt", "w", stdout);
	char str[25];
	int t;
	cin>>t;
	int l=1;
	while(l<=t)
	{
		cin>>str;
		int len = strlen(str);
		int i;
		for(i=0;i<len-1;i++)
		{
			if(str[i]>str[i+1])
				break;
		}
		if(i==len-1)
		{
			cout<<"Case #"<<l<<": "<<str<<endl;
			l++;
			continue;
		}
		for(int k=i+1;k<len;k++)
		{
			str[k]='9';
		}
		while(i>0&&str[i]==str[i-1])
		{
			str[i]='9';
			i--;
		}
		if(str[i]=='1')
			str[i] = '-';
		else str[i] = str[i]-1;
		cout<<"Case #"<<l<<": ";
		if(str[0]=='-')
		for(int i=1;i<len;i++)
			cout<<str[i];
		else cout<<str;
		cout<<endl;
		l++;
	}
}
