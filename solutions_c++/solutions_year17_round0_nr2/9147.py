#include<fstream>
#include<string.h>
#include<iostream>
using namespace std;
int main(void)
{
ifstream in("B-large.in");
ofstream out("Output.txt");
int t;
in>>t;
for(int i=1;i<=t;i++)
{  
   char a[20];
   int d=t;
   in>>a;
   t=d;
   int len=strlen(a)-1;
   for(int j=0;j<len;j++)
   {
   	if(a[j+1]<a[j])
   	{
   	  while(a[j-1]==a[j]&&j>0)  j-=1;
   	  a[j]-=1;
   	  for(int k=j+1;k<=len;k++)   a[k]='9';  
   	  break;
    }
   }
   out<<"Case #"<<i<<": ";
   int s;
   if(a[0]=='0') s=1;
   else         s=0;
   for(int l=s;l<=len;l++)  out<<a[l];
   out<<"\n";
}
in.close();
out.close();
}
