#include <bits/stdc++.h>

using namespace std;

#define ll long long int

int main()
{
    freopen("input.txt","r",stdin);

    freopen("output.txt","w",stdout);

    ll x,line,n,i,j,k,cnt=0,l=0;

    string s;

    cin>>line;

    for(x=0; x<line; x++)
    {
        cin>>s>>k;

        cnt=0,l=0;

        printf("Case #%lld: ",x+1);

        while(l<=s.size()-k)
        {
            if(s[l]=='+')
            {
                l++;

                continue;
            }

            else
            {
                cnt++;

                for(j=l; j<l+k; j++)
                {
                    if(s[j]=='+') s[j]='-';

                    else if(s[j]=='-') s[j]='+';
                }
            }

            l++;

            //cout<<"bal: "<<s<<endl;
        }

        ll p=0;

        for(i=0; i<s.size(); i++)
        {
            if(s[i]=='+')
            {
                p++;
            }
        }

        if(p!=s.size())
        {
            cout<<"IMPOSSIBLE"<<endl;
        }

        else
        {
            cout<<cnt<<endl;
        }
    }

    return 0;
}
