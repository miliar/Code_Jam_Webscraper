#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
       string s;
       int k;
       cin>>s>>k;
       int count=0;
       int size=s.length();
        bool flag=true;
       for(int i=0;i<size;i++)
       {
           if(s[i]=='-')
           {
               count++;
               if(i+k>size)
               {flag=false;
               }
               if(flag){
                    for(int j=i;j<i+k;j++)
                    {
                     if(s[j]=='-')
                      s[j]='+';
                     else
                      s[j]='-';
                 }
               }
           }
       }
       cout<<"Case #"<<test<<": ";
       if(flag)
       cout<<count<<"\n";
       else
       cout<<"IMPOSSIBLE\n";
    }
return 0;
}


