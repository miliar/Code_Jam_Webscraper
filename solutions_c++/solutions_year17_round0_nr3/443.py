//    JAI JINENDRA
#include<iostream>
#include<fstream>
#include<bits/stdc++.h>
using namespace std;
#define MAX 100000
int main()
{
   int t,T;
   long long int N,K,current,length[MAX],counter[MAX],first,last;

   ifstream fin("C-large.in");
   ofstream fout("C-large.out");
   fin>>T;
   for(t=1;t<=T;++t)
   {
      fin>>N>>K;
      first=last=0;
      length[0]=N;counter[0]=1;
      for(--K;counter[first]<=K;)
      {
         K=K-counter[first];
         if(length[last]==length[first]/2)
            counter[last]+=counter[first];
         else
         {
            ++last;
            length[last]=length[first]/2;
            counter[last]=counter[first];
         }

         if(length[last]==(length[first]-1)/2)
            counter[last]+=counter[first];
         else
         {
            ++last;
            length[last]=(length[first]-1)/2;
            counter[last]=counter[first];
         }
         ++first;
      }
      fout<<"Case #"<<t<<": ";
      fout<<(length[first]/2)<<" "<<(length[first]-1)/2<<endl;
   }
   return 0;
}
