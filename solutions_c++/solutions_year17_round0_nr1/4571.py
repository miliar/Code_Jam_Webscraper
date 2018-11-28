#include "bits/stdc++.h"
using namespace std;
typedef long long ll;

int main()
{
	int t;
	cin>>t;
	for(int case1=1;case1<=t;case1++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int c=0;
		for(int i=0;i<=s.size()-k;i++)
		{
			if(s[i]=='-')
			{
				c++;
				for(int j=i;j<=i+k-1;j++)
				{
					if(s[j]=='-')s[j]='+';
					else s[j]='-';
				}
		    }

		}
		bool ok=true;
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='-')ok=false;
		}
		printf("Case #%d: ",case1);
		if(ok)printf("%d\n",c);
		else printf("IMPOSSIBLE\n");
	}

	return 0;
}
