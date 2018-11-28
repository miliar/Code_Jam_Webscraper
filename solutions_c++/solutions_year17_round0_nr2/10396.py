#include<iostream>
using namespace std;
int main()
{
    unsigned int t,m,flag=0;
    unsigned int n,x,p;
    cin>>t;
    m=1;
    while(t--)
    {
        cin>>n;
        while(n--)
        {
           p=n+1;
           x=p%10;
           p=p/10;


           while(p!=0)
           {
              if(x>=(p%10))
              {
                  x=p%10;
                  p=p/10;
                  flag=0;
              }
              else
                {
                    flag=1;
                    break;
                }
           }
          if(flag==0)
          {
              cout<<"Case #"<<m<<": "<<n+1<<endl;
              break;
          }
        }
      m++;
    }
   return 0;
}
