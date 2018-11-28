#include<bits/stdc++.h>
using namespace std;
int a[1010];
int main()
{
    int T;cin>>T;
    for(int ks=1;ks<=T;ks++)
    {
        memset(a,0,sizeof(a));
        string S;
        int K;
        cin>>S>>K;
        int s=S.size();
        int ans=0;
        for(int i=0;i<=s-K;i++)
        {
            if((S[i]=='+'&&a[i]%2==0)||(S[i]=='-'&&a[i]%2==1)) continue;
            ans++;
            for(int k=1;k<K;k++) a[i+k]++;
        }
        for(int i=s-K+1;i<s;i++) if((S[i]=='-'&&a[i]%2==0)||(S[i]=='+'&&a[i]%2==1)) ans=-1;
        cout<<"Case #"<<ks<<": ";
        if(ans==-1) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<endl;
    }
    return 0;
}
