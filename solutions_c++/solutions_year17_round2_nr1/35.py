#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>
using namespace std;

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        int d, n;
        scanf("%d%d", &d, &n);
        vector<int> K(n), S(n);
        double answer = 1e100;
        for (int i = 0; i < n; ++ i) {
            scanf("%d%d", &K[i], &S[i]);
            double ti = (d - K[i]) / (double)S[i];
            answer = min(answer, d / ti);
        }
        printf("Case #%d: %.10f\n", test, answer);
    }
    return 0;
}
