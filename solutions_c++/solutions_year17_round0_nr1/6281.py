#include <bits/stdc++.h>

using namespace std;

#define INF (int)1e9

int s[1010], a[1010];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t;
    cin >> t;
    for(int cs=1;cs<=t;++cs){
        string ss;
        int k;
        cin >> ss >> k;
        int n = (int)ss.size();
        memset(s, 0, sizeof(s));
        memset(a, 0, sizeof(a));
        for(int i=0;i<n;++i){
            if(ss[i]=='+')
                a[i] = 1;
        }
        int sum=0, ans=0;
        for(int i=0;i<n;++i) {
            s[i] = (a[i]+sum)%2 != 1;
            sum += s[i] - (i>=k-1?s[i-k+1]:0);
            ans += s[i];
            if(i>n-k and s[i]!=0) {
                ans=INF;
                break;
            }
        }
        cout << "Case #" << cs << ": ";
        if(ans!=INF)
            cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
