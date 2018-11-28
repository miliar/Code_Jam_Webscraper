#include<iostream>
using namespace std;
int main()
{
    long test,num,s,a[4];
    cin>>test;
    for(int i=1;i<=test;i++)
    {
        cin>>num;
        if(num<10)
        {
         s=num;
        }
        else for(int j=num;j>0;j--)
        {
         long n=j;
         for(int k=0;k<4;k++)
         {
           a[k]= n%10;
           n/=10;
         }
         if(a[0]>=a[1]&&a[1]>=a[2]&&a[2]>=a[3])
            {
                s=j;
                break;
            }
        }
        cout<<"Case #"<<i<<":  "<<s<<"\n";
    }
}
