#include<bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("2017-A-large.in","r",stdin);
    freopen("2017-A-large.out","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        int k;
        cin>>s>>k;
        int cnt=0;
        for(int i=0;i+k<=s.size();i++)
        {
            if(s[i]=='-')
            {
                cnt++;
                for(int j=i;j<i+k;j++)
                    s[j] = s[j]=='+'?'-':'+';
            }
        }
        cout<<"Case #"<<t<<": ";
        if(count(s.begin(),s.end(),'-'))
            cout<<"IMPOSSIBLE\n";
        else
            cout<<cnt<<"\n";
    }
    return 0;
}
