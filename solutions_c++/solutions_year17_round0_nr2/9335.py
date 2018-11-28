#include<iostream>
#include<stdio.h>
#include<string.h> 
long long int T,N,i,c;
int check(long long int num)
{
    long long int temp;
    int a,b,flag=1;
    temp = num;
    a=num%10;
    num=num/10;
    while (num > 0)
    {
        b = num % 10;
        num=num/10;
        if(b>a)
        {
               flag=0;
               return 0;
        }
        a=b;
    }
    if(flag==1)
    return 1;
    else
    return 0;
}
using namespace std;
main()
{
      cin>>T;
      c=T;
      while(T--)
      {
                cin>>N;
                for(i=N;i>0;i--)
                {
                                if(check(i)==0)
                                continue;
                                else
                                break;
                }
                cout<<"Case #"<<c-T<<": "<<i<<"\n";                   
                //fprintf(fp,"Case #%d: ",(c-T));
                //fprintf(fp,"%d\n",sum);
                
      }
             return 0;
}
