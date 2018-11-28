#include<bits/stdc++.h>
using namespace std;
#define ll unsigned long long
int main()
{
	ll t;
	scanf("%llu",&t);
    for(ll tt=1;tt<=t;tt++)
    {
    	char a[25];
    	scanf("%s",a);
    	int l=strlen(a);
    	for(int i=l-1;i>=1;i--)
    	{
    		if(a[i]<a[i-1])
    		{
    			a[i]='9';
    			a[i-1]=(char)((int)a[i-1]-1);
			}
			
		}
		for(int i=1;i<l-1;i++)
		{
			if(a[i]=='9')
			  a[i+1]='9';
			
		}
		printf("Case #%d: ",tt);
	    for(int i=0;i<l;i++)
	    {
	    	if(a[i]=='0')
	    	continue;
	    	else
	    	printf("%c",a[i]);
		}
		printf("\n");
	}
	
	return 0;
}