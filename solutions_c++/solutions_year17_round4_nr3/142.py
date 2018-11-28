#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int n, m;
string s[55];
string ss[55];
int dp[55][32][32];
int nxt[55][32][32];
string nxts[55][32][32];

int solve(int i, int m1, int m2) {

    if (i == m) {
        return m1 == m2;
    }
    if (dp[i][m1][m2] != -1) return dp[i][m1][m2];

    int ret = 0;

    int tot = 0;
    for (int j=0; j<n; j++) if (s[j][i] == '-' || s[j][i] == '|') tot++;

    for (int j=0; j<(1<<n); j++) {

        string tmp = ss[i];
        int cur = 0;
        bool some = 0;
        for (int k=0; k<n; k++) {
            if (tmp[k] == '-' || tmp[k] == '|') {
                if ((1<<k)&j) {
                    tmp[k] = '-';
                }
                else {
                    tmp[k] = '|';
                    some = true;
                }
            }
        }

        int m11 = m1;
        int m22 = m2;
        bool good = true;
        for (int k=0; k<n && good; k++) {
            if (tmp[k] == '#') {
                if ((m11 & (1<<k))  == (m22 & (1<<k))) {
                    if ((m11 & (1<<k)) != (j & (1<<k))) {
                        m11 ^= (1<<k);
                    }
                    if (m22 & (1<<k)) {
                        m22 ^= (1<<k);
                    }
                }
                else {
                    good = 0;
                }
            }
            else if (tmp[k] == '-') {
                if ((m22 & (1<<k)) != 0) {
                    good = false;
                }
                m22 |= (1<<k);
                if ((m11 & (1<<k)) == 0) {
                    good = false;
                }
            }
            else if (tmp[k] == '|') {
                if ((m11 & (1<<k)) != 0) {
                    good = false;
                }

                bool found = false;
                for (int t=k-1; t>=0; t--) {
                    if (tmp[t] == '|' || tmp[t] == '-') found = true;
                    if (tmp[t] == '#') break;
                }
                for (int t=k+1; t<n; t++) {
                    if (tmp[t] == '|' || tmp[t] == '-') found = true;
                    if (tmp[t] == '#') break;
                }

                if (found) {
                    good = false;
                }
            }
            else if (tmp[k] == '.' && (m11 & (1<<k)) == 0) {
                bool found = false;
                for (int t=k-1; t>=0; t--) {
                    if (tmp[t] == '|') found = true;
                    if (tmp[t] == '#') break;
                }
                for (int t=k+1; t<n; t++) {
                    if (tmp[t] == '|') found = true;
                    if (tmp[t] == '#') break;
                }
                if (!found) {
                    good = false;
                }
            }

        }

        //cout<<i<<" "<<j<<" "<<m1<<" "<<m11<<" "<<tmp<<" "<<good<<endl;

        if (good) {
            int res = solve(i+1, m11, m22);

            if (res == 1) {
                nxt[i][m1][m2] = m11 + (m22<<5);
                nxts[i][m1][m2] = tmp;
                ret = 1;
                break;
            }

        }

    }

    dp[i][m1][m2] = ret;

    return ret;
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>n>>m;
        for (int i=0; i<n; i++) cin>>s[i];

        for (int i=0; i<m; i++) ss[i] = "";
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) ss[i] += s[j][i];
        }

        for (int i=0; i<m; i++) {
            for (int j=0; j<(1<<n); j++) {
                for (int k=0; k<(1<<n); k++) dp[i][j][k] = -1;
            }
        }

        bool doit = true;

        for (int i=0; i<(1<<n); i++) {
            int res = solve(0, i, 0);

            if (res == 1) {
                printf("Case #%d: POSSIBLE\n", cas);
                int m1 = i, m2 = 0;
                for (int j=0; j<m; j++) {

                    string tmp = nxts[j][m1][m2];
                    int k = nxt[j][m1][m2] & 31;
                    m2 = nxt[j][m1][m2]>>5;
                    m1 = k;
                    for (int k=0; k<n; k++) {
                        s[k][j] = tmp[k];
                    }
                }

                for (int j=0; j<n; j++) {
                    cout<<s[j]<<"\n";
                }

                doit = false;
                break;
            }
        }

        if (doit)
            printf("Case #%d: IMPOSSIBLE\n", cas);
    }

    return 0;

}
