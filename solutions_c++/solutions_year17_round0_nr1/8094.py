#include<bits/stdc++.h>
#define Wale_ed ios_base::sync_with_stdio(0);cin.tie(0);
#define ll long long
#define ull unsigned long long
#define ld long double
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    Wale_ed
    string s,sn,sp,ss;
    int n,cnt,ans;
    int t;
    cin>>t;
    for (int cas=1; cas<=t; cas++)
    {
        cin>>s>>n;
        cout<<"Case #"<<cas<<": ";
        ans=0;
        for (int i=0;i<=s.size()-n;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for (int j=0;j<n;j++)
                    s[i+j]=((s[i+j]=='+')?'-':'+');
            }
        }
        //cout<<s<<" ";
        cnt=0;
        while(cnt<s.size()&&s[cnt]!='-')
            cnt++;
        if(cnt!=s.size())
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<ans<<endl;
    }
    return 0;
}
