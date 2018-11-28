#include <iostream>
#include <string.h>
#include <ctype.h>
using namespace std;

int tidy(long long int temp)
{
    int rem1,rem2,x=1;
    while(temp>=1)
    {
        rem1=temp%10;
        rem2=(temp/10)%10;
        if(rem1<rem2)
           {
               x=0;
               break;
           }
        else
           {
             temp=temp/10;
           }
    }
    if(x==0)  return 0;
    else return 1;
}

int main()
{
    int n;
    cin>>n;
    long long int a[n];
    for(int i=0;i<n;i++)
    {
      cin>>a[i];
    }
    for(int i=0;i<n;i++)
    {
        while(a[i]>0)
        {
            if(tidy(a[i])==1)
                break;
            else
                a[i]--;
        }
        cout<<"Case #"<<i+1<<": "<<a[i]<<endl;
    }
}
