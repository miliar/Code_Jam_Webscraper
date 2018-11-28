#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int T;
unsigned long long n, ans, s[20], e[20];

int main(){
    cin >> T;
    e[0] = s[0] = 1;
    for (int i = 1; i <= 18; ++i) e[i] = e[i - 1] * 10;
    for (int i = 1; i <= 18; ++i) s[i] = e[i] + s[i - 1];
    for (int id = 1; id <= T; id++) {
        cin >> n;
        int last = 0, test;
        ans = 0;
        for (int i = 18; i >= 0; i--) {
            for (int k = last; k < 10; k++) {
                if (ans + k * s[i] <= n) {
                    test = k;
                } else {
                    break;
                }
            }
            last = test;
            ans += test * e[i];
        }
        cout << "Case #" << id << ": " << ans << endl;
    }
}
