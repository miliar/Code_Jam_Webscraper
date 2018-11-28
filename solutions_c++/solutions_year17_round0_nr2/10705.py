#include <iostream>

using namespace std;

bool checkdigit(int m)
{
  int j,k=9;
  while(m!=0)
  {
    j=m%10;
     if(j>k)
     {
        return false;
     }
    k=j;
    m=m/10;
  }
return true;
}

int main()
{
    int n,m,found=0;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        found=0;
        cin>>m;
        while(found!=1)
        {
            if(checkdigit(m))
            {
                found=1;
                break;
            }
        m--;
    }
     cout<<"Case #"<<i+1<<": "<<m<<endl;
    }
  return 0;
}

