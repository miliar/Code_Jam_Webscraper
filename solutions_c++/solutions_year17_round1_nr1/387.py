#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int r,c;
char g[30][30];
int mnr[26],mxr[26],mnc[26],mxc[26];

void go(int u, int d, int l, int r, vector<int> &p) {
    if (p.size() == 1) {
        for (int i = u; i <= d; i++) {
            for (int j = l; j <= r; j++) {
                g[i][j] = 'A' + p[0];
            }
        }
        return;
    }
    bool found = 0;
    int m;
    vector<int> lp,rp;

    if (!found) {
        for (m = u; m < d; m++) {
            lp.clear();
            rp.clear();
            for (int i : p) {
                if (mxr[i] <= m) lp.push_back(i);
                else rp.push_back(i);
            }
            bool ok = !lp.empty() && !rp.empty();
            for (int i : rp) {
                if (mnr[i] <= m) ok = 0;
            }
            if (ok) {
                found = 1;
                break;
            }
        }
        if (found) {
            go(u,m,l,r,lp);
            go(m+1,d,l,r,rp);
        }
    }

    if (!found) {
        for (m = l; m < r; m++) {
            lp.clear();
            rp.clear();
            for (int i : p) {
                if (mxc[i] <= m) lp.push_back(i);
                else rp.push_back(i);
            }
            bool ok = !lp.empty() && !rp.empty();
            for (int i : rp) {
                if (mnc[i] <= m) ok = 0;
            }
            if (ok) {
                found = 1;
                break;
            }
        }
        if (found) {
            go(u,d,l,m,lp);
            go(u,d,m+1,r,rp);
        }
    }
}

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        memset(g,0,sizeof(g));
        cin >> r >> c;
        for (int i = 0; i < r; i++) {
            cin >> g[i];
        }

        for (int i = 0; i < 26; i++) {
            mnr[i] = r;
            mxr[i] = -1;
            mnc[i] = c;
            mxc[i] = -1;
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (g[i][j] == '?') continue;
                int ch = g[i][j] - 'A';
                mnr[ch] = min(mnr[ch], i);
                mxr[ch] = max(mxr[ch], i);
                mnc[ch] = min(mnc[ch], j);
                mxc[ch] = max(mxc[ch], j);
            }
        }

        vector<int> p;
        for (int i = 0; i < 26; i++) {
            if (mxr[i] != -1) p.push_back(i);
        }

        go(0,r-1,0,c-1,p);

        cout << "Case #" << TC << ":\n";
        for (int i = 0; i < r; i++) {
            cout << g[i] << '\n';
        }
    }
}
