#include <bits/stdc++.h>
using namespace std;

int T,K;
string s;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int t=1;t<=T;++t){
        cin>>s>>K;
        int i,n=0;
        for(i=0;i<=s.size()-K;++i)
            if(s[i]=='-'){
                ++n;
                for(int j=i;j<i+K;++j)
                    s[j]=(s[j]=='-'?'+':'-');
            }
        for(;i<s.size();++i)
            if(s[i]=='-')
                break;
        if(i==s.size())
            printf("Case #%d: %d\n",t,n);
        else
            printf("Case #%d: IMPOSSIBLE\n",t,n);
    }
}
