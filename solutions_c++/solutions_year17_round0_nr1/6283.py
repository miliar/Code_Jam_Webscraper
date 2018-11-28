#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> ii;
typedef long long ll;

int main()
{
    //freopen("#input.in","r",stdin);
    //freopen("#output.in","w",stdout);

    int t,k,i,j,l,ans,cnt;
    string str;

    cin>>t;

    for(i=1; i<=t; i++)
    {
        cin>>str>>k;

        ans=cnt=0;

        for(j=0; j+k-1<str.size(); j++)
        {
            if(str[j]=='+')
                continue;
            for(l=0; l<k; l++)
            {
                if(str[j+l]=='+')
                    str[j+l]='-';
                else
                    str[j+l]='+';
            }
            ans++;
        }
        for(j=0; j<str.size(); j++)
            if(str[j]=='+')
                cnt++;

        cout<<"Case #"<<i<<": ";
            if(cnt!=str.size())
                cout<<"IMPOSSIBLE";
            else
                cout<<ans;
        cout<<endl;
    }
    return 0;
}

