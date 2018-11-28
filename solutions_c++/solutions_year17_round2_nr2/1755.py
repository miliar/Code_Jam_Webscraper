#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

int n, co[6], ct;
bool finished;
char output[10000];
char str[] = "ROYGBV";

bool is_ok_small() {
    if (ct == 1) {
        for (int i = 0; i < 6; i++) {
            if (co[i] > 0 && co[i] == 1) {
                return true;
            }
        }
    } else if (ct == 2) {
        int cc[2] = {0};
        for (int i = 0, j = 0; i < 6; i++) {
            if (co[i] > 0) {
                cc[j++] = co[i];
            }
        }
        if (cc[0] == cc[1]) {
            return true;
        }
    } else if (ct == 3) {
        std::vector<int> V;
        for (int i = 0; i < 6; i++) {
            if (co[i] > 0)
                V.push_back(co[i]);
        }
        std::sort(V.rbegin(), V.rend());
        if (V[0] <= V[1]+V[2])
            return true;
    }
    return false;
}

char _get_ch(int i) {
    if (i >= 0 && i <= 5)
        return str[i];
    return 'X';
}

bool ve(char a, char b) {
    //printf("TEST |%c| |%c|\n", a, b);
    if (a == 0 || b == 0)
        return true;
    if (a == 'R' && (b == 'Y' || b == 'G' || b == 'B')) {
        return true;
    } else if (a == 'O' && b == 'B') {
        return true;
    } else if (a == 'Y' && (b == 'R' || b == 'B' || b == 'V')) {
        return true;
    } else if (a == 'G' && b == 'R') {
        return true;
    } else if (a == 'B' && (b == 'R' || b == 'O' || b == 'Y')) {
        return true;
    } else if (a == 'V' && b == 'Y') {
        return true;
    }
    return false;
}
bool test_o(int loc, char c) {
    if (loc == 0)
        return true;
    if (ve(output[(loc+1)%n], c) && ve(output[loc-1], c)) {
        return true;
    }
    return false;
}

void solve(int lv) {
    //printf("LV = %d, CO = [", lv);
    //for (int i = 0; i < 6; i++) {
        //printf("%d ", co[i]);
    //}
    //printf("]\n");
    if (lv == n || finished) {
        if (output[n-1] == output[0]) {
            //printf("LOOP\n");
            finished = false;
        } else {
            //printf("NON-LOOP\n");
            if (!finished) {
                printf("%s\n", output);
                //printf("STRLEN = %d\n", strlen(output));
                //printf("N = %d\n", n);
            }
            finished = true;
        }
        return;
    }
    std::vector<std::pair<int, int> > V;
    for (int i = 0; i < 6; i++) {
        V.push_back(std::pair<int, int>(co[i], i));
    }
    std::sort(V.rbegin(), V.rend());
    for (int i = 0; i < 6; i++) {
        std::pair<int, int> P = V[i];
        if (P.first > 0 && test_o(lv, _get_ch(P.second))) {
            output[lv] = _get_ch(P.second);
            co[P.second]--;
            //printf("DEBUG===\n");
            //printf("LV = %d\n", lv);
            //printf("gc = %c\n", _get_ch(i));
            //printf("output = |%s|\n", output);
            solve(lv+1);
            co[P.second]++;
        }
        if (finished)
            break;
        output[lv] = 0;
    }
}
int main() {
    int T;
    scanf("%d", &T);
    for (int tt=1; tt <= T; tt++) {
        memset(output, 0, sizeof output);
        finished = false;
        scanf("%d", &n);
        ct = 0;
        for (int i = 0; i < 6; i++) {
            scanf("%d", &co[i]);
            if (co[i] > 0) ct++;
        }
        printf("Case #%d: ", tt);

        if (is_ok_small()) {
            solve(0);
            //printf("%s\n", output);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
