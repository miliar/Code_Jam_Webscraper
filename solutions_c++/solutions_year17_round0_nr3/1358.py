#include"bits/stdc++.h"
using namespace std;
typedef long long LL;
priority_queue<LL> q;
map<LL, LL> mp;
int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("ans.txt", "w", stdout);
    int T;
    LL n, k;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++){
        cin >> n >> k;
        printf("Case #%d: ", cas);
        while(!q.empty()) q.pop();
        mp.clear();
        q.push(n);
        mp[n] = 1;
        while( 1 ){
            LL now = q.top(); q.pop();
            if(k - mp[now] <= 0){
                if(now & 1){
                    cout << now / 2 << ' ' << now / 2 << endl;
                }
                else{
                    cout << now / 2 << ' ' << (now - 1) / 2 << endl;
                }
                break;
            }
            k -= mp[now];
            if(now == 1) break;
            if(now % 2 == 0){
                if(!mp.count(now / 2)) q.push(now / 2);
                mp[now / 2] += mp[now];
                if(!mp.count((now - 1) / 2)) q.push((now - 1) / 2);
                mp[(now - 1) / 2] += mp[now];
            }
            else{
                if(!mp.count(now/2)) q.push(now / 2);
                mp[now / 2] += (2 * mp[now]);
            }
        }
    }
    return 0;
}
