#include <iostream>

using namespace std;

unsigned long long int space[2];

void solve(unsigned long long int n,unsigned long long int k)
{
 if (k <= 1)
 {
  space[0] = (n-1)/2;
  space[1] = n/2;
 }
 else if ((k-1)/2 == k/2)
 {
  solve((n-1)/2,(k-1)/2);
 }
 else
 {
  solve(n/2,k/2);
 }
 return;
}

int main()
{
 int t;
 unsigned long long int n,k;
 space[0] = 0;
 space[1] = 0;
 cin>>t;
 for (int i = 1; i<=t ; i++)
 {
  cin>>n>>k;
  solve(n,k);
  cout<<"Case #"<<i<<": "<<space[1]<<" "<<space[0]<<"\n";
 }
 return 0;
}
  
 
