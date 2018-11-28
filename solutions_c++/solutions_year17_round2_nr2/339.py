#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

long long abs(long long x) {
    if (x < 0) {
        return -x;
    }
    return x;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int n, r, o, y, g, b, v;
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
        if (y == v && r == 0 && o == 0 && g == 0 && b == 0) {
            printf("Case #%d: ", t);
            for (int i = 0; i < y; ++i) {
                printf("YV");
            }
            printf("\n");
            continue;
        }
        if (r == g && y == 0 && o == 0 && v == 0 && b == 0) {
            printf("Case #%d: ", t);
            for (int i = 0; i < y; ++i) {
                printf("RG");
            }
            printf("\n");
            continue;
        }
        if (o == b && r == 0 && v == 0 && g == 0 && y == 0) {
            printf("Case #%d: ", t);
            for (int i = 0; i < y; ++i) {
                printf("BO");
            }
            printf("\n");
            continue;
        }
        vector<string> rs;
        vector<string> ys;
        vector<string> bs;
        string bob = "";
        while (o > 0) {
            if (bob == "") {
                bob += "BOB";
                b -= 2;
                o -= 1;
            } else {
                bob += "OB";
                b -= 1;
                o -= 1;
            }
        }
        if (bob != "") {
            bs.push_back(bob);
        }

        string rgr = "";
        while (g > 0) {
            if (rgr == "") {
                rgr += "RGR";
                r -= 2;
                g -= 1;
            } else {
                rgr += "GR";
                r -= 1;
                g -= 1;
            }
        }
        if (rgr != "") {
            rs.push_back(rgr);
        }

        string yvy = "";
        while (v > 0) {
            if (yvy == "") {
                yvy = "YVY";
                y -= 2;
                v -= 1;
            } else {
                yvy += "VY";
                y -= 1;
                v -= 1;
            }
        }
        if (yvy != "") {
            ys.push_back(yvy);
        }
        if (r < 0 || y < 0 || b < 0) {
            printf("Case #%d: IMPOSSIBLE\n", t);
            continue;
        }

        while (r > 0) {
            rs.push_back("R");
            --r;
        }
        while (y > 0) {
            ys.push_back("Y");
            --y;
        }
        while (b > 0) {
            bs.push_back("B");
            --b;
        }
        if (abs((int) ys.size() - (int) bs.size()) > rs.size()) {
            printf("Case #%d: IMPOSSIBLE\n", t);
            continue;
        }
        if (abs((int) ys.size() - (int) rs.size()) > bs.size()) {
            printf("Case #%d: IMPOSSIBLE\n", t);
            continue;
        }
        if (abs((int) rs.size() - (int) bs.size()) > ys.size()) {
            printf("Case #%d: IMPOSSIBLE\n", t);
            continue;
        }
        printf("Case #%d: ", t);
        while (rs.size() > 0) {
            printf("%s", rs.back().c_str());
            rs.pop_back();
            // Now put separator.
            //
            if (!rs.size()) {
                char pr = 0;
                while (ys.size() || bs.size()) {
                    if (pr == 'b' || (pr != 'y' && ys.size() > bs.size())) {
                        printf("%s", ys.back().c_str());
                        ys.pop_back();
                        pr = 'y';
                    } else {
                        printf("%s", bs.back().c_str());
                        bs.pop_back();
                        pr = 'b';
                    }
                }
            } else {
                if (ys.size() > bs.size()) {
                    printf("%s", ys.back().c_str());
                    ys.pop_back();
                } else {
                    printf("%s", bs.back().c_str());
                    bs.pop_back();
                }
            }
        }
        printf("\n");
    }
    return 0;
}

