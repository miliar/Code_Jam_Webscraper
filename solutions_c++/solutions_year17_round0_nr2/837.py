#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

char bit[N];

void _main() {
    scanf("%s", bit);
    int n = strlen(bit);
    reverse(bit, bit + n);
    for (int i = 0; i + 1 < n; ++i) {
        if (bit[i] < bit[i + 1]) {
            for(int j = 0; j <= i; ++j) bit[j] = '9';
            bit[i + 1] -= 1;
        }
    }
    while (bit[n - 1] == '0') bit[n - 1] = 0, n--;
    reverse(bit, bit + n);
    cout << bit << endl;
}
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, cas = 0;
    for (scanf("%d", &t); t--; ) {
        printf("Case #%d: ", ++cas);
        _main();
    }
    return 0;
}
