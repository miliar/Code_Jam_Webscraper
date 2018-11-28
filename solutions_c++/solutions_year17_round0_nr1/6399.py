#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.ans","w",stdout);
    int t, cs = 1, i, k;
    string s;
    cin>>t;
    while(t--){
        cin>>s>>k;
        int m = s.length() - k;
        int ans = 0;
        for(i = 0;i<=m;i++){
            if(s[i]=='+') continue;
            for(int j = i;j<i+k;j++){
                s[j] = ((s[j]=='+')?'-':'+');
            }
            ans++;
        }
        for(;i<s.length();i++){
            if(s[i]=='-') break;
        }
        printf("Case #%d: ",cs++);
        if(i<s.length())
            printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}
