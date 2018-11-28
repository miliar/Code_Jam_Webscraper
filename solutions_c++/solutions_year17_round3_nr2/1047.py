#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

int T;
int n0, n1;

struct intVal {
    int l, r, t;
    intVal() {}
    intVal(int _l, int _r, int _t): l(_l), r(_r), t(_t) {}
};

bool cmpInt(const intVal& a, const intVal& b) {
    return a.l <= b.l;
}

struct gapType {
    int cnt, type;
    gapType(int c, int t): cnt(c), type(t) {}
};

bool cmpGap(const gapType& a, const gapType& b) {
    return a.cnt <= b.cnt;
}

int main() {
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        vector <intVal> ints;
        ints.clear();
        
        cin >> n0 >> n1;
        int left[2];
        left[0] = left[1] = 720;
        
        for (int i = 0; i < n0; i++) {
            int l, r;
            cin >> l >> r;
            left[1] -= r - l;
            ints.push_back( intVal(l, r, 1) );
        }
        for (int i = 0; i < n1; i++) {
            int l, r;
            cin >> l >> r;
            left[0] -= r - l;
            ints.push_back( intVal(l, r, 0) );
        }
        sort(ints.begin(), ints.end(), cmpInt);
        
        vector< gapType > gaps;
        gaps.clear();
        
        int ans = 0;
        for (int i = 0; i < n0 + n1 - 1; i++) {
            if (ints[i].t != ints[i + 1].t) ans += 1;
            else {
                if (ints[i].r < ints[i + 1].l) {
                    gaps.push_back( gapType(ints[i + 1].l - ints[i].r, ints[i].t) );
                }
            }
        }
        
        if (ints[n0 + n1 - 1].t != ints[0].t) ans += 1;
        else {
            int cnt = 1440 - ints[n0 + n1 - 1].r + ints[0].l;
            if (cnt > 0) {
                gaps.push_back( gapType(cnt, ints[0].t) );
            }
        }
        
        sort(gaps.begin(), gaps.end(), cmpGap);
        for (int i = 0; i < gaps.size(); i++) {
            if (left[ gaps[i].type ] < gaps[i].cnt) ans += 2;
            else {
                left[ gaps[i].type ] -= gaps[i].cnt;
            }
        }
        
//        gaps.clear();
//        if (ints[0].l != 0) {
//            gaps.push_back ( gapType(ints[0].l, ints[0].t) );
//        }
//        if (ints[ ints.size() - 1 ].r != 1440) {
//            gaps.push_back ( gapType(1440 - ints[ ints.size() - 1 ].r, ints[ints.size() - 1].t) );
//        }
//        sort(gaps.begin(), gaps.end(), cmpGap);
//        for (int i = 0; i < gaps.size(); i++) {
//            if (left[ gaps[i].type ] < gaps[i].cnt) ans++;
//            else {
//                left[ gaps[i].type ] -= gaps[i].cnt;
//            }
//        }
        cout << "Case #" << cas << ": " << ans << "\n";
    }
    return 0;
}