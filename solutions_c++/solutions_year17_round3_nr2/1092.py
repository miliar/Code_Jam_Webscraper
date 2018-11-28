#include <iostream>
using namespace std;
#define ll long long

int main()
{   ll t,o;
    scanf("%lld",&t);
    for(o=1;o<=t;o++)
    {   printf("Case #%lld: ",o);
        ll a,b,c[2][2],t,i;
        scanf("%lld%lld",&a,&b);
        for(i=0;i<a;i++)
            cin>>c[i][0]>>c[i][1];
        for(i=0;i<b;i++)
            cin>>c[i+a][0]>>c[i+a][1];
        if(c[1][0]<c[0][0])
        {   t=c[1][0];
            c[1][0]=c[0][0];
            c[0][0]=t;
            t=c[1][1];
            c[1][1]=c[0][1];
            c[0][1]=t;
        }
        if(a==2 || b==2)
        {   if(c[1][1]-c[0][0]<=720 || c[1][0]-c[0][1]>=720)
                printf("2\n");
            else
                printf("4\n");
        }
        else
            printf("2\n");
    }
    return 0;
}
