#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int test,n;
char str[20];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("q2.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		printf("Case #%d: ",kk);
		cin>>str;
		n=strlen(str);
		int flag=1,now=0;
		for (int i=0;i<n-1;i++)
		{
			if (str[i]<str[i+1]) now=i+1;
			else if (str[i]>str[i+1]) {flag=0;break;}
		}
		if (flag) cout<<str;
		else 
		{
			if (now==0&&str[0]=='1') for(int i=0;i<n-1;i++) printf("9");
			else 
			{
				for (int i=0;i<now;i++) printf("%c",str[i]);
				printf("%c",str[now]-1);
				for (int i=now+1;i<n;i++) printf("9");
			}
		}
		cout<<endl;
	}
}
