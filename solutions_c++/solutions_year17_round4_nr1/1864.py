#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>
#include <ctime>
#include <cassert>
#include <cstring>
#include <fstream>

#define FOR(i, a, b) for(int (i)=(a); (i)<(b); (i)++)
#define IFOR(i, a, b) for(int (i)=(a);(i)<=(b);(i)++)
#define RFOR(i, a, b) for(int (i)=(a);(i)>=(b);(i)--)

using namespace std;

int main() {
    int totalcases;
    cin >> totalcases;
    IFOR(casenum, 1, totalcases) {
        printf("Case #%d: ", casenum);
        // solution
        int n, p;
        cin >> n >> p;
        vector<int> g(n);
        FOR(i, 0, n) {
            cin >> g[i];
        }
        if (p == 2) {
            int m0 = 0, m1 = 0;
            FOR(i, 0, n) {
                if (g[i] % 2 == 0)
                    m0++;
                else
                    m1++;
            }
            cout << m0 + (m1+1) / 2 << endl;
        }
        else if (p == 3) {
            int m0 = 0, m1 = 0, m2 = 0;
            FOR(i, 0, n) {
                if (g[i] % 3 == 0)
                    m0++;
                else if (g[i] % 3 == 1)
                    m1++;
                else
                    m2++;
            }
            int maxx = 0;
            IFOR(i, 0, m1) {
                IFOR(j, 0, m2) {
                    int cnt = m0;
                    int tm1 = m1 - i - j;
                    int tm2 = m2 - i - j;
                    if (tm1 < 0 || tm2 < 0)
                        continue;
                    cnt += i + j;
                    cnt += tm1 / 3;
                    cnt += tm2 / 3;
                    if (tm1 % 3 > 0 || tm2 % 3 > 0)
                        cnt += 1;

                    maxx = max(maxx, cnt);
                }
            }
            cout << maxx << endl;
        }

    }
    return 0;
}