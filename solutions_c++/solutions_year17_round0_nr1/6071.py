#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("file.txt", "r", stdin);
    freopen("file1.txt", "w", stdout);
	int t,k;
	char s[1003];
	cin>>t;
	for(int T=1;T<=t;++T)
	{
		cin>>s>>k;
		int n=strlen(s),cnt=0;
		
		printf("Case #%d: ",T);
		for(int i=0;i<=n-k;++i)
		{
			if(s[i]=='-'){
			cnt++;
			for(int j=i;j<k+i;++j)
			{
				
				if(s[j]=='-')
				s[j]='+';
				else
				s[j]='-';
			}
		  }
			
		}
		int flag=1;
		for(int i=0;i<n;++i)
		if(s[i]=='-')
		flag=0;
		
		if(flag)
		{
			printf("%d\n",cnt);
		}
		else
		printf("IMPOSSIBLE\n");
		
		
		
		
		
	}
	
	
	return 0;
}
