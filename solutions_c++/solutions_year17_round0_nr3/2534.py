#include <bits/stdc++.h>

using namespace std;

long long n, k;
long long len[2][100], num[2][100];
int step;

void init(int i) {
    len[0][i] = 0;
    len[1][i] = 0;
    num[0][i] = 0;
    num[1][i] = 0;
}

void update(long long x, long long y) {
    if (!len[0][step + 1]) {
        len[0][step + 1] = x;
        num[0][step + 1] = y;
        return;
    }
    if (x == len[0][step + 1]) num[0][step + 1] = num[0][step + 1] + y;
    else {
        len[1][step + 1] = x;
        num[1][step + 1] = num[1][step + 1] + y;
    }
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        printf("Case #%d: ", tt);
        cin >> n >> k;
        step = 0;
        len[0][step] = n;
        num[0][step] = 1;
        len[1][step] = 0;
        num[1][step] = 0;
        while (k > num[0][step] + num[1][step]) {
            init(step + 1);
            if (len[0][step]) {
                update(len[0][step] - 1 - ((len[0][step] - 1) / 2), num[0][step]);
                update((len[0][step] - 1) / 2, num[0][step]);
            }
            if (len[1][step]) {
                update(len[1][step] - 1 - ((len[1][step] - 1) / 2), num[1][step]);
                update((len[1][step] - 1) / 2, num[1][step]);
            }
            k = k - (num[0][step] + num[1][step]);
            step++;
            if (len[0][step] < len[1][step]) {
                swap(len[0][step], len[1][step]);
                swap(num[0][step], num[1][step]);
            }
        }
        if (k <= num[0][step]) cout << len[0][step] - 1 - ((len[0][step] - 1) / 2) << " " << (len[0][step] - 1) / 2 << endl;
        else cout << len[1][step] - 1 - ((len[1][step] - 1) / 2) << " " << (len[1][step] - 1) / 2 << endl;

    }
}
