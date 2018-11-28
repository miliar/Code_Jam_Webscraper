#include <bits/stdc++.h>
using namespace std;
typedef unsigned int UI;
typedef long long LL;
typedef unsigned long long ULL;

int main()
{
    freopen("in", "r", stdin);
    UI T;
    cin >> T;
    for (UI t = 1; t <= T; ++t) {
        ULL N, K;
        cin >> N >> K;
        priority_queue<ULL> q;
        q.push(N);
        ULL x = 0;
        ULL div = 1;
        ULL mx, mn;
        while (x < K) {
            ULL l = q.top();
            q.pop();
            if (l%2 == 0) {
                q.push(l/2);
                if (l/2-1 != 0)
                    q.push(l/2-1);
                ++x;
                mx = l/2;
                mn = l/2-1;
            } else {
                if (l/2 != 0) {
                    q.push(l/2);
                    q.push(l/2);
                }
                mx = l/2;
                mn = l/2;
                ++x;
            }
        }
        cout << "Case #" << t << ": " << mx << " " << mn << endl;
    }
    return 0;
}

