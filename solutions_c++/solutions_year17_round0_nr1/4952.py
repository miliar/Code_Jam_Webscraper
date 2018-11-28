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
        li k;
       cin>>s>>k;
       cout<<"Case #"<<tt<<": ";

        li co=0, flag=0;
        li n=s.size();
        chal(n)
        {
            if(s[i]=='-')
            {
                for(li j=i; j<i+k; ++j)
                {
                    if(j>=n)
                    {
                        flag=1;
                        break;
                    }
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                if(flag){
                    break;
                }

                    ++co;
            }
        }
        if(!flag)
            cout<<co;
        else
            cout<<"IMPOSSIBLE";
    if(tt!=t)
        cout<<endl;
    }
    exit(0);
}
