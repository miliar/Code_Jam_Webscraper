#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxn = 2000;
int N, dir[maxn], f[maxn];
string str;

int calc(int k) {
    memset(f,0, sizeof(f));
    int res = 0;
    int sum = 0;
    for (int i = 0; i + k <= N; i++) {
        if ((dir[i] + sum) % 2 != 0) {
            res++;
            f[i] = 1;
        }
        sum += f[i];
        if (i - k + 1 >= 0) {
            sum -= f[i - k +1];
        }
    }
    for (int i = N - k + 1; i < N; i++) {
        if ((dir[i] + sum) % 2 != 0) return -1;
        if (i - k + 1 >= 0) sum -= f[i - k + 1];
    }
    return res;
}

int main() {
    int T, k;
    scanf("%d", &T);
    for (int c = 1; c <= T; c++) {
        cin >> str >> k;
        N = str.length();
        for (int i = 0; i < N; i++) {
            if (str[i] == '+') dir[i] = 0;
            else dir[i] = 1;
        }
        int res = calc(k);
        if (res == -1) printf("Case #%d: IMPOSSIBLE\n", c);
        else printf("Case #%d: %d\n", c, res);
    }
    return 0;
}