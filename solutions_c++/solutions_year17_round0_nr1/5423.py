#include<bits/stdc++.h>

using namespace std;

const int N = 1e3 * 2;

int n,a[N],q,k,curr,ans,res,m;
string s;

main(){
    freopen("A-large.in","r",stdin);
    freopen("1.txt","w",stdout);

    cin >> q;

    for(int test = 1; test <= q; ++test){
        cin >> s >> k;

        int n = s.size();

        for(int i = 1; i <= n; ++i){
            if(s[i - 1] == '+') a[i] = 1;
            else a[i] = 0;
        }

        curr = 0;
        ans = 0;
        for(int i = 1; i <= n; ++i){
            if(!a[i] && n - i + 1 >= k){
                ans++;
                for(int j = i; j < i + k; ++j)
                    a[j] ^= 1;
            }
            else if(!a[i] && n - i < k) curr = 1;
        }


        if(!curr) cout << "Case #" << test << ": " << ans << "\n";
        else cout << "Case #" << test << ": " << "IMPOSSIBLE\n";
    }
}
