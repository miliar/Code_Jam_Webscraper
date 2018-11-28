#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i,x,l) for(i=x;i<l;i++)
int main()
{
	int t,ctr,i,flips,k,x,fl,j;
	string s;
	cin>>t;
	for(x=1;x<=t;x++)
	{
		cin>>s;
		cin>>k;
		ctr=0,flips=0;
		for(i=0;i<s.length()-k+1;i++)
		{
			if(s[i]=='-')
			{
				for(j=i;j<i+k and j<s.length();j++)
				{
					if(s[j]=='+')s[j]='-';
					else s[j]='+';
				}
				//cout<<flips<<" "<<endl;
				flips++;
			}
		}
		fl=1;
		for(i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				fl=0;
				break;
			}
		}
		if(fl==0)
		{
			printf("Case #%d: IMPOSSIBLE\n",x);
		}
		else printf("Case #%d: %d\n",x,flips);

	}
	return 0;
}