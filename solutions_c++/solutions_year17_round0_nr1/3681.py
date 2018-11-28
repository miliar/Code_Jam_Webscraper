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
	FILE *fin = freopen("a-small.in","r",stdin);
	assert(fin!=NULL);
	FILE *fout = freopen("a-output.out","w",stdout);
	int t;
	cin>>t;
	
	for(int k=1;k<=t;k++)
	{
		string s;
		int n,count=0;
		bool flag = true;
		cin>>s>>n;
		f(i,0,s.length()-n+1)
		{
			if(s[i]=='-')
			{
				count++;
				f(j,i,i+n)
				{
					if(s[j]=='-')
					s[j]='+';
					else if(s[j]=='+')
					s[j]='-';
				}
			}
		}
		f(i,0,s.length())
		{
			if(s[i]=='-')
			{
				flag = false;
				break;
			}
		}
		if(flag == true)
		cout<<"Case #"<<k<<": "<<count<<endl;
		else
		cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<endl;
	}
}
