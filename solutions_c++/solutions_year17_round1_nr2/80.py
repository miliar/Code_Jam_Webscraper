#include <bits/stdc++.h>

using namespace std;

typedef long long li;

void solve(li test_number);

int main() {
    ios_base::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);
    li n;
    cin >> n;
    for (li i = 0; i < n; i++) 
        solve(i + 1);
}

const li MAXN = 1010;
li n, m;
li need[MAXN];
vector<li> a[MAXN];
vector<char> used[MAXN];

inline bool good(li num) {
    vector<li> polis;
    for (li i = 0; i < n; i++) {
        bool found = false;
        for (li j = 0; j < m; j++) {
            if (!used[i][j]) {
                if (num * need[i] * 9 <= a[i][j] * 10 &&
                        a[i][j] * 10 <= num * need[i] * 11) {
                    polis.push_back(j);
                    found = true;
                    break;
                }
            }
        }
        if (!found) {
            return false;
        }
    }

    for (li i = 0; i < n; i++) {
        used[i][polis[i]] = 1;
    }
    //cout << num << endl;
    //for (auto cur : polis) {
        //cout << cur << " ";
    //}
    //cout << endl;
    return true;
}

void solve(li test_number) {
    li result = 0;
    cin >> n >> m;
    for (li i = 0; i < n; i++) {
        cin >> need[i];
    }
    for (li i = 0; i < n; i++) {
        used[i].clear();
        a[i].resize(m);
        used[i].resize(m, 0);
        for (li j = 0; j < m; j++) {
            cin >> a[i][j];
        }
        sort(a[i].begin(), a[i].end());
    }

    li cur = 0;
    while (true) {
        cur++;
        if (good(cur)) {
            result++;
            cur--;
        }
        if (result >= m || cur >= 1000010) {
            break;
        }
    }

    cout << "Case #" << test_number << ": " << result << endl;
}
