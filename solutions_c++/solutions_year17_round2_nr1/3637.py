#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cstring>
using namespace std;
struct node{
  int K,S;
};
node all[1001];
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("a.txt","w",stdout);
  int cases,t,D,N,i,s;
  double tt,Max,answer;
  cin>>t;
  for(cases=1;cases<=t;cases++)
  {
    printf("Case #%d: ",cases);
    cin>>D>>N;
    Max=0.0;
    s=0;
    for(i=0;i<N;i++)
    {
      cin>>all[i].K>>all[i].S;
      tt=(double)(D-all[i].K)/(double)all[i].S;
      if(tt>Max)
      {
        s=i;
        Max=tt;
      }
    }
    answer=(double)D/((double)(D-all[s].K)/(double)all[s].S);
    printf("%.6f\n", answer);
  }
  return 0;
}