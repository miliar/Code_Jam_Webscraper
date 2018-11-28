#include <bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    scanf("%d",&test);
    for(int testnum=1;testnum<=test;testnum++)
    {
	char s[27];
	scanf("%s",s);
	int len=strlen(s);
	for(int i=len-1;i>=1;i--)
	{
	    int u=s[i]-'0';
	    int v=s[i-1]-'0';
	    if(v>u)
	    {
		s[i-1]--;
		s[i]='9';
	    }
	}
	for(int i=0;i<len-1;i++)
	{
	    int u=s[i]-'0';
	    int v=s[i+1]-'0';
	    if(u>v)
		s[i+1]='9';
	}
	if(s[0]=='0')
	    printf("Case #%d: %s\n",testnum,&s[1]);
	else
	    printf("Case #%d: %s\n",testnum,s);
    }
    return 0;
}
