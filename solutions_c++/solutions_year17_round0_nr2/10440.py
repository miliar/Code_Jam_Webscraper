#include <iostream>
#include<bits/stdc++.h>
#include<string.h>
using namespace std;
typedef unsigned long long ll;
bool foo(ll n,int prev);
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ll t;
    cin>>t;
    for(ll i=1;i<=t;i++){
        ll n;//temp,prev,nn;
        cin>>n;
        bool flag=true;
           while(n>=10)
           {
             // nn=n;
              //prev=9;
              flag=foo(n,9);
               /* while(nn>0)
                  {
                    temp=nn%10;
                     nn/=10;
                     if(temp<=prev)
                     {
                      prev=temp;
                     }
                      else{
                      flag=false;
                      break;
                    }
                }*/
                if(flag)
                {
                    break;
                }
                n=n-1;
           }
        cout<<"Case #"<<i<<": "<<n<<endl;
    }
    return 0;
}
bool foo(ll n,int prev)
{
    if(n<=0)
    {
        return true;
    }
   int temp=n%10;
   if(temp<=prev)
   {
    return foo(n/10,temp);
   }
   else{
    return false;
   }
    return true;
}
