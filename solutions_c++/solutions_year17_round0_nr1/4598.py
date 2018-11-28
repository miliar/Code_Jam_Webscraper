#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main()
{
    int t,x=1;
    scanf("%i",&t);
    while(t--)
    {
        int n=0,k,c=0,f=1;
        char s[1001];
        scanf("%s%i",&s,&k);
        printf("Case #%i: ",x);
        for(;s[n]!='\0';n++);
        for(int i=0;i<=n-k;i++)
        {
            if(s[i]=='-')
            {
            	c++;
            	for(int j=0;j<k;j++)
            	{
                	if(s[i+j]=='-')
                		s[i+j]='+';
                	else
                		s[i+j]='-';
            	}
            }
        }
        for(int i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
            	f=0;
            	break;
            }
        }
        if(f==0)
        	printf("IMPOSSIBLE\n");
        else
        	printf("%i\n",c);
        x++;
    }
	return 0;
}
