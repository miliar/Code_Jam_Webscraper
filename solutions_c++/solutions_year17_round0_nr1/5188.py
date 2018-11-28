#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n,T,i,p=0,k,j,t;
    string s;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>s;
        cin>>k;
        n=s.size();
        p=0;
        for(i=0;i<=n-k;i++)
        {
            if(s[i]=='-'){
            for(j=i;j<i+k;j++)
            {
                if(s[j]=='+')s[j]='-';
                else s[j]='+';
            }
            p++;
            }
            //cout<<":::>>"<<p<<endl;
        }
        int x=0;

        cout<<"Case #"<<t<<": ";

        for(i=0;i<n;i++)if(s[i]=='+')x++;
        if(x!=n){cout<<"IMPOSSIBLE";}
        else cout<<p;
        cout<<endl;

    }
    return 0;
}
