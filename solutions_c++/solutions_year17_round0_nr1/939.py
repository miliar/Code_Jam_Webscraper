#include <iostream>

using namespace std;



int solve(int a[1001],int index, int l, int k)
{
 int n = 0;
 int p;
 if(l-index < k)
 {
  for(int i=index;i<l;i++)
  {
   if (a[i] == 0)
    return -1;
  }
  return 0;
 }
 else
 {
  if(a[index] == 1)
   p = solve(a,index+1,l,k);
  else
  {
   n=1;
   for(int i = index; i<index+k; i++)
    a[i] = (a[i]+1)%2;
   p = solve(a,index+1,l,k);
  }
 }
 if(p == -1)
  return p;
 else
  return p+n;
} 
 

int main()
{
  int t,k,r,a[1001],l;
  string s;
  cin>>t;
  for(int i=1;i<=t;i++)
  {
   s="";
   cin>>s>>k;
   l = s.length();
   for(int j=0;j<l;j++)
   {
    if(s[j] == '+')
     a[j] = 1;
    else
     a[j] = 0;
   }
   r=solve(a,0,l,k);
   if(r == -1)
   cout<<"Case #"<<i<<": IMPOSSIBLE\n";
   else
   cout<<"Case #"<<i<<": "<<r<<"\n";
  }
  return 0;
}
