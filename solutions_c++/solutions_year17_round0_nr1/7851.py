#include <bits/stdc++.h>
typedef long long int li;
using namespace std;

int main()
{
    li i,t,k,l,c,co,j,z,p,m,f;char s[10000];
    cin>>t;
    for(i=0;i<t;i++)
        {
          cin>>s>>k;
          co=0;f=1;
          l=strlen(s);
          for(j=0;j<=l-k;j++)
              {               
                 if(s[j]=='-')
                     {
                       co++;                    
                     for(z=j;z<j+k;z++)
                         {                         
                           if(s[z]=='-')
                           {s[z]='+';}   
                           else
                             s[z]='-';  
                         }
                     }
              }
           for(j=0;j<l;j++)
               {
                  if(s[j]=='-')
                      f=0;
               }
           if(f==1)
             cout<<"Case #"<<i+1<<": "<<co<<endl; 
           else
             cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE\n";  
        }
    return 0;
}