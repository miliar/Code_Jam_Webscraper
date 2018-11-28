#include <bits/stdc++.h>
#include<fstream>
#define li long long int
#define chal(n) for(li i=0;i<n; ++i)
#define ot(n) cout<<n<<"\n"
#define INF 1000000009
using namespace std;

int main()
{
    li t;
    cin>>t;
    for(li tt=1; tt<=t; ++tt)
    {
        string s;
       cin>>s;
       cout<<"Case #"<<tt<<": ";
       li n=s.size();
       if(n==1)
        cout<<s;
       else
       {
           char val=s[0];
           li idx=-1;
           chal(n)
           {
               if(val>s[i])
               {
                   idx=i-1;
                   break;
               }
               val=s[i];
           }
           if(idx==-1)
            cout<<s;
           else
           {
               for(; idx>=0&&s[idx]<='1'; --idx);
               if(idx<0)
               {
                   n--;
                   chal(n)
                   cout<<'9';
               }
               else
               {
                   char kval=s[idx];
                   for(; idx>=0; --idx)
                   {
                       if(s[idx]!=kval)
                        break;
                       kval=s[idx];
                   }
                   ++idx;
                   chal(idx)
                   cout<<s[i];
                   cout<<(char)((int)s[idx]-1);
                   for(li i=idx+1; i<n; ++i)
                    cout<<'9';
               }
           }
    }

    if(tt!=t)
        cout<<endl;
    }
    exit(0);
}
