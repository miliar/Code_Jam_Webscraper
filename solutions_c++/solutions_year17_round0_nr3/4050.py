//Ashwani NSIT
//codejam 2017 qualification round - C
#include <bits/stdc++.h>

using namespace std;

#define ll long int
#define mod 1000000007

int main()
{
 freopen("C-small-2-attempt0.in","r",stdin);
 freopen("ansc.out","w",stdout);
ll t1=0,n,k,i,f1,f2,ctr=0,t;
cin>>t;
while(t--)
{t1++;
priority_queue <ll> ar;
cin>>n>>k;
ctr=0;
cout<<"Case #"<<t1<<": ";
if(n%2)
 {
  f1=n/2;
  f2=n/2;
 }
 else
  {
  f1=n/2;
  f2=(n/2)-1;
  }
ctr++;
ar.push(f1);
ar.push(f2);
if(k==ctr)
 {
  cout<<f1<<" "<<f2;
 }
 else
  {
    while(ar.size())
     {ctr++;
     ll temp;
     temp=ar.top();
     ar.pop();
      if(temp%2)
       {
       f1=temp/2;
       f2=temp/2;
       }
       else
        {
        f1=temp/2;
        if(temp==1)
         {
          f2=0;
         }
         else
          {
        f2=(temp/2)-1;
          }
        }
        //cout<<f1<<" "<<f2<<endl;
        if(ctr==k)
         {
        cout<<f1<<" "<<f2;
        break;
         }
         if(f1>0)
          {
         ar.push(f1);
          }
          if(f2>0)
          {
         ar.push(f2);
          }
     }
   }
   cout<<endl;

  }
    return 0;
}
