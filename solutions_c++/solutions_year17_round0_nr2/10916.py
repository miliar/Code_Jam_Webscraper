#include<iostream>
#include<stdlib.h>

using namespace std;

void tidynum(int);

int T,N,ans;
int main()
{   int i,j,k;
    int *n;
    cin>>T;
    if(T<1 || T>100)
    {
        cout<<"Invalid T";
        exit(0);
    }
    n=new int[T];
    for(k=0;k<T;k++)
    {
       cin>> n[k];
       if(n[k]<1 || n[k]>1000)
       {
           cout<<"Invalid N";
           exit(0);
       }
    }
    for(i=0;i<T;i++)
    {
        tidynum(n[i]);
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
}
void tidynum(int a)
{
    int i=a,b,c,t;
    while(i>=1)
    {
        t=i;
        b=t%10;
        while(t!=0)
        {
            if((t/10)==0)
            {
                ans=i;
                return ;
            }
            else
             {
                t=t/10;
             }
            c=t%10;
            if(b>=c)
            {
                b=c;

            }
            else
                goto untid;

        }
        untid:
        i--;
    }
}
