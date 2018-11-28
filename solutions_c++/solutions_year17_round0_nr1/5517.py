#include <bits/stdc++.h>

using namespace std;

int solve() {
    string s;
    int k;
    cin >> s >> k;

    int sz = s.size();
    vector<int> v(sz);

    for (int i = 0; i < sz; i++) {
        if (s[i] == '+') v[i] = 1;
        else v[i] = 0;
    }

    int res = 0;
    for (int i = 0; i + k - 1 <  sz; i++) {
        if (v[i] % 2) continue;
        res++;
        for (int j = 0; j < k; j++) v[i + j]++;
    }
    
    for (int i = sz - 1; i >= 0; i--) {
        if (!(v[i] % 2)) return -1;
    }

    return res;
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        printf("Case #%d: ", i + 1);
        int tmp = solve();
        if (tmp >= 0) printf("%d\n", tmp);
        else printf("IMPOSSIBLE\n");
    }

    return 0;
}