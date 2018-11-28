#include <bits/stdc++.h>

using namespace std;

string s;
int k;

void flip(int x)
{
    int i;
    for(i=x;i<x+k;i++)
        s[i]=(s[i]=='+'?'-':'+');
}

int main()
{
    freopen("A_large.in","r",stdin); freopen("A_large.out","w",stdout);
    int t;
    cin >> t;
    int tc;
    for(tc=1;tc<=t;tc++)
    {
        cin >> s >> k;
        int i;
        int ans=0;
        for(i=0;i+k-1<s.size();i++)
        {
            if(s[i]=='-')
            {
                flip(i);
                ans++;
            }
        }
        bool ok=1;
        for(i=0;i<s.size();i++)
            ok&=s[i]=='+';
        if(ok)
            printf("Case #%d: %d\n",tc,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",tc);
    }
}
