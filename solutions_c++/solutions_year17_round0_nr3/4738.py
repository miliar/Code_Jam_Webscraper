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
    	int n,k,a[1000000],y,z,b[1000001]={},small=1000000000,pos=0,at=1;
        scanf("%i%i",&n,&k);
        printf("Case #%i: ",x);
        a[0]=n;
        b[n]=1;
        for(int i=0;i<k-1;i++)
        {
        	int r=a[pos];
        	b[r]--;
        	if(b[r]==0)
        		pos++;
        	int p=(r-1)/2;
        	int q=r-1-p;
        	b[p]++;
        	b[q]++;
        	if(q<small)
        	{
        		small=q;
        		a[at]=q;
        		at++;
        	}
        	if(p<small)
        	{
        		small=p;
        		a[at]=p;
        		at++;
       		}

        	//printf("%i ",a[i]);
        }
        z=(a[pos]-1)/2;
        y=a[pos]-1-z;
        printf("%i %i\n",y,z);
        x++;
    }
	return 0;
}
