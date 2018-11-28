#ifndef A_CPP_INCLUDED
#define A_CPP_INCLUDED

using namespace std;

#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <string.h>
#include <math.h>
#include <stdlib.h>

typedef pair<int, int> ii;
typedef vector<int> vi;

int t, n, k;
string line;
int s[1005];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.txt", "w", stdout);
    scanf("%d", &t);
    for (int r = 1; r <= t; r++) {
        cin >> line;
        n = (int)line.size();
        for (int i = 0; i < n; i++) {
            s[i] = ((line[i] == '+') ? 1: 0);
        }
        scanf("%d", &k);
        int ans = 0;
        for (int i = 0; i <= n - k; i++) {
            if (s[i] == 0) {
                ans++;
                for (int j = i; j < i + k; j++) {
                    s[j] = 1-s[j];
                }
            }
        }
        bool ok = true;
        for (int i = 0; i < n; i++) {
            if (s[i] != 1) {
                ok = false;
                break;
            }
        }
        printf("Case #%d: ", r);
        if (ok) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
}


#endif // A_CPP_INCLUDED
