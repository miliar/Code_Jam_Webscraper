#pragma comment(linker, "/STACK:36777216")
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>
#include <map>
#include <set>
#include <memory.h>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); ++i) 
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i) 
#define forv(i, v) for(int i = 0; i < int(v.size()); ++i)

#define ll long long 
#define ld long double 
#define PLL pair <ld, ld> 
#define PII pair <int, int> 
#define pb push_back 
#define sz size

const int MAXN = 10010;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;
const ld INF = 1e9;

int d, n;
int k[MAXN], s[MAXN];

PII h[MAXN];
int c = 0;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
   
    int tk;
    cin >> tk;

    forn(ii, tk) {
        cin >> d >> n;
        forn(i, n) {
            scanf("%d %d", &k[i], &s[i]);
        }
       
        ld ans = 0;
        forn(i, n) {
            bool ok = 1;
            fore(j, 1, n) {
                if (k[j] >= k[i] && s[j] < s[i]) {
                    ld t = (.0 + k[j] - k[i]) / (s[i] - s[j]);
                    ld dis = k[i] + t * s[i];
                    if (dis < d - EPS) {
                        ok = 0;
                        break;
                    } 
                    
                }
            }
            if (ok) {
                ans = max(ans, (ld)(.0 + d - k[i]) / s[i]);
            }
        }
        ans = d / ans; 
        printf("Case #%d: %.6f\n", ii + 1, (double)ans);
    }


    return 0;
};

