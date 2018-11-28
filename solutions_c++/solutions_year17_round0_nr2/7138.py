#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t,l,m,mx,p;string a;ofstream fp;
  fp.open("out.txt",ios::app);
  cin>>t;
 for(int p=1;p<=t;p++)
  {
    cin>>a;
    l=a.size();m=-1;
      for(int i=l-1;i>=1;i--)
      {
         if(a[i]<a[i-1])
          {
            a[i]='9';
            a[i-1]-=1;
            m=i;  
          }
      }
      if(m!=-1)
      {
      for(int i=m;i<l;i++)
      a[i]='9';
      }
      m=0;mx=-1;
     for(int i=0;i<l;i++)
      {
        if(m==0 && a[i]=='0')
         {mx=i;}
         if(a[i]!='0')
         m=1;
      }
    fp<<"Case #"<<p<<": "<<a.substr(mx+1)<<endl;  
  }
 return 0;
}
