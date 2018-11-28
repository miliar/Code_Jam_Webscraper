#include<iostream>
using namespace std;
const int N=1e3+100;
char s[N];
int main()
{
	int t,k,len;
	//cin>>t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%s%d",s,&k);
		len=strlen(s);
		int ctr=0;
		for(int j=0;j+k-1<len;j++)
		{
			if(s[j]=='-')
			{
				ctr++;
				for(int x=j;x<j+k;x++)
				{
					if(s[x]=='+')
						s[x]='-';
					else
						s[x]='+';
				}
			}
		}
		int fl=1;
		for(int j=0;j<len;j++)
		{
			if(s[j]=='-')
			{
				fl=0;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(fl)
			cout<<ctr<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
	}
	return 0;
}