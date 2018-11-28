#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <cstring>
#define MAXN 1010

using namespace std;

int n,c,m;
multiset<int> s[MAXN];
int ct[MAXN];
bool used[MAXN];

int main() {
    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        memset(ct,0,sizeof(ct));
        cin >> n >> c >> m;
        for (int i = 0; i < m; i++) {
            int p,b;
            cin >> p >> b;
            s[b].insert(p);
            ct[p]++;
        }

        int y = 0;
        for (int rem = m; rem > 0;) {
            memset(used,0,sizeof(used));
            for (int i = 1; i <= n; i++) {
                int bb = -1, mn = n + 1;
                for (int b = 1; b <= c; b++) {
                    if (used[b]) continue;
                    auto it = s[b].lower_bound(i);
                    if (it == s[b].end()) continue;
                    if (bb == -1 || *it < mn) {
                        mn = *it;
                        bb = b;
                    }
                }
                if (bb == -1) break;
                s[bb].erase(s[bb].lower_bound(i));
                rem--;
                used[bb] = 1;
            }
            y++;
        }

        int z = 0;
        for (int i = n; i > 0; i--) {
            z += max(0, ct[i] - y);
        }

        cout << "Case #" << TC << ": ";
        cout << y << ' ' << z << '\n';
    }
}
