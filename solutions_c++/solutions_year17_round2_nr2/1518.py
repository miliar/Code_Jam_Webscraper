#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

int main()
{
    int t,x=1;
    scanf("%i",&t);
    while(t--)
    {
    	int n,col[6],f=1,hn,max=0,pos=0;
    	char s[1001],co[6]={'R', 'O', 'Y', 'G', 'B', 'V'};
        scanf("%i",&n);
        hn=n/2;
        for(int i=0;i<6;i++)
        {
        	scanf("%i",&col[i]);
        	if(col[i]>max)
        	{
        		max=col[i];
        		pos=i;
        	}
        	if(col[i]>hn)
				f=0;
			//printf("%i ",col[i] );
       	}
        printf("Case #%i: ",x);
		if(f!=0)
		{
			int i=0,f1=1,comp=1;
			for(int j=pos;comp==1;j=(j+1)%6)
        	{
        		while(col[j]!=0)
       			{
       				s[i]=co[j];
        			col[j]--;
        			i+=2;
        			if(i>=n)
       	   			{
        				f1=0;
       					break;
       				}
       			}
       			if(f1==0)
       				break;
       			comp=0;
       			for(int pp=0;pp<6;pp++)
       			{
       				if(col[pp]!=0)
       				{
       					comp=1;
       					break;
       				}
       			}

       		}
       		i=1,f1=1;
			for(int j=pos;comp==1;j=(j+1)%6)
        	{
        		while(col[j]!=0)
       			{
       				s[i]=co[j];
        			col[j]--;
        			i+=2;
        			if(i>=n)
       	   			{
        				f1=0;
       					break;
       				}
       			}
       			if(f1==0)
       				break;
       			comp=0;
       			for(int pp=0;pp<6;pp++)
       			{
       				if(col[pp]!=0)
       				{
       					comp=1;
       					break;
       				}
       			}
      		}
        	for(int i=0;i<n;i++)
        	{
        		printf("%c",s[i] );
        	}
		}
		else
    		printf("IMPOSSIBLE");
    	printf("\n");
        x++;
    }
	return 0;
}
