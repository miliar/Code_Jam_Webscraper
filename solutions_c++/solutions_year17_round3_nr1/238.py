#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;

typedef long long LL;

const long double pi = 3.141592653589793;
struct Pancake{
    int R, H;
    bool operator < (const Pancake &rhs) const {
        if (R == rhs.R) return H > rhs.H;
        else return R > rhs.R;
    }
};

int T, cas = 1;
int N, K;

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    while (cas <= T) {
        scanf("%d %d", &N, &K);
        vector<Pancake> pancake;
        for (int i = 0; i < N; i++) {
            Pancake x;
            scanf("%d %d", &x.R, &x.H);
            pancake.push_back(x);
        }
        sort(pancake.begin(), pancake.end());
        long double ans = 0.0;
        for (int i = 0; i < N - K + 1; i++) {
            long double cur = (long double)pancake[i].R * (long double)pancake[i].R + 2.0 * (long double)pancake[i].R * (long double)pancake[i].H;
            vector<long double> side;
            for (int j = i + 1; j < N; j++) {
                side.push_back(2.0 * (long double)pancake[j].R * (long double)pancake[j].H);
            }
            sort(side.begin(), side.end());
            for (int j = (int)side.size() - 1; (int)side.size() - j <= K - 1; j--)
                cur += side[j];
            ans = max(ans, cur);
        }
        printf("Case #%d: %.9Lf\n", cas, ans * pi);
        cas++;
    }
    return 0;
}