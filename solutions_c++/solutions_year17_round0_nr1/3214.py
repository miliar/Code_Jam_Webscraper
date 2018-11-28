#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        string s;
        int k,ans=0;
        bool fl=true;
        cin>>s>>k;
        for (int j=0;j<(int)s.length() && fl;j++)
            if (s[j]=='-')
                if (s.length()-j<k) fl=false;
                else
                {
                    for (int z=j;z<j+k;z++)
                        if (s[z]=='-') s[z]='+';
                        else
                            s[z]='-';
                    ans++;
                }
        cout<<"Case #"<<i<<": ";
        if (!fl) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<'\n';
    }
    return 0;
}
