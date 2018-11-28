//    JAI JINENDRA
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
   int t,T,number[20];
   long long int N,i,l,numberTillNow;
   ifstream fin("B-large.in");
   ofstream fout("B-large.out");
   fin>>T;
   //cin>>T;
   for(t=1;t<=T;++t)
   {
      //cin>>N;
      fin>>N;
      fout<<"Case #"<<t<<": ";
      for(l=0;N;++l)
      {
         number[l]=N%10;
         N=N/10;
      }
      numberTillNow=number[l-1];
      for(i=l-2;i>=0;--i)
      {
         if(number[i+1]<=number[i])
         {
            numberTillNow=numberTillNow*10+number[i];
            continue;
         }
         for(number[i+1]--,++i;i<l-1;++i)
         {
            if(number[i+1]<=number[i])
               break;
            number[i+1]--;
         }
         break;
      }
      if(i==-1)
      {
         for(i=l-1;i>=0;--i)
            fout<<number[i];
         fout<<endl;
         continue;
      }
      for(--l;number[l]==0&&l>=i;--l);
      for(;l>=i;--l)
         fout<<number[l];
      for(;l>=0;--l)
         fout<<9;
      fout<<endl;
   }
   return 0;
}
