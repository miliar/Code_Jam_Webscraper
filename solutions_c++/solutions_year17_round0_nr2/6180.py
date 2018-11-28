#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
  	freopen("output1.txt", "w", stdout);
/*	int m=0,a[1000];
	for(int i=1;i<=10000;i++)
	{
		int x=i;
		int j=0,s[50];
		while(x!=0)
		{
			s[j++]=x%10;
			x=x/10;
		}
		int f=0;
		for(int k=0;k<j-1;k++)
		{
			if(s[k]<s[k+1])
			{
				f=1;
				break;
			}
		}
		if(f==0)
		{
			a[m++]=i;
		}
	}
	for(int i=0;i<m;i++) cout << a[i] << " ";
*/
	int t;
	cin >> t;
	for(int j=1;j<=t;j++)
	{
		char s[20];
		scanf("%s",s);
		cout << "Case #" << j << ": ";
		for(int i=0;i<strlen(s)-1;i++)
		{
			if(s[i]>s[i+1])
			{
				s[i]--;
				for(int j=i+1;j<strlen(s);j++)
				{
					s[j]='9';
				}
				i=-1;
			}
		}
		int f=0;
		for(int i=0;i<strlen(s);i++)
		{
			if(s[i]=='0'&&f==0)
				continue;
			else
			{
				f++;
				cout << s[i];
			}
		}
		cout << endl;
	}
	return 0;

}

