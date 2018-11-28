#include<bits/stdc++.h>
using namespace std;

long long int a[101000];
priority_queue<long long> Q;

int main()
{
    int t,i;
    long long n,k,x;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {

        scanf("%lld %lld",&n,&k);
        Q = priority_queue <long long>();
        Q.push(n);
        while(k>1)
        {
            x= Q.top();
            Q.pop();
            x--;
            Q.push(x/2);
            Q.push(x-x/2);
            k--;
        }
        x= Q.top();
        x--;
        if(x/2> x-x/2)
            printf("Case #%d: %lld %lld\n",i,x/2,x-x/2);
        else
            printf("Case #%d: %lld %lld\n",i,x-x/2,x/2);

     //   Q = priority_queue <int>();
    }

     /*   for(i=0;i<5;i++)
        {
            scanf("%d",&a[i]);
            Q.push(a[i]);
        }
            x = Q.top();
            Q.pop();
            printf("x is %d \n",x);
            y = Q.top();
            Q.pop();
             printf("y is %d ",y);
            Q.push(x+y);
*/

    return(0);
}
