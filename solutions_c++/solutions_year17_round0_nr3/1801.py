#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <stdlib.h>
#include <cmath>
#include <map>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;


int T;
ll K;
ll N;

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> T;
    int C = 1;
    while (T --) {
        cin >> K >> N;
        map<ll,ll> mp;
        mp[K] ++;
        ll a,b;
        ll total = N;
        while (total > 0) {
            ll lg = mp.rbegin()->first;
            ll cnt = mp.rbegin()->second;
            mp.erase(mp.rbegin()->first);
            lg --;
            a = lg / 2;
            b = lg - a;
            mp[a] += cnt;
            mp[b] += cnt;
            total -= cnt;
        }
        //cout << b << " " << a << endl;
        printf("Case #%d: %I64d %I64d\n",C ++,b,a);
    }

}









/*
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <stdlib.h>
#include <cmath>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
set<ll> st;
ll ans = 0;
void dfs(ll x,int cnt) {

    if (cnt == 18) {
        ans ++;
        return ;
    }
    for (int i = 0;i < 36;i ++) {
        if (x >> i & 1) {
            int p[4];
            p[0] = (i - 1);
            p[1] = (i + 1);
            p[2] = (i - 6);
            p[3] = (i + 6);
            for (int j = 0;j < 4;j ++) {
                if (j < 2) {
                    if (p[j] / 6 != i / 6) continue;
                }
                else {
                    if (p[j] % 6 != i % 6) continue;
                }
                if (p[j] >= 0 && p[j] < 36) {
                    if (x >> p[j] & 1) {

                    }
                    else {
                        int row = p[j] / 6;
                        int col = p[j] % 6;
                        row = 5 - row;
                        col = 5 - col;
                        int mirror = row * 6 + col;
                        if (x >> mirror & 1) {
                            continue;
                        }
                        ll nxt = x;
                        nxt |= (1LL << p[j]);
                        //cout << nxt << endl;
                        if (st.find(nxt) == st.end()) {
                            st.insert(nxt);
                            dfs(nxt,cnt + 1);
                        }
                    }
                }
            }
        }
    }
}

int main() {
    st.insert(1);
    dfs(1,1);
    cout << ans << endl;
}
*/

























