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
        long long n, k;
        cin >> n >> k;

        long long tt = 1;
        int keta = 1;
        while ((tt << 1) + 1 <= k) {
            tt = (tt << 1) + 1;
            keta++;
        }

        long long resl = 0, resr = 0;
        long long big = n, small = n;
        long long bigcnt = 1;
        long long nums = 1;

        FOR(i, 0, keta) {
            if (big == small) {
                if (big % 2 == 0) {
                    resl = big / 2 - 1, resr = big / 2;
                    small = resl, big = resr;
                    bigcnt = nums;
                    nums *= 2;
                }
                else {
                    resl = big / 2, resr = big / 2;
                    small = big = resl;
                    nums *= 2;
                }
            }
            else {
                long long smallcnt = nums - bigcnt;
                if (big % 2 == 0) {
                    resl = big / 2 - 1, resr = big / 2 - 1;
                    small = big / 2 - 1, big = big / 2;
                }
                else {
                    resl = big / 2 - 1, resr = big / 2;
                    small = big / 2 - 1, big = big / 2;
                    bigcnt = nums * 2 - smallcnt;
                }
                nums *= 2;
            }
        }
        k -= tt;
        if (k > 0) {
            if (big == small) {
                if (big % 2 == 0) {
                    if (k * 2 <= nums) {
                        resl = big / 2 - 1, resr = big / 2;
                    }
                    else {
                        resl = big / 2 - 1, resr = big / 2 - 1;
                    }
                }
                else {
                    resl = big / 2, resr = big / 2;
                }
            }
            else {
                if (big % 2 == 0) {
                    if (k <= bigcnt) {
                        resl = big / 2 - 1, resr = big / 2;
                    }
                    else {
                        resl = big / 2 - 1, resr = big / 2 - 1;
                    }
                }
                else {
                    if (k <= bigcnt) {
                        resl = big / 2, resr = big / 2;
                    }
                    else {
                        resl = big / 2 - 1, resr = big / 2;
                    }
                }
            }
        }

        printf("%lld %lld\n", resr, resl);
    }
    return 0;
}