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

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        string s;
        int k;
        cin >> s >> k;

        int n = s.size();

        int answer = 0;
        for (int i = 0; i < n-k+1; i++) {
            if (s[i] == '-') {
                for (int j = i; j < i+k; j++) {
                    s[j] = (s[j] == '-') ? '+' : '-';
                }
                answer++;
            }
        }

        bool ok = true;
        for (int i = 0; i < n; i++) {
            ok = ok && (s[i] == '+');
        }

        if (ok) {
            printf("%d", answer);
        } else {
            printf("IMPOSSIBLE");
        }

        printf("\n");
    }

    return 0;
}
