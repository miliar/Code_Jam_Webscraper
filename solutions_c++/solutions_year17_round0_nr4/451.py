//    JAI JINENDRA
#include<iostream>
#include<fstream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
   int t,T;
   long long int N,K,current,first,last,M,i,j,xi,xj,counter;
   char input[105][105],output[105][105],c;
   bool xpresent;
   ifstream fin("D-small-attempt1.in");
   ofstream fout("D-small-attempt1.out");
   //fin>>T;
   fin>>T;
   for(t=1;t<=T;++t)
   {
      fin>>N>>M;
      for(i=1;i<=N;++i)
      for(j=1;j<=N;++j)
         input[i][j]=output[i][j]='.';

      xpresent=false;counter=0;
      while(M--)
      {
         fin>>c>>i>>j;
         input[i][j]=output[i][j]=c;
         if(c=='x'||c=='o')
         {
            output[i][j]='o';
            xi=i;xj=j;xpresent=true;
         }
      }
      fout<<"Case #"<<t<<": ";

      if(N==1)
      {
         if(input[1][1]=='o')
            fout<<"2 0"<<endl;
         else
            fout<<"2 1"<<endl<<"o 1 1"<<endl;
         continue;
      }

      if(xpresent==false||xj==1)
      {
         output[1][1]='o';
         for(i=2;i<=N;++i)
            output[1][i]='+';
         for(i=2;i<=N;++i)
            output[i][i]='x';
         for(i=2;i<N;++i)
            output[N][i]='+';
      }
      else
      {
         for(i=1;i<xj;++i)
            output[1][i]='+';
         for(++i;i<=N;++i)
            output[1][i]='+';

         for(i=1;i<xj;++i)
            output[i+1][xj-i]='x';
         for(i=xj+1;i<=N;++i)
            output[i][i]='x';
         for(i=2;i<N;++i)
            output[N][i]='+';
      }
      fout<<(3*N-2)<<" ";
      counter=0;
      for(i=1;i<=N;++i)
      {
         if(input[1][i]!=output[1][i])
            ++counter;
      }
      fout<<(2*N-3+counter)<<endl;

      for(i=1;i<=N;++i)
      for(j=1;j<=N;++j)
      {
         if(input[i][j]!=output[i][j])
            fout<<output[i][j]<<" "<<i<<" "<<j<<endl;
      }
   }
   return 0;
}
