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

int tc;

#define MAXN 110

int f[MAXN+2][MAXN+2][4];
int c[MAXN+2][MAXN+2][MAXN+2][4];
int a[MAXN];
int n, p, ans, s;

void init3() {
    for(int i=0; i<MAXN; ++i)
        for(int j=0; j<MAXN; ++j)
            for(int z=0; z<3; ++z) {
                if (z == 0) {
                    f[i+1][j][1] = max(f[i][j][0] + 1, f[i+1][j][1]);
                    f[i][j+1][2] = max(f[i][j][0] + 1, f[i][j+1][2]);
                }
                int t;
                t = (z + 1) % 3;
                f[i+1][j][t] = max(f[i+1][j][t], f[i][j][z]);

                t = (z + 2) % 3;
                f[i][j+1][t] = max(f[i][j+1][t], f[i][j][z]);

            }
        
}

void init4() {
    for(int i=0; i<MAXN; ++i)
        for(int j=0; j<MAXN; ++j)
            for(int k=0; k<MAXN; ++k)
                for(int z=0; z<4; ++z) {
                    if (z == 0) {
                        c[i+1][j][k][1] = max(c[i][j][k][0] + 1, c[i+1][j][k][1]);
                        c[i][j+1][k][2] = max(c[i][j][k][0] + 1, c[i][j+1][k][2]);
                        c[i][j][k+1][3] = max(c[i][j][k][0] + 1, c[i][j][k+1][3]);
                    }

                int t;
                t = (z + 1) % 3;
                c[i+1][j][k][t] = max(c[i+1][j][k][t], c[i][j][k][z]);

                t = (z + 2) % 3;
                c[i][j+1][k][t] = max(c[i][j+1][k][t], c[i][j][k][z]);

                t = (z + 3) % 3;
                c[i][j][k+1][t] = max(c[i][j][k+1][t], c[i][j][k][z]);


            }
        
}


int main() {
    init3();
    init4();
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt = 1; tt <= tc; ++tt) {
        scanf("%i%i", &n, &p);
        memset(a, 0, sizeof(a));
        ans = 0;
        s = 0;
        for(int i=0; i<n; ++i) {
            int x;
            scanf("%i", &x);
            if (x % p == 0) {
                ans++;
            } else {
                a[x % p]++;
                s += x;
            }
        }
        s = s % p;

        if (p == 2) {
            ans += (a[1] + 1) / 2;
        } else if (p == 3) {
            ans += f[ a[1] ][ a[2] ][ s ];
        } else {
            ans += c[ a[1] ][ a[2] ][ a[3] ][ s ];
        }

        printf("Case #%i: %i\n", tt, ans);
    }
    return 0;
}