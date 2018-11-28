#include <iostream>
#include <cstdio>
#define ll long long
using namespace std;

int main()
{
  int T;
  ll N,D, Si,Di;
  double totalmin = 0;
  cin>>T;
  for(int a0 = 1; a0<=T; a0++)
  {
    double min = 0;
    cout<<"Case #"<<a0<<": ";
    cin>>D>>N;
    for(int i = 0; i < N;i++)
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
