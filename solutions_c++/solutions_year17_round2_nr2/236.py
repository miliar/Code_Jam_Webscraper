#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cassert>
using namespace std;

const int MAXN = 1000;
const int RED = 0;
const int YELLOW = 1;
const int BLUE = 2;
const int GREEN = 3;
const int VIOLET = 4;
const int ORANGE = 5;

int order[] = {RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET};
char ans[MAXN + 5];
char finalAns[MAXN + 5];
char col[] = "RYBGVO";
int cnt[6];
int ix[6];
int n;

bool cmp(int i1, int i2) {
    return cnt[i1] > cnt[i2];
}

bool solve() {
    int c,c2;
    ix[0] = 0;
    ix[1] = 1;
    ix[2] = 2;
    sort(ix, ix + 3, cmp);
    if (cnt[ix[0]] > cnt[ix[1]] + cnt[ix[2]]) return false;
    else if (cnt[ix[2]] == 0) {
        if (cnt[ix[0]] > cnt[ix[1]]) return false;
        else {
            for (c=0;c<n;c++) ans[c] = col[ix[c & 1]];
            ans[n] = 0;
            return true;
        }
    } else {
        int start = ix[0], prev = -1;
        int C = 0;
        while (sort(ix, ix + 3, cmp), cnt[ix[0]] > 1) {
            int choice = ix[0] != prev ? ix[0] : ix[1];
            ans[C++] = col[choice];
            cnt[choice]--;
            prev = choice;
        }
        if (start == prev) start = (start + 2) % 3;
        ans[C++] = col[start];
        ans[C++] = col[(start + 1) % 3];
        ans[C++] = col[(start + 2) % 3];
        ans[C] = 0;
        return true;
    }
}

bool init() {
    bool good = true;
    for (int c=0;c<3;c++) {
        if (cnt[c] < cnt[c + 3]) return false;
        if (cnt[c] > 0 && cnt[c] == cnt[c + 3]) good &= (n == (cnt[c] << 1));
    }
    if (!good) return false;
    for (int c=0;c<3;c++) {
        cnt[c] -= cnt[c + 3];
        n -= cnt[c + 3] << 1;
    }
    return true;
}

int main() {
    freopen("stable.in","r",stdin);
    freopen("stable.out","w",stdout);
    int c,c2;
    int tests;
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
        scanf("%d",&n);
        for (c=0;c<6;c++)
            scanf("%d",&cnt[order[c]]);
        int N = n;
        if (!init()) {
            printf("Case #%d: IMPOSSIBLE\n",test);
        } else {
            if (n == 0) {
                int which = -1;
                for (c=0;c<3;c++)
                    if (cnt[c + 3])
                        which = c;
                assert(which > -1);
                assert(cnt[which + 3] << 1 == N);
                for (c=0;c<N;c++)
                    ans[c] = col[which + 3 * (c & 1)];
                ans[N] = 0;
                printf("Case #%d: %s\n",test, ans);
            } else if (solve()) {
                int C = 0;
                for (int i = 0; ans[i]; i++) {
                    int j = find(col, col + 3, ans[i]) - col;
                    finalAns[C++] = ans[i];
                    while (cnt[j + 3] > 0) {
                        finalAns[C++] = col[j + 3];
                        finalAns[C++] = col[j];
                        cnt[j + 3]--;
                    }
                }
                finalAns[C] = 0;
                printf("Case #%d: %s\n",test, finalAns);
            } else {
                printf("Case #%d: IMPOSSIBLE\n",test);
            }
        }
    }
    
    
    
    return 0;
}
