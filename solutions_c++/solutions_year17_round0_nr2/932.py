#include <iostream>

using namespace std;





unsigned long long int solve(unsigned long long int n)
{
 int d[19],index=0,p=0;
 unsigned long long int dec=1, r=0;
 for (int i = 0; i<19; i++)
 {
  d[i] = 0;
 }
 for (int i = 0; i<19; i++)
 {
  d[18-i] = (n/dec)%10;
  dec=dec*10;
 }
 for (int i = 0; i<18; i++)
 {
  if(d[i]<d[i+1])
  {
   index = i+1;
  }
  else if(d[i]>d[i+1])
  {
   p=1;
   break;
  }
 }
 if(p==1)
 {
  d[index] = d[index] - 1;
  for (int i = index+1; i<19; i++)
  {
   d[i] = 9;
  }
 }
 dec=1;
 for(int i = 0;i<19;i++)
 {
  r = r + (dec*d[18-i]);
  dec = dec *10;
 }
 return r; 
} 
 

int main()
{
  int t;
  unsigned long long int n,r;
  cin>>t;
  for(int i=1;i<=t;i++)
  {
   cin>>n;
   r=solve(n);
   cout<<"Case #"<<i<<": "<<r<<"\n";
  }
  return 0;
}
