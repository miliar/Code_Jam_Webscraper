#include<bits/stdc++.h>
using namespace std;
long long t,tt,i,n,hs;
bool b;
string s;
void wow(long long wi, long long wn)
{
	long long ii;
	for(ii=wi;ii<wi+n;ii++)
	{
		if(s[ii]=='+')
			s[ii]='-';
		else
			s[ii]='+';
	}
}
int main()
{
	freopen("q17ain.txt","r",stdin);
	freopen("q17aout.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		tt++;
		cin>>s>>n;
		b=1;
		hs=0;
		for(i=0;i<=s.length()-n;i++)
		{
			if(s[i]=='-')
			{
				wow(i,n);
				hs++;
			}
			//cout<<s<<endl;
		}
		for(i=s.length()-n+1;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				b=0;
				break;
			}
		}
		if(b==0)
		{
			printf("Case #%lld: IMPOSSIBLE\n",tt);
		}
		else
		{
			printf("Case #%lld: %lld\n",tt,hs);
		}
	}
}
