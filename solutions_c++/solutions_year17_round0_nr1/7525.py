#include<bits/stdc++.h>
#define ll long long int
using namespace std;
FILE *in=freopen("in.txt","r",stdin);
FILE *out=freopen("out.txt","w",stdout);
int main()
{
	int t;
	cin>>t;
	for(int m=1;m<=t;m++)
	{
		string s;
		int k;
		
		cin>>s>>k;
		int sz=s.length();
		int count=0;
		for(int i=0;i<=sz-k;i++)
		{
			if(s[i]=='-')
			{
				count++;
				for(int j=i;j<k+i;j++)
				{
					if(s[j]=='-')
					s[j]='+';
					
					else if(s[j]=='+')
					s[j]='-';
				}
			}
		}
		int flag=0;
		for(int i=0;i<sz;i++)
		{
			if(s[i]=='-')
			flag=1;
		}
		if(flag==1)
		cout<<"Case #"<<m<<": IMPOSSIBLE"<<endl;
		
		else
		cout<<"Case #"<<m<<": "<<count<<endl;
	}
	return 0;
}
