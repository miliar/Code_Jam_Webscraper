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
    	long long int n,d,k[1000],s[1000];
    	double ans;
        scanf("%lli%lli",&d,&n);
        printf("Case #%i: ",x);
        for(int i=0;i<n;i++)
        {
        	scanf("%lli%lli",&k[i],&s[i]);
        }
        ans=(double)(d*s[0])/(d-k[0]);
        for(long long int i=1;i<n;i++)
        {
        	//printf("%lf ",ans );
        	double x=(double)(d*s[i])/(d-k[i]);
        	if(x<ans)
        		ans=x;
        }
    	printf("%lf\n",ans);
        x++;
    }
	return 0;
}
