#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define PI 3.1415926535897932384626433832795

#define fill(x, v)  fillchar(x, v, sizeof(x))
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector< pii >   vpii;

#define MAXN 100

int tc;

char s[MAXN][MAXN];
int  x, y;
int start_x;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt = 1; tt <= tc; ++tt) {
        scanf("%i%i", &y, &x);
        for(int i=1; i<=y; ++i) {
            scanf("%s", &s[i][1]);
        }


        for(int j=1; j<=x; ++j) {
            for(int i=1; i<=y; ++i) if (s[i][j] != '?') {
                start_x = j;
                j = x;
                break;
            }
        }

        //printf("start_x=%i\n", start_x);

        for(int j=start_x; j<=x; ++j) {
            int t = 0;
            for(int i=1; i<=y; ++i) if (s[i][j] != '?') t = i;
            //printf("j=%i t=%i\n", j, t);

            if (!t) {
                for(int i=1; i<=y; ++i) s[i][j] = s[i][j - 1];
            } else {
                for(int i=t - 1; i>=1; --i) 
                    if (s[i][j] == '?') s[i][j] = s[i + 1][j];
                for(int i=t + 1; i<=y; ++i) s[i][j] = s[i - 1][j];
            }
        }

        for(int j=start_x - 1; j>=1; --j) {
            for(int i=1; i<=y; ++i) s[i][j] = s[i][j + 1];
        }

        printf("Case #%i:\n", tt);

        for(int i=1; i<=y; ++i) printf("%s\n", &s[i][1]);
    }
    return 0;
}