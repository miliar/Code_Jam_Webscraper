#include<bits/stdc++.h>
using namespace std;
int main()
{
    int tcase;
    scanf("%d",&tcase);
    for(int test=1;test<=tcase;test++)
    {
	int k,ans=0;
	int fl=1;
	char s[1234];
	scanf("%s%d",s,&k);
	int len=strlen(s);
	for(int i=0;i<len;i++)
	{
	    if(s[i]=='+')
		continue;
	    if(k+i>len)
		break;
	    int j;
	    for(j=i;j<i+k;j++)
	    {
		if(s[j]=='-')
		    s[j]='+';
		else
		    s[j]='-';
	    }
	    ans++;
	}
	for(int i=0;i<len;i++)
	    if(s[i]=='-')
	    {
		fl=0;
		break;
	    }
	if(fl)
	    printf("Case #%d: %d\n",test,ans);
	else
	    printf("Case #%d: IMPOSSIBLE\n",test);
    }
    return 0;
}
