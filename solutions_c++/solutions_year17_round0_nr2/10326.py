#include <bits/stdc++.h>
using namespace std;
unsigned long long find(unsigned long long a)
{
    int b[18],i,x,f=0;
    unsigned long long tmp=a;
    for(i=0;i<18;i++)
    {
        b[i]=-1;
    }
    i=17;
    while(tmp)
    {
        x=tmp%10;
        tmp/=10;
        b[i]=x;
        //printf("%d",b[i]);
        i--;
    } //printf("\n");
    for(i=17;i>0;i--)
    {
        //printf("%d %d\n",i,b[i]);
        if(b[i-1]==-1)
        {
            break;
        }
        if(b[i]<b[i-1])
        {
            if(i==17)
            {
                b[i]=9;
                if(f==0)
                b[i-1]--;
                //printf("%d-1 %d\n",i,b[i-1]);
                f=0;
            }
            else
            {
                b[i]=9;
                if(f==0)
                b[i-1]--;
               // printf("%d-1 %d\n",i,b[i-1]);
                f=1;
                i+=2;
                
            }
        }
        else
        {
            f=0;
        }
    }
   
    for(i=0,tmp=0;i<18;i++)
    {
        if(b[i]>0){
       // printf("%d",b[i]);
        tmp=tmp*10+b[i];
        }
    }
    //printf("\n");
    return tmp;
}
int main()
{
    int t;
    unsigned long long n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%llu",&n);
        printf("%llu\n",find(n));
    }
    return 0;
}
