#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>

using namespace std;

bool test(double mySpeed, int dist, int count, int *start, int *speed) {
    double myTime = (double)dist / mySpeed;
    for (int i = 0; i < count; ++i) {
        double thisDist = (double)(dist - start[i]);
        double thisTime = thisDist / (double)speed[i];

        if (myTime < thisTime) return false;
    }
    return true;
}

void solve()
{
    int dist;
    int horses;
    int start[1000];
    int speed[1000];
    double maxTime = 0.0;

    scanf("%d%d", &dist, &horses);
    for (int i = 0; i < horses; ++i) {
        scanf("%d%d", &start[i], &speed[i]);
        double thisDist = (double)(dist - start[i]);
        double thisTime = thisDist / (double)speed[i];
        if (thisTime > maxTime) maxTime = thisTime;
    }

    printf(" %6f\n", (double)dist / maxTime);
}

int main(void)
{
    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        printf("Case #%d:", cC + 1);
        solve();
    }

    return 0;
}