#include <iostream>
#include <cstdio>
using namespace std;
string s;
int t, k, wyn=0;
int main()
{
	ios_base::sync_with_stdio(0);
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		cin>>k;
		wyn=0;
		for(int j=0;j<=s.size()-k;j++)
		{
			if(s[j]=='-')
			{
				wyn++;
				for(int h=j;h<j+k;h++) 
				if(s[h]=='-') s[h]='+';
				else s[h]='-';
			}
		}
		bool czy=1;
		for(int j=s.size()-k+1;j<s.size();j++) if(s[j]=='-') czy=0;
		printf("Case #%d: ", i);
		if(czy) printf("%d", wyn);
		else printf("IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}
