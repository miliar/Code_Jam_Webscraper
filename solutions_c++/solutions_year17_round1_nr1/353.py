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

char str[102][102];
int have[102];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    int r, c;
    scanf("%d", &t);
    for (int tt=0 ; tt<t ; tt++) {
        scanf("%d %d", &r, &c);
        for (int i=0 ; i<r ; i++) {
            scanf(" %s", str[i]);
        }
        for (int i=0 ; i<r ; i++) {
            have[i] = 0;
            for (int j=0 ; j<c ; j++) {
                if (str[i][j] != '?') {
                    have[i] = 1;
                    break;
                }
            }
        }
        int first=0;
        while (have[first] == 0) {
            first++;
        }
        for (int i=first ; i<r ; i++) {
            if (have[i] == 0) {
                for (int j=0 ; j<c ; j++) {
                    str[i][j] = str[i-1][j];
                }
                continue;
            }
            char tmp;
            int index_temp;
            for (int j=0 ; j<c ; j++) {
                if (str[i][j] != '?') {
                    tmp = str[i][j];
                    index_temp = j;
                    break;
                }
            }
            int j=0;
            for (; j<=index_temp ; j++) {
                str[i][j] = tmp;
            }
            for (; j<c ; j++) {
                if (str[i][j] == '?') str[i][j] = tmp;
                else tmp = str[i][j];
            }
        }
        for (int i=0 ; i<first ; i++) {
            for (int j=0 ; j<c ; j++) {
                str[i][j] = str[first][j];
            }
        }

        printf("Case #%d:\n", tt+1);
        for (int i=0 ; i<r ; i++) {
            printf("%s\n", str[i]);
        }
    }
}
