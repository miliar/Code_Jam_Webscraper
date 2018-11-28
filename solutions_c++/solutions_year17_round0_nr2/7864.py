#include <bits/stdc++.h>
typedef long long int li;
using namespace std;

int main()
{
    li t,i,k,l,j;char s[10000];
    cin>>t;
    for(i=0;i<t;i++)
        {
          cin>>s;
          l=strlen(s);
          for(j=l-1;j>=1;j--)
              {
                if(s[j]<s[j-1]) 
                    {
                      s[j-1]=s[j-1]-1;
                       for(k=j;k<l;k++)
                           s[k]='9';
                   }
             }
          if(s[0]!='0')
          cout<<"Case #"<<i+1<<": "<<s<<endl;
          else
           {
             cout<<"Case #"<<i+1<<": ";
             for(j=1;j<l;j++)
                 cout<<s[j];
              cout<<endl;
          }
       }
    return 0;
}
