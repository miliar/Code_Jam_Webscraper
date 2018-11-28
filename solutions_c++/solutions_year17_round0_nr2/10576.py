#include<fstream>
#include<iostream>
using namespace std;
int tidy(int tp,int r[])
{
int f;
int j=0;
do{
r[j]=tp%10;
tp/=10;
j++;
}while(tp);
if(j==1)
return 1;
for(int i=0;i<(j-1);i++)
{
 if(r[i]<r[i+1])
  {f=-1;break;}
  else 
  f=1;
}
return f;
}
int main()
{
 ofstream mf;
 mf.open("Tid.txt");
 int T,f,i,N,r[4],R[100];
 bool c=false;
 cin>>T;
for(int t=1;t<=T;t++)
{
 cin>>N;
for(i=N;i>0;i--)
{
 f=tidy(i,r);
if(f==1)
{c=true;break;}
if(f==-1)
c=false;
}
if(f==1)
R[t-1]=i;
}
for(i=1;i<=T;i++)
mf<<"\nCase #"<<i<<": "<<R[i-1];
mf<<"\n";
return 0;
}