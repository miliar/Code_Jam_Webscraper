#include <bits/stdc++.h>

using namespace std;

#define ll long long int

vector < int > v;

int main()
{
    freopen("input.txt","r",stdin);

    freopen("output.txt","w",stdout);

    ll x,line,n,i,a,j,ans;

    cin>>line;

    for(x=0; x<line; x++)
    {
        cin>>n;

        for(i=n; i>=1; i--)
        {
            v.clear();

            ll temp=i;

            while(temp)
            {
                a=temp%10;

                temp/=10;

                v.push_back(a);

            }

            ll cnt=0;

            for(j=1; j<v.size(); j++)
            {
                if(v[j]<=v[j-1])
                {
                    cnt++;
                }
            }

            if(cnt==v.size()-1)
            {
                ans=i;

                break;
            }
        }

        printf("Case #%lld: %lld\n",x+1,ans);
    }

    return 0;
}
