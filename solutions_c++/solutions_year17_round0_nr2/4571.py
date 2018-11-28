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
    	int d[20]={},d1[20]={},size=0;
        long long int n;
        scanf("%lli",&n);
        printf("Case #%i: ",x);
        while(n>0)
        {
        	d[size]=n%10;
        	n/=10;
        	size++;
        }
        for(int i=size-1;i>=0;i--)
        {
        	d1[i]=d[i];
        	if(d1[i+1]>d1[i])
        	{
        		d1[i+1]--;
        		for(int j=i;j>=0;j--)
        		{
        			d1[j]=9;
        		}
        		for(int j=i+1;j<size;j++)
        		{
        			if(d1[j+1]>d1[j])
        			{
        				d1[j]=9;
        				d1[j+1]--;
        			}
        		}
        		break;
        	}
        }
        for(int i=size-1;i>=0;i--)
        {
            if(d1[i]!=0)
            	printf("%i",d1[i]);
        }
        printf("\n");
        x++;
    }
	return 0;
}
