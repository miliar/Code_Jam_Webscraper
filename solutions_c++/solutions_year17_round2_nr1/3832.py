#include <iostream>
#include <cstdio>
#define ll long long
using namespace std;

int main()
{
  int T;
  ll n,D,Si,Di;
  double totalmin = 0;
  cin>>T;
  for(int test = 1; test<=T; test++)
  {
    double min = 0;
    cout<<"Case #"<<test<<": ";
    cin>>D>>n;
    for(int i = 0; i < n;i++)
    {
      cin>>Di>>Si;
      min = (double)(D-Di)/(double)Si;
      if(i == 0) totalmin = min;
      if(min > totalmin)
        totalmin = min;
    }
    double x = (double)D/(double)totalmin;
    printf("%.6f\n",x);

  }
}
