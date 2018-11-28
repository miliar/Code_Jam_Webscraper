#include <bits/stdc++.h>
#define ll long long
#define int long long
#define F first
#define S second
using namespace std;

const int N = 1e5 + 10;

int n;

int cn[10][10], cnt[N];
vector <int> d[10];
pair <int, int> st[N];
char qcur[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

void sol(int cs) {
    cin >> n;
    memset(cn, 0, sizeof(cn));
    for(int i = 0; i < 6; i++) {
        //cn[i][i] = 0;
        cin >> cnt[i];
    }
    int m = n;
    cn[0][2] = cn[2][0] = 1;
    cn[4][2] = cn[2][4] = 1;
    cn[4][0] = cn[0][4] = 1;
    cn[0][3] = cn[3][0] = 1;
    cn[2][5] = cn[5][2] = 1;
    cn[4][1] = cn[1][4] = 1;
    for(int i = 0; i < 6; i++) {
        for(int j = 0; j < 6; j++) {
            if(cn[i][j]) {
                d[i].push_back(j);
            }
        }
    }
    for(int i = 0; i < 6; i++) {
        for(int j = 0; j < 6; j++) {
            if(cn[i][j] == 1 && (j % 2) == 1 && (i % 2) == 0) {
                if(cnt[i] + cnt[j] == n) {
                    if(cnt[i] == cnt[j]) {
                        for(int k = 0; k < cnt[i]; k++) {
                            cout << qcur[i] << qcur[j];
                        }
                        return;
                    } else {
                        cout << "IMPOSSIBLE";
                        return;
                    }
                }
                if(cnt[j] && cnt[i] <= cnt[j]) {
                    cout << "IMPOSSIBLE";
                    return;
                } else {
                    st[i] = make_pair(j, cnt[j]);
                    cnt[i] -= cnt[j];
                    m -= cnt[j] * 2;
                    cnt[j] = 0;
                }
            }
        }
    }
    int cur = -1, maxl = -1;
    for(int i = 0; i < 5; i += 2) {
        if(cnt[i] > maxl) {
            maxl = cnt[i];
            cur = i;
        }
    }
    vector <int> ans;
    ans.push_back(cur);
    cnt[cur]--;
    for(int i = 1; i < m; i++) {
        int maxl = -1, nx = -1;
        for(auto x: d[cur]) {
            if(cnt[x] == maxl && i == m - 2 && x == ans.front()) {
                nx = x;
            }
            if(cnt[x] > maxl) {
                maxl = cnt[x];
                nx = x;
            }
        }
        if(maxl == 0) {
            cout << "IMPOSSIBLE";
            return;
        }
        cur = nx;
        ans.push_back(cur);
        cnt[cur]--;
    }
    if(ans.front() == ans.back()) {
        cout << "IMPOSSIBLE";
        return;
    }
    for(auto x: ans){
        cout << qcur[x];
        for(int i = 0; i < st[x].S; i++) {
            cout << qcur[st[x].F] << qcur[x];
        }
        st[x].S = 0;
    }
}

main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    //ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        sol(i);
        cout << endl;
    }
}
