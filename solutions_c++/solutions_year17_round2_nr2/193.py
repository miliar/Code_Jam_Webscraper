#include <cstdio>
#include <string>
#include <cassert>
using namespace std;

int nrt, n;
int r, o, y, g, b, v, nr[3];
char ord[3];

void order(int r, int b, int y) {
    if(r <= b && b <= y) {
        ord[0] = 'R', nr[0] = r;
        ord[1] = 'B', nr[1] = b;
        ord[2] = 'Y', nr[2] = y;
    }
    else if(r <= y && y <= b) {
        ord[0] = 'R', nr[0] = r;
        ord[1] = 'Y', nr[1] = y;
        ord[2] = 'B', nr[2] = b;
    }
    else if(y <= r && r <= b) {
        ord[0] = 'Y', nr[0] = y;
        ord[1] = 'R', nr[1] = r;
        ord[2] = 'B', nr[2] = b;
    }
    else if(y <= b && b <= r) {
        ord[0] = 'Y', nr[0] = y;
        ord[1] = 'B', nr[1] = b;
        ord[2] = 'R', nr[2] = r;
    }
    else if(b <= r && r <= y) {
        ord[0] = 'B', nr[0] = b;
        ord[1] = 'R', nr[1] = r;
        ord[2] = 'Y', nr[2] = y;
    }
    else {
        ord[0] = 'B', nr[0] = b;
        ord[1] = 'Y', nr[1] = y;
        ord[2] = 'R', nr[2] = r;
    }
}

int main() {

    scanf("%d", &nrt);
    for(int t = 1; t <= nrt; ++t) {
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
        printf("Case #%d: ", t);

        if(r + g == n) {
            if(r == g) {
                for(int i = 0; i < n / 2; ++i)
                    printf("RG");
                printf("\n");
            }
            else
                printf("Impossible\n");
            continue;
        }
        if(b + o == n) {
            if(b == o) {
                for(int i = 0; i < n / 2; ++i)
                    printf("BO");
                printf("\n");
            }
            else
                printf("Impossible\n");
            continue;
        }
        if(y + v == n) {
            if(y == v) {
                for(int i = 0; i < n / 2; ++i)
                    printf("YV");
                printf("\n");
            }
            else
                printf("Impossible\n");
            continue;
        }

        string ans;
        string ansb;
        string ansy;
        string ansr;

        if(o > 0) {
            if(b < o + 1) {
                printf("Impossible\n");
                continue;
            }

            b -= o;
            for(int i = 1; i <= o; ++i) {
                ansb.push_back('B');
                ansb.push_back('O');
            }
            ansb.push_back('B');
        }
        if(g > 0) {
            if(r < g + 1) {
                printf("Impossible\n");
                continue;
            }

            r -= g;
            for(int i = 1; i <= g; ++i) {
                ansr.push_back('R');
                ansr.push_back('G');
            }
            ansr.push_back('R');
        }
        if(v > 0) {
            if(y < v + 1) {
                printf("Impossible\n");
                continue;
            }
            
            y -= v;
            for(int i = 1; i <= v; ++i) {
                ansy.push_back('Y');
                ansy.push_back('V');
            }
            ansy.push_back('Y');
        }

        order(r, b, y);
        if(nr[0] + nr[1] < nr[2]) {
            printf("Impossible\n");
            continue;
        }

        while(nr[0] < nr[1]) {
            ans.push_back(ord[2]);
            ans.push_back(ord[1]);
            --nr[2];
            --nr[1];
        }
        assert(nr[2] >= 0);

        int idx = 1;
        while(nr[2] > 0) {
            ans.push_back(ord[2]);
            ans.push_back(ord[idx]);
            --nr[2];
            --nr[idx];
            idx ^= 1;
        }
        assert(nr[0] >= 0 && nr[1] >= 0);

        if(nr[0] > nr[1]) {
            assert(nr[0] == nr[1] + 1);

            for(int i = 0; i < nr[1]; ++i) {
                ans.push_back(ord[0]);
                ans.push_back(ord[1]);
            }
            ans.push_back(ord[0]);
        }
        else {
            assert(nr[0] == nr[1]);

            for(int i = 0; i < nr[0]; ++i) {
                ans.push_back(ord[1]);
                ans.push_back(ord[0]);
            }
        }

        for(int i = 0; i < (int) ans.length(); ++i) {
            if(ans[i] == 'B' && ansb.length() > 0) {
                printf("%s", ansb.c_str());
                ansb.clear();
            }
            else if(ans[i] == 'R' && ansr.length() > 0) {
                printf("%s", ansr.c_str());
                ansr.clear();
            }
            else if(ans[i] == 'Y' && ansy.length() > 0) {
                printf("%s", ansy.c_str());
                ansy.clear();
            }
            else {
                printf("%c", ans[i]);
            }
        }
        printf("\n");
    }

    return 0;
}