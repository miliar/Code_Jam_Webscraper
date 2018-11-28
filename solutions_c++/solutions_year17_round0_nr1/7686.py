#include <bits/stdc++.h>
using namespace std;
int s1[1007];
string s;
int main()
{
	freopen("Input.txt", "r", stdin);
    freopen("Output.out", "w", stdout);
    int t,k,i,j,cas=0;
    scanf("%d",&t);
    while(t--)
    {
    cas++;
    cin>>s;
    scanf("%d",&k);
    for(i=0;i<s.length();i++)
    {
    	if(s[i]=='-')
    	s1[i]=0;
    	else
    	s1[i]=1;
    }
    int c=0,flag=0;
    	for(i=0;i<s.length();i++)
    	{
    		if(s1[i]==1)
    			continue;
    		if(i+k>s.length())
    			break;
			c++;
			int i1=i;
			for(j=1;j<=k;j++)
    		{
    			s1[i1]=s1[i1]^1;
    			i1++;
    		}

    	}
    	for(i=0;i<s.length();i++)
    	{
    		if(s1[i]==0)
    		flag=1;
    	}
    	if(flag==0)
    	{
    		printf("Case #%d: %d\n",cas,c);
    	}
    	else
    		printf("Case #%d: IMPOSSIBLE\n",cas);
    }
}