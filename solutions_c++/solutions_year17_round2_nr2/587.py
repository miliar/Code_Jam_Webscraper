#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <list>


using namespace std;

struct Node {
    char ch;
    int val;

    bool operator < (const Node& nd) const {
        return val > nd.val;
    };
}nodes[3];

int main() {
    int n, r, o, y, g, b, v;
    int test;
    scanf("%d", &test);
    for (int cas = 1; cas <= test; cas++) {
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        int tt = max(max(r, y), b);
        nodes[0].val = r;
        nodes[0].ch = 'R';
        nodes[1].val = y;
        nodes[1].ch = 'Y';
        nodes[2].ch = 'B';
        nodes[2].val = b;
        sort(nodes, nodes + 3);

        printf("Case #%d: ", cas);

        if (n / 2 < tt) {
            puts("IMPOSSIBLE");
        }
        else {
            int cc = 0;
            int last = -1;
            while (cc < n) {
                int ma = 0;
                for (int i = 0; i < 3; i++) {
                    if (i == last) continue;
                    if (nodes[i].val > ma) {
                        ma = nodes[i].val;
                    }
                }

                for (int i = 0; i < 3; i++) {
                    if (i == last) continue;
                    if (nodes[i].val != ma) continue;
                    last = i;
                    putchar(nodes[i].ch);
                    nodes[i].val--;
                    break;
                }
                cc++;
            }
            puts("");
        }
    }
    return 0;
}
