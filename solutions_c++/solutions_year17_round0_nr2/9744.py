#include<bits/stdc++.h>
using namespace std;


int main()
{
    int p,check=1,a,b;
    long long n,i,j;
    cin>>p;
    for(int t=1;t<=p;t++)
    {

       cin>>n;
       cout<<"Case #"<<t<<": ";
       for(j=n;j>=1;--j)
       {
           i=j;
         if(i%10!=0)
         {
             check=1;
             a=i%10;
    i=i/10;
    while(i!=0)
    {

        b=i%10;
        i=i/10;
        if(a>=b)
            a=b;
        else
        {
            check=0;
            break;
        }
    }

         }
         else
            check=0;
         if(check==1)
         {
             cout<<j<<"\n";
             break;
         }

       }



    }



return 0;
}
