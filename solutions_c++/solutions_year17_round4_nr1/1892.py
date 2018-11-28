#include <bits/stdc++.h>
using namespace std;
const int MAXN = 110;
int T;
int N, P;
int G[MAXN];
int cnt[5];
int ans;

int main() {
    cin >> T;
    for(int t=1;t<=T;t++) {
        scanf("%d %d", &N, &P);
        for(int i=0;i<N;i++) scanf("%d", &G[i]);
        for(int i=0;i<P;i++) cnt[i] = 0;
        for(int i=0;i<N;i++) cnt[G[i]%P]++;
        ans = 0;
        ans += cnt[0];

        if(P==3) {
            int p = min(cnt[1], cnt[2]);
            ans += p;
            cnt[1] -= p;
            cnt[2] -= p;
            if(cnt[1]%3 > 0) ans++;
            if(cnt[2]%3 > 0) ans++;
            ans += cnt[1]/3;
            ans += cnt[2]/3;
        } else if(P==2) {
            ans += cnt[1]/2;
            if(cnt[1]%2==1) ans++;
        }
        
        
        cout << "Case #" << t << ": " << ans << endl;
    }

}
