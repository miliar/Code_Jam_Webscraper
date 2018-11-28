#include<bits/stdc++.h>
using namespace std;
#define ll unsigned long long
int main()
{
	int t;
	scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
    	char s[1005];
    	scanf("%s",s);
    	int k;
    	scanf("%d",&k);
    	int l=strlen(s);
    	int st;
    	int end;
    	int flag=0;
    	int count=0;
    	for(int i=0;i<l;i++)
    	{
    		if(s[i]=='+')
    		continue;
    		st=i;
    		end=st+(k-1);
    		if(end>=l)
    		{
    			flag=1;
    			break;
			}
			count++;
    		for(int j=st;j<=end;j++)
    		{
    			if(s[j]=='-')
    			s[j]='+';
    			else
    			{		
				s[j]='-';
			    }
			}
		}
		if(flag==0)
    	printf("Case #%d: %d\n",tt,count);
    	else
    	printf("Case #%d: IMPOSSIBLE\n",tt);
	}
	
	return 0;
}