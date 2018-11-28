#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s;
	int t,i,ans=0,k,j,flag,x=0;
	scanf("%d",&t);
	while(t--)
	{
		cin >> s>>k,ans=0,flag=1;
		for(i=0;i<s.size();)
		{
			while(i<s.size() && s[i]=='+') i++;
			if(i>s.size()-k) break;
			for(j=0;j<k;j++)
			{
				if(s[i+j]=='+') s[i+j]='-';
				else s[i+j]='+';
			}
			ans++;
		}
		while(i<s.size())
			if(s[i++]=='-') flag=0;
		if(flag) printf("Case #%d: %d\n",++x,ans);
		else printf("Case #%d: IMPOSSIBLE\n",++x);
	}
	
} 
