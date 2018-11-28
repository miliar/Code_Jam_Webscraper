#include <iostream>
#include<stdio.h>
using namespace std;

int main() 
{
    int T;
    scanf("%d",&T);
    int p=1;
    while(p<=T)
    {int n;
    double t2=0,d1,d,v1,t1,max;
     scanf("%lf",&d);
     scanf("%d",&n);
     while(n--){
         scanf("%lf%lf",&d1,&v1);
         t1=(d-d1)/v1;
         if(t2<t1)
         t2=t1;
     }
    max=d/t2;

    printf("Case #%d: %0.6lf\n",p,max);        
p++;        
        
    }

	// your code goes here
	return 0;
}
