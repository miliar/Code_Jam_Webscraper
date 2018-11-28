#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("x.in","r",stdin);
    freopen("y.txt","w",stdout);
	int t;
	cin>>t;
	for(int kk=1;kk<=t;++kk)
	{
		char s[1010];
		int count=0;
		int k;
		cin>>s>>k;
		int l=strlen(s);
		int i;
		for(i=0;i<l;++i)
		{
			if(s[i]=='-'&&(i+k)>l)
			{
				break;
			}
			if(s[i]=='-')
			{
				++count;
				for(int j=i;j<i+k;++j)
				{
					if(s[j]=='-')
					{
						s[j]='+';
					}
					else if(s[j]=='+')
					{
						s[j]='-';
					}
				}
			}
		}
		if(i!=l)
		{
			cout<<"Case #"<<kk<<": IMPOSSIBLE\n";
		}
		else
		{
			cout<<"Case #"<<kk<<": "<<count<<"\n";
		}
	}
	return 0;
}
