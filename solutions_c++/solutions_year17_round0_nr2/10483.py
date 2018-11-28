#include<bits/stdc++.h>

using namespace std;

bool is_tidy(long long int n)
{
  int min = INT_MAX;
  long long int no = n, temp = 0;
  while(no)
  {
    temp = no%10;
    if(temp>min)
      return false;
    if(temp<min)
      min = temp;
    no/=10;
  }
  return true;
}

long long int fun(long long int n)
{
  for(long long int i = n; i>=1; i--)
    if(is_tidy(i))
      return i;
}

int main(void)
{
  int t;
  cin>>t;
  for(int q = 1; q<=t; q++)
  {
    long long int n = 0;
    cin>>n;
    cout<<"Case #"<<q<<": "<<fun(n)<<endl;
  }
}
