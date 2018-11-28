#include<bits/stdc++.h>
using namespace std;
int main()
{
  long long i,j,p,k,z,f,t;
  string s;
  ifstream fin;
  ofstream fout;
  fin.open("/home/anupam/A-large.in",ios::in);
  fin>>t;
  fout.open("/home/anupam/cjout.txt",ios::out);
  for(p=0;p<t;p++)
  {
    fin>>s>>k;
    f=1;
    z=0;
    for(i=0;i<s.length();i++)
    {
      if(s[i]=='-')
      {
      if(i+k-1>=s.length())
       {
         f=0;
         break;
       }
       for(j=i;j<=i+k-1;j++)
       {

         if(s[j]=='+')
         {
           s[j]='-';
         }
         else
         {
           s[j]='+';
         }
       }
       cout<<s<<i+k-1<<"\n";
       z++;
      }
    }
    for(i=0;i<s.length();i++)
    {
      if(s[i]=='-')
      {
        f=0;
        break;
      }
    }
    //f==0?cout<<s<<" "<<"Impossible\n":cout<<"Case #"<<s<<" "<<p<<": "<<z<<"\n";
   f==0?fout<<"Case #"<<p+1<<": "<<"IMPOSSIBLE\n":fout<<"Case #"<<p+1<<": "<<z<<"\n";

  }
return 0;
}
