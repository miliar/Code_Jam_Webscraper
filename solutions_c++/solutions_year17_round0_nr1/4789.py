#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define mod 1000000007
#define ll long long

int main()
{
    string s;
    int t,i,cnt,flag,ind,n;
    
   freopen("input2.in","r",stdin);
   freopen("output2.txt","w",stdout);
    
    cin>>t;
    
    for(int j=0;j<t;j++)
    {
       cnt=0;
       flag=0;
       cin>>s>>ind;
       n=s.length();
       for(i=0;s[i];i++)
       {
           if(s[i]=='-')
           {
               if(i>(n-ind))
               {
                flag=1;
                break;
               }
               for(int k=i;k<i+ind;k++)
               {
                   if(s[k]=='+')
                   s[k]='-';
                   else 
                   s[k]='+';
               }
               cnt++;
           }
       }
       if(flag==0)
       cout<<"Case #"<<j+1<<": "<<cnt<<endl;
       if(flag==1)
       cout<<"Case #"<<j+1<<": "<<"IMPOSSIBLE"<<endl;
    }
    
    return 0;
}
