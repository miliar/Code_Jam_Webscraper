#include <bits/stdc++.h>
using namespace std;
const int N = 1000 + 5;
int T, Case, n;
int a[6];
typedef pair<int,int> pii;
char color[] = "ROYGBV", s[N];

struct node {
    int cnt, id, first;
    node(int c, int i, int f = 0):cnt(c),id(i),first(f) {}
    bool operator < (const node &rhs) const {
        if(cnt == rhs.cnt) return first < rhs.first;
        return cnt < rhs.cnt;
    }
};

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("outLarge.out", "w", stdout);
    scanf("%d", &T);
    while(T--) {
        scanf("%d", &n);
        for(int i = 0; i < 6; i++) {
            scanf("%d", &a[i]);
        }
        printf("Case #%d: ", ++Case);
        if(a[0] + a[3] == n) {
            if(a[0] != a[3]) puts("IMPOSSIBLE");
            else {
                for(int i = 0; i < n/2; i++) {
                    s[i*2] = color[0];
                    s[i*2+1] = color[3];
                }
                s[n] = 0;
                puts(s);
            }
            continue;
        }else if(a[1] + a[4] == n) {
            if(a[1] != a[4]) puts("IMPOSSIBLE");
            else {
                for(int i = 0; i < n/2; i++) {
                    s[i*2] = color[1];
                    s[i*2+1] = color[4];
                }
                s[n] = 0;
                puts(s);
            }
            continue;
        }else if(a[2] + a[5] == n) {
            if(a[2] != a[5]) puts("IMPOSSIBLE");
            else {
                for(int i = 0; i < n/2; i++) {
                    s[i*2] = color[2];
                    s[i*2+1] = color[5];
                }
                s[n] = 0;
                puts(s);
            }
            continue;
        }
        if(a[1]) {
            if(a[4] < a[1] + 1) {
                puts("IMPOSSIBLE");
                continue;
            }
            a[4] -= a[1];
            n -= a[1]*2;
        }
        if(a[3]) {
            if(a[0] < a[3] + 1) {
                puts("IMPOSSIBLE");
                continue;
            }
            a[0] -= a[3];
            n -= a[3]*2;
        }
        if(a[5]) {
            if(a[2] < a[5] + 1) {
                puts("IMPOSSIBLE");
                continue;
            }
            a[2] -= a[5];
            n -= a[5]*2;
        }

        priority_queue<node> Q;
        int C = 0;
        for(int i = 0; i < 6; i += 2) {
            if(a[i]) {
                Q.push(node(a[i], i));
            }
        }
        node pre = Q.top(); Q.pop();
        s[C++] = color[pre.id];
        pre.first = 1;
        while(Q.size()) {
            node cur = Q.top(); Q.pop();
            s[C++] = color[cur.id];
            if(--pre.cnt > 0) Q.push(pre);
            pre = cur;
        }
        s[C] = 0;
        if(C < n || s[0] == s[n-1]) puts("IMPOSSIBLE");
        else {
            for(int i = 0; i < C; i++) {
                putchar(s[i]);
                if(s[i] == 'R' && a[3] > 0) {
                    while(a[3]--) {
                        putchar(color[3]);
                        putchar(color[0]);
                    }
                }
                if(s[i] == 'Y' && a[5] > 0) {
                    while(a[5]--) {
                        putchar(color[5]);
                        putchar(color[2]);
                    }
                }
                if(s[i] == 'B' && a[1] > 0) {
                    while(a[1]--) {
                        putchar(color[1]);
                        putchar(color[4]);
                    }
                }
            }
            puts("");
        }
    }
    return 0;
}
