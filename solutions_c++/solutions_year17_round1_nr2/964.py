#include <bits/stdc++.h>
#include <cmath>
#include <cassert>

#define MAXN 60

using namespace std;
typedef pair<int, int> TwoIntPairType;

const int INF = ~0U>>1;
int R[MAXN];

vector <TwoIntPairType> vecs[MAXN];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int caseCnt;
    scanf("%d", &caseCnt);
    int caseNow = 0;
    while (caseNow < caseCnt) {
        ++caseNow;
        printf("Case #%d: ", caseNow);
        int N, P;
        scanf("%d%d", &N, &P);
        for (int i = 0; i < N; ++i) {
            scanf("%d", &R[i]);
        }
        for (int i = 0; i < N; ++i) {
            int arr[MAXN];
            for (int j = 0; j < P; ++j) {
                scanf("%d", &arr[j]);
            }
            sort(arr, arr + P);
            vecs[i].clear();
            for (int j = 0; j < P; ++j) {
                double lDouble = arr[j] / (1.1 * R[i]);
                double rDouble = arr[j] / (0.9 * R[i]);
                int lValue = ceil(lDouble);
                int rValue = floor(rDouble);
                assert(floor(3.0) == 3
                    && ceil(3.0) == 3
                    && floor(2.7) == 2
                    && ceil(2.7) == 3);
                vecs[i].push_back({lValue, rValue});
            }
        }
        int ans = 0;
        while (true) {
            int flag = 1;
            int minValue = INF;
            for (int i = 0; i < N; ++i) {
                if (vecs[i].empty()) {
                    flag = 0;
                    break;
                }
                TwoIntPairType tmp = vecs[i].back();
                minValue = min(minValue, tmp.second);
            }
            if (flag == 0) {
                break;
            }

            int canThisFlag = 1;
            for (int i = 0; i < N; ++i) {
                while ((!vecs[i].empty()) && vecs[i].back().first > minValue) {
                    vecs[i].pop_back();
                    canThisFlag = 0;
                }
            }

            if (!canThisFlag) {
                continue;
            }

            ans ++;
            for (int i = 0; i < N; ++i) {
                assert(vecs[i].back().first <= minValue
                    && vecs[i].back().second >= minValue);
                vecs[i].pop_back();
            }
        }

        printf("%d\n", ans);
    }
    return 0;
}
