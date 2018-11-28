#include <cstdio>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#define MAX_N 1005
#define ll __int64

using namespace std;

string s;
int N, K;
int dir[MAX_N];
int f[MAX_N];

int main()
{
   // freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w+", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i<= T; i++) {
        cin >> s;
        scanf("%d", &K);
        N = s.size();
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '+') {
                dir[i] = 0;
            } else {
                dir[i] = 1;
            }
        }
        int sum = 0;
        int ans = 0;
        memset(f, 0, sizeof(f));
        for (int i = 0; i + K <= N; i++) {
            if ((sum + dir[i]) % 2 != 0) {
                ans++;
                f[i] = 1;
            }
            sum += f[i];
            if (i - K + 1 >= 0) {
                sum -= f[i-K+1];
            }
        }

        for (int i = N - K + 1; i < N; i++) {
            if ((sum + dir[i]) % 2 != 0) {
                ans = -1;
            }
            sum += f[i];
            if (i - K + 1 >= 0) {
                sum -= f[i-K+1];
            }
        }



        if (ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", i);
        } else {
            printf("Case #%d: %d\n", i, ans);
        }
    }


    return 0;
}
