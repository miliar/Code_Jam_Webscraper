#include<iostream>
#include<bits/stdc++.h>
#include <fstream>
using namespace std;
int main()
{
  ofstream myfile;
  myfile.open ("pancake.txt");
  long long int t,i,k,c=0,len=0,flag,j,h;
  char s[1001];
  cin>>t;
  for(i=0;i<t;i++)
  {
    cin>>s>>k;
    len=strlen(s);
    c=0;
    for(j=0;j<=len-k;j++)
    {
      if(s[j]=='+')continue;
      c++;
      for(h=j;h<=j+k-1;h++)
      {
        if(s[h]=='+')s[h]='-';
        else s[h]='+';
      }
    }
    flag=0;
    for(j=len-k+1;j<len;j++)
      if(s[j]=='-')
        {
          flag=1;
          break;
        }
    if(flag==0)
      myfile<<"Case #"<<i+1<<": "<<c<<"\n";
    else
      myfile<<"Case #"<<i+1<<": IMPOSSIBLE\n";
  }

}
