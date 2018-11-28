#include <cstdio>
#include <algorithm>

using namespace std;

#define NMAX 1000

int max3(int a, int b, int c)
{
    return max(a, max(b, c));
}

int main()
{
    int t;
    static char buf[NMAX+2];

    scanf("%d", &t);
    for (int tc = 1; tc <= t; ++tc) {
        int n;
        int r, o, y, g, b, v;
        bool possible = true;

        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
        /// small dataset - o = g = v = 0

        if (r) {
            buf[0] = 'R';
            --r;
        } else if (y) {
            buf[0] = 'Y';
            --y;
        } else {
            buf[0] = 'B';
            --b;
        }

        for (int i = 1; i < n && possible; ++i) {
            switch (buf[i-1]) {
            case 'R':
                if (y == 0 && b == 0) {
                    possible = false;
                } else if (y > b) {
                    buf[i] = 'Y';
                    --y;
                } else {
                    buf[i] = 'B';
                    --b;
                }
                break;
            case 'Y':
                if (r == 0 && b == 0) {
                    possible = false;
                } else if (r > b) {
                    buf[i] = 'R';
                    --r;
                } else {
                    buf[i] = 'B';
                    --b;
                }
                break;
            case 'B':
                if (y == 0 && r == 0) {
                    possible = false;
                } else if (y > r) {
                    buf[i] = 'Y';
                    --y;
                } else {
                    buf[i] = 'R';
                    --r;
                }
                break;
            }
        }

        if (buf[0] == buf[n-1]) {
            possible = false;
        }

        buf[n] = '\0';
        printf("Case #%d: ", tc);
        puts(possible ? buf : "IMPOSSIBLE");
    }

    return 0;
}
