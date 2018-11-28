#include <iostream>
#include <iomanip>

using namespace std;

unsigned long long solve(int n, int k, unsigned long long t[1000], unsigned long long s[1000])
{
 unsigned long long area = 0,top;
 int index = 0;
 for(int i=0; i<n; i++)
 {
  if (t[i]+s[i] > area)
  {
   area = t[i]+s[i];
   index = i;
  }
 }
 top = t[index];
 for(int i=0; i<n; i++)
 {
  if (t[i] >= top)
  {
   t[i] = t[i] - top;
  }
  else
  {
   t[i] = 0;
  }
 } 
 s[index] = 0;
 t[index] = 0;
 if (k==1)
 {
  return area;
 }
 else
 {
  return area + solve(n,k-1,t,s);
 }
}


int main()
{
 int te,n,k;
 unsigned long long int r[1000],h[1000],t[1000],s[1000];
 double area;
 cin>>te;
 for(int i=1; i<=te; i++)
 {
  cin>>n>>k;
  for(int j=0; j<n; j++)
  {
   cin>>r[j]>>h[j];
   t[j] = r[j]*r[j];
   s[j] = 2*r[j]*h[j];
  }
  area = solve(n,k,t,s);
  cout<<"Case #"<<i<<": "<<setprecision(10)<<fixed<<3.14159265359*area<<"\n";
 }
 return 0;
}
