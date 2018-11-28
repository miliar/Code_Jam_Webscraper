//    JAI JINENDRA
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
   int t,T,change[1005],counter,l,i,K;
   char str[1005];
   ifstream fin("A-large.in");
   ofstream fout("A-large.out");
   fin>>T;
   for(t=1;t<=T;++t)
   {
      fin>>str>>K;
      fout<<"Case #"<<t<<": ";

      //fout<<"Case #1: ";
      for(l=0;str[l];++l)
         change[l]=0;
      counter=0;
      for(i=0;i+K<=l;++i)
      {
         if(  (str[i]=='-'&&change[i]%2==0) || (str[i]=='+'&&change[i]%2) )
         {
            ++counter;
            change[i+1]++;
            change[i+K]--;
         }
         change[i+1]+=change[i];
      }
      for(;i<l&&( (str[i]=='+'&&change[i]%2==0) || (str[i]=='-'&&change[i]%2) );++i)
      {
         //cout<<i<<" "<<str[i]<<" "<<change[i]<<endl;
         change[i+1]+=change[i];
      }

      if(i==l)
      {
         fout<<counter<<endl;
      }
      else
      {
         fout<<"IMPOSSIBLE"<<endl;
      }
      //fout<<counter<<endl;
   }
   return 0;
}
