#include <bits/stdc++.h>

#define sz(a) (int)a.size()

using namespace std;

const int DAY = 1440;
const int HALF = 720;

struct event {
    int l, r;
    int type;

    event() {}
    event(int l, int r, int type) : l(l), r(r), type(type) {}

    bool operator < (const event &e) const {
        return l < e.l;
    }
};

int main() {
    freopen("text.in", "r", stdin);
    freopen("text.out", "w", stdout);
    int tests;
    scanf("%d", &tests);
    for (int tn = 0; tn < tests; tn++) {
        printf("Case #%d: ", tn + 1);
        int ac, aj;
        scanf("%d%d", &ac, &aj);
        vector<vector<vector<int>>> dp(DAY + 1, vector<vector<int>>(DAY + 1, vector<int>(2)));
        vector<event> events;
        for (int i = 0; i < ac + aj; i++) {
            int l, r;
            scanf("%d%d", &l, &r);
            events.emplace_back(l, r, i < ac ? 0 : 1);
        }
        sort(events.begin(), events.end());
        if (events.size() == 1) {
            if (events[0].l >= HALF || events[0].r <= HALF) {
                printf("2\n");
            } else {
                printf("2\n");
            }
            continue;
        }
        if (events.size() == 2) {
            if (events[0].l >= HALF || events[1].r <= HALF) {
                printf("2\n");
            } else {
                int x = 0;
                int y = 0;
                for (int i = 0; i < sz(events); i++) {
                    if (events[i].type == 0) x += events[i].r - events[i].l;
                    if (events[i].type == 1) y += events[i].r - events[i].l;
                }
                int answer = INT_MAX;
                for (int A = 0; A <= events[0].l; A++) {
                    for (int B = events[0].r; B <= events[1].l; B++) {
                        for (int C = events[1].r; C <= DAY; C++) {
                            int xx = x;
                            int yy = y;
                            if (events[0].type == 0) {
                                xx += events[0].l - A;
                                yy += A;
                            } else {
                                yy += events[0].l - A;
                                xx += A;
                            }
                            if (events[0].type == 0) {
                                xx += B - events[0].r;
                            } else {
                                yy += B - events[0].r;
                            }
                            if (events[1].type == 0) {
                                xx += events[1].l - B;
                            } else {
                                yy += events[1].l - B;
                            }
                            if (events[1].type == 0) {
                                xx += C - events[1].r;
                                yy += DAY - C;
                            } else {
                                yy += C - events[1].r;
                                xx += DAY - C;
                            }
                            int new_ans = 1 + (A == 0 ? 0 : 1) + (C == DAY ? 0 : 1);
                            if (events[0].type == events[1].type) new_ans--;
                            int beg = A == 0 ? events[0].type : 1 - events[0].type;
                            int end = C == DAY ? events[1].type : 1 - events[1].type;
                            if (beg != end) new_ans++;
                            if (xx == HALF && yy == HALF) {
                                answer = min(answer, new_ans);
                            }
                        }
                    }
                }
                if (events[0].type == events[1].type) {
                    for (int A = 0; A <= events[0].l; A++) {
                            for (int C = events[1].r; C <= DAY; C++) {
                                int xx = x;
                                int yy = y;
                                if (events[0].type == 0) {
                                    xx += events[0].l - A;
                                    yy += A;
                                } else {
                                    yy += events[0].l - A;
                                    xx += A;
                                }
                                if (events[1].type == 0) {
                                    xx += C - events[1].r;
                                    yy += DAY - C;
                                } else {
                                    yy += C - events[1].r;
                                    xx += DAY - C;
                                }
                                if (events[0].type == 0) {
                                    if (yy < HALF && events[1].l - events[0].r + yy >= HALF) {
                                        yy = HALF;
                                        xx = HALF;
                                    }
                                } else {
                                    if (xx < HALF && events[1].l - events[0].r + xx >= HALF) {
                                        xx = HALF;
                                        yy = HALF;
                                    }
                                }
                                int new_ans = 2 + (A == 0 ? 0 : 1) + (C == DAY ? 0 : 1);
                                int beg = A == 0 ? events[0].type : 1 - events[0].type;
                                int end = C == DAY ? events[1].type : 1 - events[1].type;
                                if (beg != end) new_ans++;
                                if (xx == HALF && yy == HALF) {
                                    answer = min(answer, new_ans);
                                }
                            }
                    }
                }
                answer = min(answer, 5);
                printf("%d\n", answer);
            }
        }
    }
    return 0;
}
