#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
  long n,d,e,f,c;
  cin>>n;
  for(long i=0;i<n;i++)
  {
    cin>>d;
    while(d>0)
    {
        c=1;
        long temp = d;
        //cout<<d<<endl;
         e=temp%10;
        temp=temp/10;
        while(temp!=0)
        {
            f=temp%10;
            if(f<=e);
            else 
            {
                c=0;
                break;
            }
            e=f;
            temp=temp/10;
        }
        if(c==1)
        {
            cout<<"Case #"<<i+1<<": "<<d<<endl;
            break;
        }
        d--;
    }
  }
  return 0;
}

