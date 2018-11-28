#include<iostream>
using namespace std;
int main()
{
  int t1;
  cin>>t1;
  for(int t=1;t<=t1;t++)
  {
    unsigned long long int n,r,i;
    cin>>n;
    for(r=n;r>=0;r--)
    {
      int c=0;
      int  a[18];
      i=r;
      for(int j=17;j>=0;j--)
      {
        a[j]=i%10;
        i=i/10;
      }
      for(int j=17;j>0;j--)
      {
        if(a[j]>=a[j-1])
        c++;
      }
        if(c==17)
        {
          cout<<"Case #"<<t<<": "<<r<<endl;
          break;
        }
    }
  }
return 0;}
