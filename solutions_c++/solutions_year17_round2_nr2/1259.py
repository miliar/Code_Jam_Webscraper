#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define forv(i, a) forn(i, (int)(a).size())

typedef long long lng;

int n;
int order[5000];
int m[10];

int cmp(int i, int j)
{
    return m[i] > m[j];
}

int make_order()
{
    int idx[] = {0, 1, 2};
    sort(idx, idx + 3, cmp);

    int r = m[idx[0]];
    int g = m[idx[1]];
    int b = m[idx[2]];

    if (r == 1) {
        int i = 0;
        order[i++] = idx[0];

        if (g != 0) {
            order[i++] = idx[1];
        }

        if (b != 0) {
            order[i++] = idx[2];
        }

        return i;
    }

    if (r > g + b)
        return -1;

    int i = 0;
    forn(t, b + g - r) {
        order[i++] = idx[0];
        order[i++] = idx[1];
        order[i++] = idx[2];
    }

    forn(t, r - b) {
        order[i++] = idx[0];
        order[i++] = idx[1];
    }

    forn(t, r - g) {
        order[i++] = idx[0];
        order[i++] = idx[2];
    }

    return i;
}

const char* str[] = {"R", "Y", "B", "GR", "VY", "OB"};


bool check_single() {
    int idx[] = {0, 1, 2, 3, 4, 5};
    sort(idx, idx + 6, cmp);

    if (m[idx[1]] == 0 && idx[0] > 2) {
        forn(i, m[idx[0]]) {
            cout << str[idx[0]];
        }
        return true;
    }

    return false;
}

int solve()
{
    int cnt[10];

    cin >> n;
    forn(i, 6)
        cin >> cnt[i];

    m[0] = cnt[0] - cnt[3];
    m[1] = cnt[2] - cnt[5];
    m[2] = cnt[4] - cnt[1];
    m[3] = cnt[3];
    m[4] = cnt[5];
    m[5] = cnt[1];

    if (check_single()) {
        return 0;
    }

    forn(i, 3) {
        if (m[i + 3] > 0 && m[i] < 1) 
            return -1;
    }

    int t = make_order();
    if (t < 0)
        return -1;

    forn(i, t) {
        int cur = order[i];
        cout << str[cur];

        if (m[cur + 3] > 0) {
            forn(k, m[cur + 3]) {
                cout << str[cur + 3];
            }
            m[cur + 3] = 0;
        }
    }
    
    return 0;
}

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0); 

    int T;
    cin >> T;
    forn(tc, T) {
        std::cout << "Case #" << tc + 1 << ": ";

        if (solve() < 0) {
            cout << "IMPOSSIBLE";
        }

        cout << endl;
    }
    
    return 0;
}
