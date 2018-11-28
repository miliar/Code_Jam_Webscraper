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
#define MP(a, b) make_pair(a, b)

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;

const int MNOGO = 0x3fffffff;

#define PROBLEM "B"

struct Segment {
    int b, e, c;
    Segment(int _b, int _e, int _c): b(_b), e(_e), c(_c) {}
};

inline bool cmpseg(Segment a, Segment b) {
    if (a.b != b.b) return a.b < b.b;
    return a.e < b.e;
}

const int MAXS = 256;

int a[MAXS][721];

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        int n, m;
        cin >> n >> m;

        vector<Segment> es;

        for (int i = 0; i < n; i++) {
            int b, e;
            cin >> b >> e;
            es.PB(Segment(b, e, 0));
        }

        for (int i = 0; i < m; i++) {
            int b, e;
            cin >> b >> e;
            es.PB(Segment(b, e, 1));
        }

        es.PB(Segment(0, 0, 0));
        es.PB(Segment(1440, 1440, 0));

        int s = n+m;
        stable_sort(es.begin(), es.end(), cmpseg);

        int answer = MNOGO;

        for (int color = 0; color < 2; color++) {
            es[0].c = color;
            es[s+1].c = color;

            for (int i = 0; i <= s+1; i++) {
                for (int t = 0; t <= 720; t++) {
                    a[i][t] = MNOGO;
                }
            }
            a[0][0] = 0;

            for (int i = 1; i <= s+1; i++) {
                for (int t = 0; t <= 720; t++) {
                    int pl = es[i].e - es[i].b;
                    int tp = es[i].b - es[i-1].e;

                    if (es[i].c == 0) {
                        int ps;
                        for (int dt = 0; dt <= tp && t+dt+pl <= 720; dt++) {
                            if (es[i-1].c == 1) ps = 1;
                            else {
                                if (dt == tp) ps = 0;
                                else ps = 2;
                            }

                            if (a[i][t+dt+pl] > a[i-1][t] + ps) {
                                a[i][t+dt+pl] = a[i-1][t] + ps;
                            }
                        }
                    } else {
                        int ps;
                        for (int dt = 0; dt <= tp && t+dt <= 720; dt++) {
                            if (es[i-1].c == 0) ps = 1;
                            else {
                                if (dt == 0) ps = 0;
                                else ps = 2;
                            }

                            if (a[i][t+dt] > a[i-1][t] + ps) {
                                a[i][t+dt] = a[i-1][t] + ps;
                            }
                        }
                    }
                }
            }

//             for (int t = 0; t <= 720; t++) {
//                 cerr << t << ": ";
//                 for (int i = 0; i <= s+1; i++) {
//                     cerr << a[i][t] << " ";
//                 }
//                 cerr << endl;
//             }

            answer = min(answer, a[s+1][720]);
        }

        printf("%d", answer);

        printf("\n");
    }

    return 0;
}
