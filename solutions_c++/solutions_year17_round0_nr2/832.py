#define DBG 1

#include <cstring>
#include <map>
#include <unordered_map>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstdio>
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int, int> pii;

int gi() {
    int a;
    scanf("%d", &a);
    return a;
}

ll gli() {
    ll a;
    scanf("%lld", &a);
    return a;
}

char a[22];

#define SINGLELINE 1
void solve() {
    a[0] = '0';
    scanf("%s", &a[1]);

    int l = strlen(a);

    int s = 1;
    for (int i = 0; i < l-1; i++)
        if (a[i] > a[i+1]) {
            if (a[i] == '1') {
                s = 2;
                for (int j = 2; j < l; j++)
                    a[j] = '9';
            } else {
                for (int j = i; j > 0; j--) {
                    if (a[j-1] < a[j]) {
                        a[j]--;
                        for (int k = j+1; k < l; k++)
                            a[k] = '9';
                        break;
                    }
                }
            }
            break;
        }
    printf("%s\n", &a[s]);
}

int main() {
    int t = gi();

    for (int i = 1; i <= t; i++) {
        printf("Case #%d:%c", i, (SINGLELINE ? ' ' : '\n'));
        solve();
        fprintf (stderr, "Case %d / %d. Elapsed %.2f. Estimated %.2f\n", i, t, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / i * t) / CLOCKS_PER_SEC);
    }

    return 0;
}
