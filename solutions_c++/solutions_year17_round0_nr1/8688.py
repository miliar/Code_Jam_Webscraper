#include <bits/stdc++.h>
#define fr(a, b, c) for(int a = b; a < c; ++a)
#define pb push_back

using namespace std;

typedef pair<int, int> ii;

bitset<1001> bs;
int n, k;

int ok() {
    fr(i, 0, n) if (!bs[i]) return i;
    return -1;
}

inline int query(int pos) {
    fr(i, pos, pos+k) bs.flip(i);
}

void dbg() {
    fr(i, 0, n) {
        if (bs[i]) cout << '1';
        else cout << '0';
    }
    cout << endl;
}

int main() {
    int t, cas = 0;
    cin >> t;
    while (t--) {
        string str;
        cin >> str;
        n = str.size();
        bs.reset();
        fr(i, 0, str.size()) if (str[i] == '+') bs.set(i);
        cin >> k;
        int v;
        int ans = 0;
        bool fudeu = false;
        while (true) {
            v = ok();
            //dbg();
            //getchar();
            if (v == -1) break;
            else if (v + k >  n) {
                fudeu = true;
                break;
            } else query(v), ++ans;
        }
        if (fudeu) printf("Case #%d: IMPOSSIBLE\n", ++cas);
        else printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}

