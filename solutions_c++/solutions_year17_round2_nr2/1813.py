#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int t, tc = 0, n, color[6], isImm, maxi, mid, mini;
    char maxich, midch, minich;
    scanf("%d", &t);
    while (t--) {
        scanf("%d %d %d %d %d %d %d", &n, &color[0], &color[1], &color[2], &color[3], &color[4], &color[5]);
        isImm = 0;
        maxi = 0;
        for (int i = 0; i < 6; ++i) {
            if (color[i] > n / 2) {
                isImm = 1;
                break;
            }
            maxi = color[i] > maxi ? color[i] : maxi;
        }
        if (isImm) {
            printf("Case #%d: IMPOSSIBLE\n", ++tc);
            continue;
        }
        if (maxi == color[0]) {
            maxich = 'R';
            if (color[2] >= color[4]) {
                mid = color[2], midch = 'Y';
                mini = color[4], minich = 'B';
            } else {
                mid = color[4], midch = 'B';
                mini = color[2], minich = 'Y';
            }
        } else if (maxi == color[2]) {
            maxich = 'Y';
            if (color[0] >= color[4]) {
                mid = color[0], midch = 'R';
                mini = color[4], minich = 'B';
            } else {
                mid = color[4], midch = 'B';
                mini = color[0], minich = 'R';
            }
        } else {
            maxich = 'B';
            if (color[0] >= color[2]) {
                mid = color[0], midch = 'R';
                mini = color[2], minich = 'Y';
            } else {
                mid = color[2], midch = 'Y';
                mini = color[0], minich = 'R';
            }
        }
        int l = mini - (maxi - mid);
        printf("Case #%d: ", ++tc);
        while (maxi--) {
            printf("%c", maxich);
            if (mid) {
                printf("%c", midch);
                mid--;
                if (l) {
                    printf("%c", minich);
                    mini--;
                    l--;
                }
                continue;
            }
            if (mini) {
                printf("%c", minich);
                mini--;
            }
        }
        putchar(10);
    }
    return 0;
}