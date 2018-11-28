#include <stdio.h>
#include <math.h>
#include<cstring>
#include<vector>
#include<algorithm>
#include <iostream>
#define ll long long int 
using namespace std;

int main() 
{
	freopen("a1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int t,i,j;
    double d,n,a,b,k,l;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        //l=999999999999999999;
        l=-1;
        scanf("%lf%lf",&d,&n);
        for(j=0;j<n;j++)
        {
            scanf("%lf%lf",&a,&b);
            k=(d-a)/b;
            if(k>l)
              l=k;
        }
        
        printf("Case #%d: %lf\n",i,d/l);
    }
	
	return 0;
}

