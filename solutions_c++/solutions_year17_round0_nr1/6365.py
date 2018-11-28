#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,tc;
	char s[10000];
	scanf("%d",&t);
	for(tc=1;tc<=t;tc++)
	{
		queue<int>q;
		int k,i,flag=0,unbalanced,c,j,op=0,a[10000],co=0;
		flag=0,unbalanced=0,c=0;
		scanf("%s%d",&s,&k);
		for(i=0;s[i];i++)
		{
			if(s[i]=='-')
			{
				//q.push(i+k);
				flag=1;
				break;
			}
		}
		if(flag==1)
		{
			for(j=0;s[j];j++)
			{
				if(s[j]=='-'&&(q.size()%2==0))
				{
					c++;
					q.push(j+k-1);
				}
				else if(s[j]=='+'&&(q.size()%2!=0))
				{
					c++;
					q.push(j+k-1);
				}
				if(!(q.empty()))
				{
					if(q.front()==j)
						q.pop();
				}
				/*if(unbalanced==0&&s[j]=='+')
					continue;
				if(s[j]=='-'&&unbalanced==0)
				{
					c++;
					unbalanced=k-1;
				}
				else
				{
					if(s[j]==s[j-1])
					{
						unbalanced--;
					}
					else
					{
						unbalanced--;
						c++;
					}
				}*/
			}
			if(q.size()>0)
				printf("Case #%d: IMPOSSIBLE",tc);
			else
				printf("Case #%d: %d\n",tc,c);
		}
		else
		{
			printf("Case #%d: 0\n",tc);
		}
		for(i=0;s[i];i++)
		{

		}
	}
	
	return 0;
}
