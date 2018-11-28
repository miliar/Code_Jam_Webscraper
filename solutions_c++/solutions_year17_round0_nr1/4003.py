#include <bits/stdc++.h>
using namespace std;
int T;
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        string s;
        int k;
        printf("Case #%d: ",ca);
        cin>>s>>k;
        int ans=0;
        for(int i=0;i<s.size()-k+1;i++)
        {
            if(s[i]=='-'){
                ans++;
                for(int j=0;j<k;j++){
                    if(s[i+j]=='-')s[i+j]='+';
                    else s[i+j]='-';
                }
            }
        }
        for(int i=s.size()-k+1;i<s.size();i++)
        {
            if(s[i]=='-')ans=-1;
        }
        if(ans==-1)puts("IMPOSSIBLE");
        else cout<<ans<<endl;
    }
    return 0;
}
