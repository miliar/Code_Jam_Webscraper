#include<bits/stdc++.h>
using namespace std;

char a[10000];

void flip(int l,int m)
{
	for(int i=l;i<m+1;i++)
		if(a[i] == '+')
			a[i]='-';
		else
			a[i]='+';
}

int main()
{
/*	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
*/	int test;
	cin>>test;
	for(int tt=1;tt<test+1;tt++)
	{
		int k,cnt=0;
		cin>>a>>k;
		for(int i=0;i<strlen(a)-k+1;i++)
		{
			if(a[i]=='-')
			{
				cnt++;
				flip(i,i+k-1);
			}
		}
		for(int i=strlen(a)-k+1;i<strlen(a);i++)
			if(a[i] == '-')
			{
				cnt=-1;
				break;
			}
		cout<<"Case #"<<tt<<": ";
		if(cnt == -1)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<cnt<<"\n";
	}
}
