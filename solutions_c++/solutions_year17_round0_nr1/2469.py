#include <bits/stdc++.h>
#define INF 100000000000005
#define MAXN 2000
#define mod 1000000007
#pragma comment(lib, "user32")

using namespace std;

#define F first
#define S second
#define MP make_pair
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

string s;
int adr[1005], kd[1005];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("outc.txt", "w", stdout);
    int t, k; cin >> t;
    for(int i = 0; i < t; ++i) {
        cin >> s >> k;
        memset(adr, 0, sizeof adr);
        memset(kd, 0, sizeof kd);
        int f = 0;
        for(int j = 0; j < s.size(); ++j) {
            if(s[j] == '-') f = 1;
            if(s[j] == '+') adr[j] = 1;
        }
        if(!f) {
            cout << "Case #" << i + 1 << ": " << 0 << endl;
            continue;
        }
        if(k > s.size()) {
            cout << "Case #" << i + 1 << ": " << "Impossible" << endl;
            continue;
        }
        int res = 0, st = 0;
        for(int j = 0; j < s.size() - k + 1; ++j) {
            if( (adr[j] + st) % 2 == 0 ) {
                st += 1, res += 1;
                kd[j] = 1;
            }
            if( (j - k + 1) >= 0 ) {
                st -= kd[j - k + 1];
            }
        }
        int fd = 0;
        for(int j = s.size() - k + 1; j < s.size(); ++j) {
            if( (adr[j] + st) % 2 == 0 ) {
                fd = 1;
            }
            if( (j - k + 1) >= 0 ) {
                st -= kd[j - k + 1];
            }
        }
        if(fd == 1) {
            cout << "Case #" << i + 1 << ": " << "Impossible" << endl;
            continue;
        }
        cout << "Case #" << i + 1 << ": " << res << endl;
    }
}
