#include <bits/stdc++.h>
#define li long long int
#define INF 1000000009
using namespace std;

int main()
{
    li t;
    cin>>t;
    for(li k=1;k<=t;k++)
    {
        string s;
       cin>>s;
       cout<<"Case #"<<k<<": ";
       if(s.size()==1)
        cout<<s;
       else
       {
           char c;
           c=s[0];
           li index=-1;
           li n=s.size();
           for(li i=0;i<s.size();i++)
           {
               if(c>s[i])
               {
                   index=i-1;
                   break;
               }
               c=s[i];
           }
           if(index==-1)
            cout<<s;
           else
           {
               for(; index>=0&&s[index]<='1'; --index);
               if(index<0)
               {
                   n--;
                   for(li i=0;i<n;i++)
                   cout<<'9';
               }
               else
               {
                   char akt=s[index];
                   for(; index>=0; --index)
                   {
                       if(s[index]!=akt)
                        break;
                       akt=s[index];
                   }
                   ++index;
                   for(li i=0;i<index;i++)
                   cout<<s[i];
                   char sk=(char)((int)s[index]-1);
                   cout<<sk;
                   for(li i=index+1; i<n; ++i)
                    cout<<'9';
               }
           }
    }

    if(k!=t)
        cout<<endl;
    }
}
