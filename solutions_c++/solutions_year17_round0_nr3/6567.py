/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 50;

priority_queue<int> Q;

int main()
{
    freopen("input_r.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    cin >> T;

    for (int _t = 1; _t <= T; _t++)
    {
        int N, K;
        cin >> N >> K;

        while(Q.size() > 0) Q.pop();
        Q.push(N);

        int l, r;
        for (int i = 0; i < K; i++)
        {
            int bs = Q.top();
            Q.pop();

            l = (bs - 1) / 2;
            r = (bs - 1) - l;

            Q.push(l);
            Q.push(r);
        }

        cout << "Case #" << _t << ": " << max(l, r) << " " << min(l, r) << endl;
    }

    return 0;
}
