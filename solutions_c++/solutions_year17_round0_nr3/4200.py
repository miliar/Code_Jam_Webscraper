#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int t; cin >> t;
    for (int T = 1; T <= t; T++){
        int n, k; cin >> n >> k;
        priority_queue<int>q;
        q.push(n);
        int m1, m2;
        for (int i = 0; i < k; i++){
            int now = q.top();
            q.pop();
            if (now & 1){
                m1 = m2 = now / 2;
            }
            else{
                m1 = now / 2; m2 = now / 2 - 1;
            }
            q.push(m1);
            q.push(m2);
        }
        printf("Case #%d: %d %d\n", T, m1, m2);
    }
    return 0;
}
