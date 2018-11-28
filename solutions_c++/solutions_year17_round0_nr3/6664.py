#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
typedef long long LL;

int main() 
{
  int t;
  cin>>t;
  
  for(int i=1;i<=t;i++)
  {
     LL num,k,n;
     LL ls,rs;
     cin>>num>>k;
     int f=0;
     if(num>=1000 && num<10000)
     {
        if(k>num*0.5)
        {
          ls=0,rs=0;
          f=1;
        }
     }
     else if(num>=10000 && num<100000)
     {
      if(k>num*0.3)
        {
          ls=0,rs=0;
          f=1;
        }
     }
     else if(num>=100000 && num<1000000)
     {
      if(k>num*0.2)
        {
          ls=0,rs=0;
          f=1;
        }
     }
     else if(num>=1000000)
     {
      //cout<<"in";
      if(k>(num*0.1))
        {
          ls=0,rs=0;
          f=1;
        }
     }
     if(f==0)
     {
       n=num;
       vector<int> v;
       
       if(num==k)
       {
           ls=0;
           rs=0;
       }
       else
       {
           for(int j=0;j<k;j++)
           {
               if(j>0)
               {
                   sort(v.begin(),v.end());
                   n = v[v.size()-1];
                   v.erase(v.begin()+v.size()-1);
               }
               if(n%2==0)
               {
                   ls = n/2 -1;
                   rs = n/2;
                   v.push_back(ls);
                    v.push_back(rs);
               }
               else
               {
                   ls = n/2;
                   rs = n/2;
                   v.push_back(ls);
                    v.push_back(rs);
               }
           }
       }
     }
     cout<<"Case #"<<i<<": ";
     cout<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
     
  }
  return 0;
}
