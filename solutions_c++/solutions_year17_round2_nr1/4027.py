#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
 int t;
 cin>>t;
 for(int T=1; T<=t; T++)
 {
   int D,N;
   cin>>D>>N;

   int Ki,Si;
   float ans=0;
   while(N--)
   {
     cin>>Ki>>Si;

     float lesser=float(D-Ki)/Si;
     if(lesser>ans) ans=lesser;
   }

   printf("Case #%d: %f\n",T,D/ans);
 }
  return 0;
 }

