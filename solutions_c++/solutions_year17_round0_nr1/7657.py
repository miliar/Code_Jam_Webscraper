#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("inp.txt","r",stdin);
	freopen("res.txt","w",stdout);
	long long int t,i,k,len,j,x;
	char temp;
	scanf("%lld",&t);
	for(x=1;x<=t;x++)
	{
		string str;
		cin>>str>>k;
		len=str.length();
		char que[len+1];
		long long int st=0,en=0,count=0;
		i=0;
		while(i<len)
		{
			if(st==en)
			{
				if(str[i]=='-')
				{
					que[en]=str[i];
					en++;
				}
				i++;
			}
			else if(en-st==k)
			{
				while(que[st]=='-' && st<en)
				{
					st++;
				}
				for(j=st;j<en;j++)
				{
					if(que[j]=='-')
					{
						que[j]='+';
					}
					else
					{
						que[j]='-';
					}
				}
				count++;
			}
			else
			{
				que[en]=str[i++];
				en++;
			}
		}
		if(en-st==k)
		{
			while(que[st]=='-' && st<en)
			{
				st++;
			}
			for(j=st;j<en;j++)
			{
				if(que[j]=='-')
				{
					que[j]='+';
				}
				else
				{
					que[j]='-';
				}
			}
			count++;
		}
		if(st==en)
		{
			printf("Case #%lld: %lld\n",x,count);
		}		
		else
		{
			printf("Case #%lld: IMPOSSIBLE\n",x);
		}
	}
	return 0;
}
