#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#ifdef __linux__
    #define I64d "%lld"
#else
    #define I64d "%I64d"
#endif

typedef long long int int64;



int main() {
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        int D, N;
        scanf("%d %d", &D, &N);
        vector<pair<int, int> > h;
        int64 a = 0, b = 1;
        for (int i = 0; i < N; i++) {
            int64 p, v;
            scanf(I64d""I64d, &p, &v);
            if ((D - p) * b > v * a) {
                a = D - p;
                b = v;
            }
        }
        printf("Case #%d: %.15lf\n", test + 1,  D * 1.0 * b * 1.0 / a);
    }

    return 0;
}
