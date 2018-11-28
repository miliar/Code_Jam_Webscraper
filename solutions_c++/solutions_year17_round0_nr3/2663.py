#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;


int main() {
    int tcase;
    cin >> tcase;
    for (int t = 0; t < tcase; t++) {
        long long n, k;
        cin >> n >> k;
        long long ass = 0;
        long long e = 1;
        long long ce = 1;
        pair<long long, long long> dodd = make_pair(n, 0);
        pair<long long, long long> deven = make_pair(n, 0);
        if (n%2 != 0) {
            dodd.second = 1;
        } else {
            deven.second = 1;
        }
        // cout << "dodd : " << dodd.first << " " << dodd.second << endl;
        // cout << "deven: " << deven.first << " " << deven.second << endl;
        // cout << maxL << " " << minL << endl;
        while (ass < k) { 
            long long doddValue = dodd.first;
            long long doddCount = dodd.second;
            long long devenValue = deven.first;
            long long devenCount = deven.second;
            long long doddNewValue = n;
            long long doddNewCount = 0;
            long long devenNewValue = n;
            long long devenNewCount = 0;
            if (doddCount > 0 && ((doddValue-1)/2)%2!=0){
                doddNewValue = ((doddValue-1)/2);
                doddNewCount += (doddCount*2);
            } else {
                devenNewValue = ((doddValue-1)/2);
                devenNewCount += (doddCount*2);
            }

            if (devenCount > 0 && ((devenValue-1)/2)%2!=0) {
                devenNewValue = (devenValue-1)/2+1;
                devenNewCount += devenCount;
                doddNewValue = (devenValue-1)/2;
                doddNewCount += devenCount;
            } else {
                devenNewValue = (devenValue-1)/2;
                devenNewCount += devenCount;
                doddNewValue = (devenValue-1)/2+1;
                doddNewCount += devenCount;
            }
            ass += e;
            // cout << ass << " " << maxL << " " << minL << endl;
            if (ass >= k) {
                break;
            }
            dodd = make_pair(doddNewValue, doddNewCount);
            deven = make_pair(devenNewValue, devenNewCount);
            // cout << "dodd : " << dodd.first << " " << dodd.second << endl;
            // cout << "deven: " << deven.first << " " << deven.second << endl;
            e *= 2;
            ce = ce + e;
        }
        long long doddValue = dodd.first;
        long long doddCount = dodd.second;
        long long devenValue = deven.first;
        long long devenCount = deven.second;
        ce = ce - e;
        long long x = k - ce;
        // cout << "========" << endl;
        // cout << "dodd : " << dodd.first << " " << dodd.second << endl;
        // cout << "deven: " << deven.first << " " << deven.second << endl;
        // cout << "x-e  : " << x << " " << e << endl;
        long long maxL = -1;
        long long minL = -1;
        if ((doddCount > 0 && doddValue > devenValue) || (devenCount == 0)) {
            if (x > doddCount) {
                maxL = (devenValue-1)/2 +1;
                minL = (devenValue-1)/2;
            } else {
                maxL = (doddValue-1)/2;
                minL = (doddValue-1)/2;
            }
        } else {
            if (x > devenCount) {
                maxL = (doddValue-1)/2;
                minL = (doddValue-1)/2;
            } else {
                maxL = (devenValue-1)/2 +1;
                minL = (devenValue-1)/2;
            }
        }
        cout << "Case #" << t+1 << ": " << maxL << " " << minL << endl;
    }
    return 0;
}