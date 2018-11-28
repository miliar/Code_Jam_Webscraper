#include <bits/stdc++.h>
using namespace std;

void Solve(int testNum) {
    int k, ans = 0;
    string s;
    cin >> s >> k;
    printf("Case #%d: ", testNum);
    for(int i = 0; i <= s.size() - k; i++) {
        if(s[i] == '-') {
            for(int j = 0; j < k; j++)
                if(s[i+j] == '-') s[i+j] = '+';
                else s[i+j] = '-';
            ans++;
        }

    }
    for(int i = 0; i < s.size(); i++) {
        if(s[i] == '-') {
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    cout << ans << endl;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        Solve(i+1);
    }
}
/*
5
134
143
6810
5554

---+-++-
++++-++-
+++++---
++++++++

--++--++-
+++++++++
*/
