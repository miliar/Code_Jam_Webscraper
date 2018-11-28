#include<iostream>
#include<cmath>
#include<string>
using namespace std;
bool val(int N)
 {
 int num1,num2;
 while(N>0)
  {
   num1=N%10;
   N=N/10;

   num2=N%10;
   if(num2>num1)
   return false;
  }return true;
 }
int main()
{
int T,n,val1;
cin>>T;
  for(int i=0;i<T;i++)
  {
  cin>>n;
  cout<<"Case #"<<i+1<<": ";
  for(int j=n;j>=1;j--)
   {
   if(val(j))
   {cout<<j<<endl;
   break;
    }
   }
  }
return 0;
}

