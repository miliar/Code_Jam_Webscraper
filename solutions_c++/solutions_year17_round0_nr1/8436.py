#include<bits/stdc++.h>
using namespace std;

#define Rahul_Vats  jbmr_kkd 

int main()
{
	int test;
	char s[10000];
	scanf("%d",&test);
	for(int i=1;i<=test;i++)
	{
		queue<int> q;
		int k,status=0,c=0;
		scanf("%s%d",&s,&k);
		for(int i=0;s[i];i++)
		{
			if(s[i]=='-')
			{status=1;break;}
		}
		if(status==1)
		{
			for(int j=0;s[j];j++)
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
			}
			if(q.size()>0)
				printf("Case #%d: IMPOSSIBLE\n",i);
			else
				printf("Case #%d: %d\n",i,c);
		}
		else
		{
			printf("Case #%d: 0\n",i);
		}
	}
 
	return 0;
}
