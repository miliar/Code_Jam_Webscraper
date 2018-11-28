#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	cin>>T;
	
	for (int t=1;t<=T;t++)
	{
		string S;
		cin>>S;
		
		int len;
		cin>>len;
		
		int i,move=0,j;
		
		for (i=0;i<=S.size()-len;i++)
		{
			if(S[i]=='-')
			{
				for (j=i;j<i+len;j++)
				{
					if(S[j]=='+')
					S[j]='-';
					
					else S[j]='+';
				}
				move++;
			}
			
		}
		
		int ok=1;
		for (i=0;i<S.size();i++)
		{
			if(S[i]=='-')
			{
				ok=0;
			}
		}
		
		if(!ok)
		{
			printf("Case #%d: IMPOSSIBLE\n",t);
		}
		
		else
		{
			printf("Case #%d: %d\n",t,move);
		}
		
		
	}
	
	
	
}
