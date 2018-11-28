#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

int main() {
    int tests;
    scanf("%d", &tests);
    fore(test, 1, tests) {
        cerr << "test " << test << endl;
        int n;
        scanf("%d", &n);
        while(true) {
            int cur = n;
            vi digits;
            while(cur) {
                digits.pb(cur % 10);
                cur /= 10;
            }
            bool fail = false;
            for(int j = (int)digits.size() - 2; j >= 0; j--)
                if (digits[j + 1] > digits[j]) {
                    fail = true;
                    break;
                }
            if (!fail) {
                printf("Case #%d: %d\n", test, n);
                break;
            }
            n--;
        }
    }
}
