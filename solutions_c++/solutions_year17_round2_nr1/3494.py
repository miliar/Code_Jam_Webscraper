//#include <iostream>
#include <stdio.h>

int main() {
    int nTests, nHorses, posHorse, velHorse;
    long long D;

    long double time, maxTime = 0;
    scanf(" %d", &nTests);
    for(int i = 0; i < nTests; i++) {
        scanf(" %lld %d", &D, &nHorses);
        for (int i = 0; i < nHorses; i++) {
            scanf(" %d %d", &posHorse, &velHorse);
            time = (long double)(D - posHorse) / velHorse;
            if (time > maxTime) {
                maxTime = time;
            }
        }
        printf("Case #%d: %Lf\n", i+1, D/maxTime);
        maxTime = 0;
    }

    return 0;
}