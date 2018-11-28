#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000000;
// double EPS = 1e-12;
const int MOD = 1000000007;


int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, k;
    int n;
    char str[1010];
    scanf("%d", &t);
    for (int tt=0 ; tt<t ; tt++) {
        scanf(" %s", str);
        n = strlen(str);
        int i=0;
        for (i=0 ; i<n-1 ; i++) {
            if (str[i] > str[i+1]) {
                break;
            }
        }
        if (i<n-1) {
            int j=i;
            while (j>=1) {
                if (str[j] == '0') {
                    str[j] = '9';
                    j--;
                }
                else {
                    str[j]--;
                    if (str[j-1] > str[j]) {
                        j--;
                    }
                    else break;
                }
            }
            if (j==0) {
                str[j]--;
            }
            j++;
            for (; j<n ; j++) {
                str[j] = '9';
            }
        }

        printf("Case #%d: ", tt+1);
        for (int i=0 ; i<n ; i++) {
            if (i==0 && str[i]=='0') continue;
            printf("%c", str[i]);
        }
        printf("\n");
    }
}
