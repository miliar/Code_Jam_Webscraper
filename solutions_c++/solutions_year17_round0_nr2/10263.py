#include<bits/stdc++.h>
using namespace std;

int nocompare(int n)
{
    int check=1,a,b;
    a=n%10;
    n=n/10;
    while(n!=0)
    {

        b=n%10;
        n=n/10;
        if(a>=b)
            a=b;
        else
        {
            check=0;
            break;
        }
    }
    return check;

}

int main()
{
    int p,n,check=1;
    cin>>p;
    for(int t=1;t<=p;t++)
    {
       cin>>n;
       cout<<"Case #"<<t<<": ";
       for(int i=n;i>=1;--i)
       {
         if(i%10!=0)
         {
           check=nocompare(i);

         }
         else
            check=0;
         if(check==1)
         {

             cout<<i<<"\n";
             break;
         }

       }



    }// test case close



return 0;
}
