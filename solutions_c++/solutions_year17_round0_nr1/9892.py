#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,j,count,k,flag,n,m,z;
    char s[1000];
    cin>>t;
    for(z=1;z<=t;z++)
    {
        cin>>s;
        cin>>k;
        count=0;
        flag=0;
        
        n=strlen(s);
        for(i=0;i<n;i++)
        {
           if(s[i]=='-')
           {m=i+k;
               if(m<=n)
               {
               for(j=i;j<m;j++)
               {
                   if(s[j]=='+')
                   s[j]='-';
                   else
                   s[j]='+';
               }
               count++;
               }
           }
        }
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
        cout<<"Case #"<<z<<":"<<" IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<z<<":"<<" "<<count<<endl;
    }
    return 0;
}
