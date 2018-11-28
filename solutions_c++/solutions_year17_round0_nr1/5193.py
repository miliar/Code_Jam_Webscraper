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

const int MAXN = 1000;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;
int tk;
int k;
char tmp[MAXN];
string s;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
   
    scanf("%d\n", &tk); 
    
    forn(ii, tk) {
        scanf("%s", &tmp);
        s = tmp;
        scanf("%d\n", &k);
        int ans = 0;
        forn(i, int(s.size()) - k + 1) {
            if (s[i] == '+') continue;
            ++ans;
            fore(j, i, i + k) {
                if (s[j] == '+') {
                    s[j] = '-';
                }
                else {
                    s[j] = '+';
                }
            }
        }
        bool fail = 0;
        forn(i, s.size()) {
            if (s[i] == '-') fail = 1;
        }
        printf("Case #%d: ", ii + 1);
        if (fail) {
            printf("IMPOSSIBLE\n");
        }
        else {
            printf("%d\n", ans);
        }
    }

    return 0;
};

