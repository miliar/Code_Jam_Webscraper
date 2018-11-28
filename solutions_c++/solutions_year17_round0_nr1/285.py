#define STRINGIZE(x) #x
#define STRINGIZE2(x) STRINGIZE(x)
#define FP STRINGIZE2(FILEPATH)

#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
using namespace std;

const int N = 1000 + 13;

int n, k;
int a[N];

bool read() {
    char s[N];
    if (scanf("%s%d", s, &k) != 2) {
        return false;
    }
    
    n = (int) strlen(s);
    for (int i = 0; i < n; i++) {
        a[i] = s[i] == '+';
    }
    return true;
}

void solve(int test) {
    printf("Case #%d: ", test + 1);
    
    int result = 0;
    for (int i = 0; i + k <= n; i++) {
        if (a[i] == 0) {
            result++;
            for (int j = i; j < i + k; j++) {
                a[j] ^= 1;
            }
        }
    }
    
    if (*min_element(a, a + n) == 0) {
        puts("IMPOSSIBLE");
    } else {
        printf("%d\n", result);
    }
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
