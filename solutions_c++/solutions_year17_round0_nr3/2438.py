/*************************************************************************
	> File Name: QualificationRound_C.cpp
	> Author: BMan
	> Mail: luo-kai-jia@163.com
	> Created Time: Sat 08 Apr 2017 01:21:46 PM CST
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;


typedef unsigned long long ULL;

int main() {
    int _T = 0;
    cin >> _T;
    for (int _t = 1; _t <= _T; _t++) {
        unsigned long long n, k;
        cin >> n >> k;
        
        ULL l = 0, r = 0;
        map<ULL, ULL> m;
        m[n] = 1;

        while(m.rbegin() != m.rend()) {
            auto iter = m.rbegin();
            l = (iter->first - 1) / 2;
            r = (iter->first - 1) - l;
            if (iter->second >= k) {
                break;
            } else {
                m[l] += iter->second;
                m[r] += iter->second;
                k -= iter->second;
                m.erase(iter->first);
            }
        }
        
        cout << "Case #" << _t << ": " << r << ' ' << l << endl;
    }
    return 0;
}
