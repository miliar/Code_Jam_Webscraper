#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define pi pair<int,int>
#define pll pair<ll,ll>
#define vl vector< ll >
#define bug(a) cout<<a<<endl;
#define bug2(a,b) cout<<a<<" "<<b<<endl;
#define bug3(a,b,c) cout<<a<<" "<<b<<" "<<c<<endl;
using namespace std;
bool istidy(char s[])
{
	for(int i=0;s[i+1]!='\0';i++)
	{
		if(s[i]>s[i+1])
			return false;
	}
	return true;	
}
int main()
{
	int test;
	scanf("%d",&test);
	ofstream out("out.txt");
	for(int t=1;t<=test;t++)
	{
		char s[100001];
		scanf("%s",s);
		int len=strlen(s);
		if(istidy(s))
		{
			out<<"Case #"<<t<<": "<<s<<endl;	
		}
		else
		{
			int i;
			for(i=0;s[i+1]!='\0';i++)
			{
				if(s[i]>s[i+1])
					break;
			}
			for(int j=i+1;s[j]!='\0';j++)
				s[j]='9';
			int j;
			for(j=i;j>0;j--)
			{
				if(s[j]!=s[j-1])
					break;
			}
			if(j==0)
			{
				int val=s[0]-'0';
				val-=1;
				s[0]=val+'0';
				for(j=1;j<=i;j++)
					s[j]='9';
			}
			else if(j==i)
			{
				int val=s[j]-'0';
				val-=1;
				s[j]=val+'0';	
			}
			else
			{
				int l=j;
				for(j=j+1;j<=i;j++)
					s[j]='9';
				int val=s[l]-'0';
				val-=1;
				s[l]=val+'0';
			}
			ll res=0;
			for(int i=0;s[i]!='\0';i++)
				res=(res*10)+(s[i]-'0');
			out<<"Case #"<<t<<": "<<res<<endl;
		}
	}
	return 0;
}


