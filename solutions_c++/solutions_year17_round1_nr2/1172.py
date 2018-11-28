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
    	int n,p,need[50],aq[50][50],c=0,pos[50]={};
        scanf("%i%i",&n,&p);
        printf("Case #%i: ",x);
        for(int i=0;i<n;i++)
        {
        	scanf("%i",&need[i]);
        }
        for(int i=0;i<n;i++)
        {
        	for(int j=0;j<p;j++)
        	{
        		scanf("%i",&aq[i][j]);
        	}
        }
        for(int i=0;i<n;i++)
        {
        	sort(aq[i],aq[i]+p);
        }
        /*for(int i=0;i<n;i++)
        {
        	for(int j=0;j<p;j++)
        	{
        		printf("%i ",aq[i][j]);
        	}
        	printf("\n");
        }*/
        for(int k=0;k<p;k++)
        {
        	int f=0;
			for(int z=aq[0][k]/(need[0]*1.1);z<=(aq[0][k]/(need[0]*0.9))+1;z++)
			{
			//printf("%i %i %i\n",aq[0][k],z,f);
			if(aq[0][k]>=0.9*(need[0]*z)&&aq[0][k]<=1.1*(need[0]*z))
			{
				int f1=1;
				//printf("%i %i %i\n",aq[0][k],z,f);
				for(int i=1;i<n;i++)
        		{
        			int f2=0;
        			for(int j=pos[i];j<p;j++)
        			{
        				if(aq[i][j]>=0.9*(need[i]*z)&&aq[i][j]<=1.1*(need[i]*z))
        				{
							f2=1;
							pos[i]=j+1;
							break;
        				}
	        		}
	        		if(f2==0)
	        		{
	        			f1=0;
	        			break;
	        		}
    	    	}
    	    	if(f1==1)
    	    	{
    	    		f=1;
    	    		//printf("%i\n",need[0]*z );
    	    		c++;
    	    	}
    	    	//printf("%i %i\n",aq[0][k],f);
			}
			if(f==1)
				break;
			}
    	}
    	printf("%i\n",c);
        x++;
    }
	return 0;
}
