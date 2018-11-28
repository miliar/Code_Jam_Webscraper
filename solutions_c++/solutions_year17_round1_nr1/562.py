#define _CRT_SECURE_NO_WARNINGS

#include <cstring>
#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

bool match(int x) {
    return x == '?' || x <= 'Z' && x >= 'A';
}

int get_char() {
    int ch;
    do {
        ch = getchar();
    } while (!match(ch));
    return ch;
}

struct Rect {
    int ch;
    int ch_x;
    int ch_y;

    int x_min;
    int x_max;
    int y_min;
    int y_max;

    bool in_range(const Rect& r) const {
        if (ch_x < r.x_min || ch_x > r.x_max ||
            ch_y < r.y_min || ch_y > r.y_max)
            return false;
        return true;
    }
};

void solve() {
    int n, m;
    vector<Rect> result;
    scanf("%d%d", &n, &m);
    for (int x = 0; x < n; ++x) {
        for (int j = 0; j < m; ++j) {
            int ch = get_char();
            if (ch != '?') {
                Rect r;
                r.ch = ch;
                r.ch_x = x;
                r.ch_y = j;
                result.push_back(r);
            }
        }
    }

    result[0].x_min = 0;
    result[0].x_max = n - 1;
    result[0].y_min = 0;
    result[0].y_max = m - 1;

    for (int j = 1; j < int(result.size()); ++j) {
        for (int i = 0; i < j; ++i) {
            if (result[j].in_range(result[i])) {
                if (result[j].ch_x == result[i].ch_x) {
                    // split by y
                    result[j].x_min = result[i].x_min;
                    result[j].x_max = result[i].x_max;

                    if (result[j].ch_y < result[i].ch_y) {
                        result[j].y_min = result[i].y_min;
                        result[j].y_max = result[i].ch_y - 1;
                        result[i].y_min = result[i].ch_y;
                    }
                    else {
                        result[j].y_min = result[j].ch_y;
                        result[j].y_max = result[i].y_max;
                        result[i].y_max = result[j].ch_y - 1;
                    }
                }
                else {
                    // split by x
                    result[j].y_min = result[i].y_min;
                    result[j].y_max = result[i].y_max;

                    if (result[j].ch_x < result[i].ch_x) {
                        result[j].x_min = result[i].x_min;
                        result[j].x_max = result[i].ch_x - 1;
                        result[i].x_min = result[i].ch_x;
                    }
                    else {
                        result[j].x_min = result[j].ch_x;
                        result[j].x_max = result[i].x_max;
                        result[i].x_max = result[j].ch_x - 1;
                    }
                }
            }
        }
    }

    char board[32][32];
    memset(board, '?', sizeof(board));
    for (const auto& rect : result) {
        for (int i = rect.x_min; i <= rect.x_max; ++i) {
            for (int j = rect.y_min; j <= rect.y_max; ++j) {
                board[i][j] = rect.ch;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j)
            putchar(board[i][j]);
        putchar('\n');
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d:\n", i);
        solve();
    }
}
