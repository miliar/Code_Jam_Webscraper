#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define PB(x) push_back(x)
#define SZ() size()
#define MP(a, b) make_pair(a, b)

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;

// const int MNOGO = 0x3fffffff;

#define PROBLEM "B"

bool check(char a, char b) {
    if (a == 'R') return b == 'Y' || b == 'B' || b == 'G';
    if (a == 'Y') return b == 'R' || b == 'B' || b == 'V';
    if (a == 'B') return b == 'R' || b == 'Y' || b == 'O';
    if (a == 'O') return b == 'B';
    if (a == 'G') return b == 'R';
    if (a == 'V') return b == 'Y';
    return false;
}

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;

        vector<string> reds, yellows, blues;

        if (o + b == n) {
            if (o == b) {
                for (int k = 1; k <= n; k+=2) {
                    printf("OB");
                }
            } else {
                printf("IMPOSSIBLE");
            }
            printf("\n"); continue;
        }

        if (g + r == n) {
            if (g == r) {
                for (int k = 1; k <= n; k+=2) {
                    printf("GR");
                }
            } else {
                printf("IMPOSSIBLE");
            }
            printf("\n"); continue;
        }

        if (v + y == n) {
            if (v == y) {
                for (int k = 1; k <= n; k+=2) {
                    printf("VY");
                }
            } else {
                printf("IMPOSSIBLE");
            }
            printf("\n"); continue;
        }

        if (o > 0) {
            if (b < o+1) {
                printf("IMPOSSIBLE");
                printf("\n"); continue;
            }
            string t = "B";
            b--;
            for (int k = 0; k < o; k++) {
                t += "OB";
                b--;
            }
            blues.PB(t);
        }
        if (g > 0) {
            if (r < g+1) {
                printf("IMPOSSIBLE");
                printf("\n"); continue;
            }
            string t = "R";
            r--;
            for (int k = 0; k < g; k++) {
                t += "GR";
                r--;
            }
            reds.PB(t);
        }
        if (v > 0) {
            if (y < v+1) {
                printf("IMPOSSIBLE");
                printf("\n"); continue;
            }
            string t = "Y";
            y--;
            for (int k = 0; k < v; k++) {
                t += "VY";
                y--;
            }
            yellows.PB(t);
        }

        for (int k = 0; k < b; k++) {
            blues.PB("B");
        }
        for (int k = 0; k < r; k++) {
            reds.PB("R");
        }
        for (int k = 0; k < y; k++) {
            yellows.PB("Y");
        }

        int nn = blues.SZ() + reds.SZ() + yellows.SZ();
        if (blues.SZ() > nn / 2 || reds.SZ() > nn / 2 || yellows.SZ() > nn / 2) {
            printf("IMPOSSIBLE");
            printf("\n"); continue;
        }

        vector<string> xs[3];
        xs[0] = reds;
        xs[1] = blues;
        xs[2] = yellows;

        if (xs[2].size() > xs[1].size()) {
            vector<string> t = xs[1];
            xs[1] = xs[2];
            xs[2] = t;
        }
        if (xs[1].size() > xs[0].size()) {
            vector<string> t = xs[1];
            xs[1] = xs[0];
            xs[0] = t;
        }
        if (xs[2].size() > xs[1].size()) {
            vector<string> t = xs[1];
            xs[1] = xs[2];
            xs[2] = t;
        }


        vector<string> answer;
        for (int i = 0; i < xs[0].size() * 2; i++) answer.PB("");

        for (int k = 0; k < xs[0].size(); k++) {
            answer[k*2] = xs[0][k];
        }
        int pos = 1;
        for (int k = 0; k < xs[1].size(); k++) {
            assert(answer[pos] == "");
            answer[pos] = xs[1][k];
            pos += 2;
        }
        int pk = 0;
        while (pk < xs[2].size() && pos < xs[0].size() * 2) {
            assert(answer[pos] == "");
            answer[pos] = xs[2][pk++];
            pos += 2;
        }

        assert(answer.size() >= xs[2].size() - pk);
        vector<string> answer2;
        pos = 0;
        while (pk < xs[2].size()) {
            answer2.PB(answer[pos++]);
            answer2.PB(xs[2][pk++]);
        }
        while (pos < answer.size()) {
            answer2.PB(answer[pos++]);
        }

//         vector<string> *last_target = NULL;
//         vector<string> answer;
//         for (int i = 0; i < nn; i++) {
//             vector<string> empty;
//             vector<string> *target = &empty;
//
//             if (last_target != &yellows && yellows.size() > (*target).size()) {
//                 target = &yellows;
//             }
//             if (last_target != &reds && reds.size() > (*target).size()) {
//                 target = &reds;
//             }
//             if (last_target != &blues && blues.size() > (*target).size()) {
//                 target = &blues;
//             }
//
//             answer.PB((*target)[(*target).size() - 1]);
//             (*target).pop_back();
//             last_target = target;
//         }


        string result = "";
        for (int i = 0; i < answer2.size(); i++) {
            result += answer2[i];
        }

        for (int i = 0; i < result.size(); i++) {
            if (!check(result[i], result[(i+1) % result.size()])) {
                cerr << "!!!!!!!" << endl;
                cerr << "PROBLEM! " << result << " " << i << endl;
                cerr << "!!!!!!!" << endl;
            }
        }

        cout << result;
        printf("\n");
    }

    return 0;
}
