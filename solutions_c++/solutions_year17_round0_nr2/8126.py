#include<iostream>
#include<bits/stdc++.h>
#include <fstream>
using namespace std;
int main()
{
  ofstream myfile;
  myfile.open ("tidyanswerlarge.txt");
  long long int t,i,flag=0,ans=0,s,r,j,h,k,len;
  cin>>t;
  char a[10000];
  for(i=0;i<t;i++)
  {
    cin>>a;
    len=strlen(a);
    for(j=1;j<len;j++)
    {
      if(a[j-1]<=a[j]) continue;
      else {
        h=j-1;
        while(h>0) {
          if(a[h]==a[h-1])
            { h--;
              continue;
            }
            else break;
        }
        a[h]=char(int(a[h]) -1);
        h++;
       for(;h<len;h++)
          a[h]='9';
        break;
      }
    }flag=0;
    myfile<<"Case #"<<i+1<<": ";
    for(j=0;j<len;j++)
    {
      if(flag==0 && a[j]=='0')
        continue;
      else {
        flag=1;myfile<<a[j];
      }
    }
    myfile<<"\n";
  }
  myfile.close();
}
