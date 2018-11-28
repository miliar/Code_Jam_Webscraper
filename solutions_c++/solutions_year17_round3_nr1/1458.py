#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

const double PI = 3.14159265358979323846;

struct Pancake {
    int64_t r;
    int64_t h;
    bool used;

    bool operator< (const Pancake& q) const {
        return r * h > q.r * q.h;
    }
};

double solve(int N, int K, vector<Pancake>& pancakes) {
    int64_t maxCover = numeric_limits<int64_t>::min();
    sort(pancakes.begin(), pancakes.end());

    for (int i = 0; i < N; ++i) {
        pancakes[i].used = true;

        int usedCount = 1;
        int64_t currentCover = pancakes[i].r * pancakes[i].r + 2 * pancakes[i].r * pancakes[i].h;
        for (int x = 0; x < N && usedCount < K; ++x) {
            if (!pancakes[x].used && pancakes[x].r <= pancakes[i].r) {
                currentCover += 2 * pancakes[x].r * pancakes[x].h;
                ++usedCount;
            }
        }

        maxCover = max(maxCover, currentCover);
        pancakes[i].used = false;
    }

    return maxCover * PI;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N, K;
        cin >> N >> K;
        vector<Pancake> pancakes(N);
        for (int i = 0; i < N; ++i) {
            cin >> pancakes[i].r >> pancakes[i].h;
            pancakes[i].used = false;
        }

        cout.precision(17);
        cout << "Case #" << t << ": " << solve(N, K, pancakes) << endl;
    }
    return 0;
}
