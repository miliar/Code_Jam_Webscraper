#include <iostream>
#include <iomanip>

using namespace std;

 

int main()
{
  int t,n;
  long int d,k,s;
  double max=0,temp;
  cin>>t;
  for(int i=1;i<=t;i++)
  {
   max=0;
   cin>>d>>n;
   for(int j=0;j<n;j++)
   {
    cin>>k>>s;
    temp = (d-k)*1.0/s;
    if(temp>max)
     max= temp;
   } 
   cout<<"Case #"<<i<<": "<<setprecision(6)<<fixed<<d/max<<"\n";
  }
  return 0;
}
