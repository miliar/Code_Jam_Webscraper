#include <bits/stdc++.h>

using namespace std;

string s;
int T,k,res,cas;

int main()
{
	for(cin>>T;T--;)
	{
		cin>>s>>k,res=0;
		int n=s.length();

		for(int i=0;i+k<=n;i++)
			if(s[i]=='-')
			{
				res++;
				for(int j=i;j<i+k;j++)
					s[j]=(s[j]=='+')?'-':'+';
			}

		for(int i=0;i<n;i++)
			if(s[i]=='-')
			{
				res=-1;
				break;
			}
		printf("Case #%d: ",++cas);

		if(res==-1)
			puts("IMPOSSIBLE");
		else
			cout<<res<<endl;
	}
}