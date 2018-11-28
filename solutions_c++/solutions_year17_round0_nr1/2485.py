#include <bits/stdc++.h>

using namespace std;

int n, k;
string s;
int tree[1001];

void init() {
    for (int i = 1; i <= n; i++) tree[i] = 0;
}

void update(int i, int s) {
    if (i > n) return;
    while (i <= n) {
        tree[i] += s;
        i += (i & -i);
    }
}

int get(int i) {
    int sum = 0;
    while (i) {
        sum += tree[i];
        i -= (i & -i);
    }
    return sum;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        cin >> s >> k;
        n = s.length();
        init();
        for (int j = 0; j < n; j++) {
            if (s[j] == '-') {
                update(j + 1, 1);
                update(j + 2, -1);
            }
        }
        int res = 0;
        for (int i = 1; i <= n; i++)
            if (get(i) % 2) {
                if (i + k - 1 > n) {
                    res = -1;
                    break;
                }
                res++;
                update(i, 1);
                update(i + k, -1);
            }
        if (res == -1) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }
}
