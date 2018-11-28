#define STRINGIZE(x) #x
#define STRINGIZE2(x) STRINGIZE(x)
#define FP STRINGIZE2(FILEPATH)

#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
using namespace std;

const int N = 1000 + 3;

int d, n;
int k[N], s[N];

bool read() {
    if (scanf("%d%d", &d, &n) != 2) {
        return false;
    }
    
    for (int i = 0; i < n; i++) {
        assert(scanf("%d%d", &k[i], &s[i]) == 2);
    }
    
    return true;
}

void solve(int test) {
    printf("Case #%d: ", test + 1);
    
    double maxT = -1;
    for (int i = 0; i < n; i++) {
        maxT = max(maxT, (d - k[i]) / double(s[i]));
    }
    
    double ans = d / maxT;
    printf("%.10f\n", ans);
}

int main() {
    freopen(FP "input.txt", "rt", stdin);
    freopen(FP "output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    for (int test = 0; test < testCount; test++) {
        assert(read());
        solve(test);
    }
    
    return 0;
}
