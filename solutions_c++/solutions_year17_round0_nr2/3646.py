#include<bits/stdc++.h>
#define T() int t; cin>>t; while(t--)
#define f(i,start,lim) for(long long i=start;i<lim;i++)
#define ll long long
#define YES printf("YES\n")
#define NO printf("NO\n")
#define MOD 1000000007
#define MAX 9001
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		string s;
		cin>>s;
		f(i,0,s.length()-1)
		{
			if(s[i]>s[i+1] )
			{
				while(i>=0 && s[i]==s[i-1])
				{
					i--;
				}
				s[i]=s[i]-1;
				f(j,i+1,s.length())
				{
					s[j]='9';
				}
				
				break;
			}
		}
		int i=0;
		while(s[i]=='0')
		{
			i++;
		}
		cout<<"Case #"<<k<<": ";
		for(;i<s.length();i++)
		cout<<s[i];
		cout<<endl;
	}
}
