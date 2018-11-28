#include<iostream>
using namespace std;
typedef long long int ull;
bool istidy(long long int a)
{ long long int temp,r,p,s=10;
  while(a>0)
  {
    r=a%10;


    if(s<r)
    {
      return false;
    }
    s=r;


  a=a/10;

  }
  return true;
}
//using namespace std;
int main()
{
  int n;
  cin>>n;
  for(int i=1;i<=n;i++)
  { long long int l,t;
    long long int a;
    cin>>a;

    while(a>0)
    {// cout<<a<<"\n";
    //cout<<istidy(a);
      if(istidy(a))
      {t=a;
      break;}
      else
      {
      a=a-1;
      }

    }
    cout<<"Case #"<<i<<": "<<t<<"\n";
   }
}
