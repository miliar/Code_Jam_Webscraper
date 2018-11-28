#include <cstdio>

void testcase() {
    int dest, horseCount;

    scanf("%d %d", &dest, &horseCount);
    double bestTime;
    for (int i = 0; i < horseCount; i++) {
        int startPos, maxSpeed;
        scanf("%d %d", &startPos, &maxSpeed);
        double candidateTime = (dest - startPos) / (double)maxSpeed;
        if (i == 0 || candidateTime > bestTime) {
            bestTime = candidateTime;
        }
    }
    printf("%lf\n", dest / bestTime);
}

int main() {
    int tc, t;

    scanf("%d", &tc);
    for (t = 1; t <= tc; t++) {
        printf("Case #%d: ", t);
        testcase();
    }
    return 0;
}
