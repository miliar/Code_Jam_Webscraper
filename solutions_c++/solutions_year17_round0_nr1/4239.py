#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("gcj_in.txt","r",stdin);
    freopen("gcj_out.txt","w",stdout);
    int t;
    cin >> t;
    for(int it=1;it<=t;it++) {
        string s;
        int i,n,k,j,ans=0,cnt=0;
        cin >> s >> k;
        n = s.length();
        for(i=0;i<=n-k;i++) {
            if(s[i] == '+') continue;
            else {
                for(j=i;j<i+k;j++) {
                    if(s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
                ans = ans + 1;
            }
        }
        for(i=0;i<n;i++) {
            if(s[i] == '+') cnt = cnt + 1;
        }
        cout << "Case #" << it << ": ";
        if(cnt == n) cout << ans << "\n";
        else cout << "IMPOSSIBLE\n";
    }
    return 0;

}
