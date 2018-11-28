using namespace std;
#include<iostream>
#include<stdio.h>
#include<string.h>
 int  funtionForCalculaion(int x)
    { int c,d;
         if(x<10)
           { return 1; }
            else
             {  while(x>0)
                 {   c=x%10;
                     x=x/10;
                     d=x%10;
                        if(c<d)
                         {  return 0; break; }
                 }
             }
      return 1; }
int main()

{
freopen("inputfile.in","r",stdin);// for opening file
freopen("mynumbers.out","w",stdout);// for printing in file
int par,t,b,n,result;
int testcase;
cin>>testcase;
for(int zest=1;zest<=testcase;zest++)
    {  cin>>par;
         for(int j=0;j<par;j++)
           {  result=funtionForCalculaion(par); par--;//decrement for
                if(result==1)
                   { cout<<"Case #"<<zest<<": "<<par+1<<endl; break; }

           }
   }
}
