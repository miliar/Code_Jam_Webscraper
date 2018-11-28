#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define PB(x) push_back(x)
#define MP(a, b) make_pair(a, b)

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;

// const int MNOGO = 0x3fffffff;

#define PROBLEM "A"

int a[10];

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        memset(a, 0, sizeof a);

        int n, p;
        cin >> n >> p;

        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            a[x % p]++;
        }

        if (p == 2) {
            int answer = a[0] + (a[1] + 1) / 2;
            printf("%d", answer);
        } else if (p == 3) {
            int answer = a[0];
            int min12 = min(a[1], a[2]);
            int max12 = max(a[1], a[2]);
            answer += min12;

            int left = max12 - min12;
            answer += (left + 2) / 3;
            printf("%d", answer);
        } else if (p == 4) {
            int answer = a[0];
            int min13 = min(a[1], a[3]);
            int max13 = max(a[1], a[3]);

            answer += min13;
            int left13 = max13 - min13;

            answer += a[2] / 2;
            int left2 = a[2] % 2;

            if (left2 == 0) {
                answer += (left13 + 3) / 4;
            } else {
                if (left13 >= 2) {
                    answer++;
                    left13 -= 2;
                    answer += (left13 + 3) / 4;
                } else {
                    answer++;
                }
            }
            printf("%d", answer);
        }

        printf("\n");
    }

    return 0;
}
