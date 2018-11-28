#include <bits/stdc++.h>
using namespace std;

int main() 
  {int p,t;
  cin>>p;
  t=p;
    while(p--)
     {long long k,cp;
     cin>>k;
     cp=k;
     vector <int> a;
   while(cp!=0)
     {int j=cp%10;
     a.push_back(j);
     cp=cp/10;}
    for(int q=0;q<a.size();q++)
       {if(a[q]<a[q+1]&&a.size()>1)
         {a[q]=9;
         a[q+1]=a[q+1]-1;
       for(int j=0;j<q;j++)
          {a[j]=9;}
    }}
  long long ans=0;
     for(int q=0;q<a.size();q++)
      {ans+=(pow(10,q)*a[q]);}
    cout<<"Case #" <<t-p<<": " <<ans<<endl;  }
   }
