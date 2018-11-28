#include <bits/stdc++.h>

using namespace std;

int ctn[1001];
int ctc[1001];
int n, c;

bool check(int x){
    int cur = 0;
    for (int i = n - 1; i >= 0; i--){
        if (cur + ctn[i] > x){
            cur = cur + ctn[i] - x;
        } else {
            cur = 0;
        }
    }
    return cur == 0;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int cnt = 0; cnt < t; cnt++){
        int q;
        cin >> n >> c >> q;
        for (int i = 0; i < c; i++) ctc[i] = 0;
        for (int i = 0; i < n; i++) ctn[i] = 0;
        for (int i = 0; i < q; i++){
            int p, b;
            cin >> p >> b;
            p--, b--;
            ctn[p]++;
            ctc[b]++;
        }
        int mx = 0;
        int mx1 = 0;
        for (int i = 0; i < c; i++) mx = max(mx, ctc[i]);
        for (int i = 0; i < n; i++) mx1 = max(mx1, ctn[i]);
        if (mx1 <= mx){
            cout << "Case #" << cnt + 1 << ": " << mx << " " << 0 << "\n";
            continue;
        }
        int l = mx - 1;
        int r = mx1;
        while (l < r - 1){
            int m = (l + r) / 2;
            if (check(m)) r = m;
            else l = m;
        }
        int sum = 0;
        for (int i = 0; i < n; i++){
            if (ctn[i] > r) sum += ctn[i] - r;
        }
        cout << "Case #" << cnt + 1 << ": " << r << " " << sum << "\n";
    }
    return 0;
}

