/*
 * tesuji
 * Google Code Jam 2017
 */

#include <algorithm>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <map>
#include <set>
using namespace std;

int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    
    for (int TC = 1; TC <= T; ++TC) {
        int N, K;
        scanf("%d %d", &N, &K);

        double l = log2(K);
        int level = floor((int)l);
        int layer = pow(2, level);
        int freeS = N - (layer - 1);

        int gS = freeS / layer;
        int posK = K - layer;

        if (posK < (freeS % layer)) {
            ++gS;
        }

        int minLR = gS / 2;
        int maxLR = minLR;
        
        if (gS % 2 == 0) {
            minLR = maxLR - 1;
        }

        printf("Case #%d: %d %d\n", TC, maxLR, minLR);
    }
}
