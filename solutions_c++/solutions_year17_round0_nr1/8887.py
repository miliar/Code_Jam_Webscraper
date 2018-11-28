#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	int z=1;
	while(t--)
	{
		char s[2000];
		int k;
		scanf("%s %d",&s,&k);
		int len=strlen(s);
		int i;
		stack<char>st;
		for(i=len-1;i>=0;i--)
		{
			st.push(s[i]);
		}
		int ans=0;
		bool poss=true;
		while(st.empty()==false)
		{
			if(st.top()=='+')
			st.pop();
			else
			{
				if(k>st.size())
				{
					poss=false;
					break;
				}
				else
				{
					ans+=1;
					stack<char>temp;
					int j;
					for(j=0;j<k;j++)
					{
						if(st.top()=='-')
						{
							temp.push('+');
							st.pop();
						}
						else
						{
							temp.push('-');
							st.pop();
						}
					}
					for(j=0;j<k;j++)
					{
						st.push(temp.top());
						temp.pop();
					}
				}
			}
		}
		if(poss==false)
		{
			printf("Case #%d: IMPOSSIBLE\n",z++);
		}
		else
		{
			printf("Case #%d: %d\n",z++,ans);
		}
	}
	return 0;
}
