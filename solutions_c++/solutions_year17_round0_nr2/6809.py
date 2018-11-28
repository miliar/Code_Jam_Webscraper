#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <cstdio>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <math.h>
#define ll long long
#define int64 long long
#define ull unsigned long long
#define pb push_back
#define INF 0x3f3f3f3f
#define lson l, mid, rt<<1
#define rson mid+1, r, rt<<1|1

using namespace std;

const int maxn = 25;
const int mod = 1e9 + 7 ;
char s[maxn];
int len;

int main() {
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int T ;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++) {
        scanf("%s", s);
        int len = strlen(s);
        //printf("%s\n", s);
        for (int i = len - 1; i >= 1; i--) {
            if (s[i] < s[i - 1]) {
                for (int j = i; j < len; j++) {
                    s[j] = '9';
                }
                s[i - 1]--;
            }
        }
        int i;
        for (i = 0; i < len; i++) {
            if (s[i] != '0') break;
        }
        printf("Case #%d: %s\n", tt, s + i);
    }
    return 0 ;
}
