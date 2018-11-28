#include <bits/stdc++.h>
using namespace std;
int T;
string s;
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        printf("Case #%d: ",ca);
        cin>>s;
        string ans="";
        ans=s[s.size()-1];
        for(int j=s.size()-2;j>=0;j--)
        {
           if(s[j]<=ans[0])ans=s[j]+ans;
           else {
               for(int k=0;k<ans.size();k++)ans[k]='9';
               ans=(char)(s[j]-1)+ans;
           }
        }
        int u=0;
        for(int i=0;i<ans.size();i++)
        {
            if(ans[i]=='0')u++;
            else break;
        }
        ans=ans.substr(u,ans.size()-u);
        cout<<ans<<endl;
    }
    return 0;
}
