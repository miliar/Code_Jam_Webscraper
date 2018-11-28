#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;cin>>t;
    for(int ii=1;ii<=t;ii++){
        string s;cin>>s;
        int k;cin>>k;
        int res=0;
        for(int i=0;i<s.size();i++)
            if(s[i]=='-'){
                res++;
            if(i+k>s.size())break;
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
         cout<<"Case #"<<ii<<": ";
         bool ok=1;
         for(int i=s.size()-1;i>=s.size()-k && i>=0;i--)
            if(s[i]=='-'){ok=0;break;}
        if(ok)cout<<res<<endl;else cout<<"IMPOSSIBLE\n";
    }
    return 0;
}
