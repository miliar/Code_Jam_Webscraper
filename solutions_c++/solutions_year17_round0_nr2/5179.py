#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define xx first
#define yy second

#ifndef _WIN32
#define gc getchar_unlocked
#else
#define gc getchar
#endif // _WIN32
void ri(int &a) {
    a = 0;
    register int x = gc();
    bool neg = false;
    while (x < '0' || x > '9') {
        if (x == '-') neg = true;
        x = gc();
    }
    while (x >= '0' && x <= '9') {
        a = (a << 3) + (a << 1) + (x-'0');
        x = gc();
    }
    if (neg) a = -a;
}

const int maxn = 100100, INF = (1 << 30)-1;

string n;
int t;

int main() {
    freopen("output.out", "w", stdout);
    cin >> t;
    for (int cs = 1; cs <= t; cs++) {
        printf("Case #%d: ", cs);
        string n;
        cin >> n;
        int len = n.size();
        bool works = true;
        for (int i = 0; works && i < len-1; i++) {
            if (n[i] > n[i+1]) works = false;
        }
        if (works) {
            printf("%s\n", n.c_str());
            continue;
        }
        int last = 0;
        for (; last < len-1; last++) {
            if (n[last] == '9' || n[last] > n[last+1]) break;
        }
        while (last > 0 && n[last] == n[last-1]) last--;
        printf("%s", n.substr(0, last).c_str());
        if (!(last == 0 && n[last] == '1')) printf("%c", n[last]-1);
        for (int i = last+1; i < len; i++) {
            printf("9");
        }
        printf("\n");
    }
    return 0;
}
