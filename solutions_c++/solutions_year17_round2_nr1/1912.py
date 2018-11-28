#include<iostream>
#include<bits/stdc++.h>
#include <fstream>
#define ll long long int
using namespace std;
int main()
{
  ll t;
  double n,d;
  cin>>t;
  for(ll i=0;i<t;i++)
  {
    cin>>d>>n;
    double k,s;
    double maxtime=0;
    for(ll j=0;j<n;j++)
    {
      cin>>k>>s;
      if((d-k)/s>maxtime)
      {
        maxtime = (d-k)/s;
      }
    }
    //cout<<"\n"<<d/maxtime<<"\n";
    printf("Case #%lld: %.6f\n",i+1,d/maxtime);
  }
}
