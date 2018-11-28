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

#define PROBLEM "B"

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        string s;
        cin >> s;

        int n = s.size();

        for (int i = 1; i < n; i++) {
            if (s[i-1] > s[i]) {
                int k = i-1;
                s[k]--;
                while (k > 0 && s[k-1] > s[k]) {
                    k--;
                    s[k]--;
                }
                for (int j = k+1; j < n; j++) {
                    s[j] = '9';
                }
                break;
            }
        }

        int st = 0;
        while (s[st] == '0') st++;

        for (; st < n; st++) {
            cout << s[st];
        }

        printf("\n");
    }

    return 0;
}
