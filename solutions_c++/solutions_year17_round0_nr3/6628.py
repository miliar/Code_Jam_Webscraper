
#include <bits/stdc++.h>
using namespace std;
#define int long long

bool oc[1007];
int32_t main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        set<int> occ;
        int n, k;
        cin >> n >> k;
        occ.insert(0);
        occ.insert(n+1);
        int currbest, currl, currr;
        for (int i =0; i<k; i++) {
            currbest = currl = currr = -1;
            for (int j = 1; j <=n; j++) {
                if (occ.count(j))
                    continue;
                int l = j - *(--(occ.upper_bound(j)));
                int r = *occ.upper_bound(j) - j;
                if (min(l,r) > min(currl, currr)
                        || (min(l, r) == min(currl, currr) &&
                            max(l, r) > max(currl, currr))) {
                    currbest = j;
                    currl=l;
                    currr=r;
                }
            }
            occ.insert(currbest);
            //cerr << currbest << " " << currl << " " << currr << endl;
        }
        cout << "Case #" << tt << ": " << max(currl, currr)-1 << " "<< min(currl, currr)-1 << endl;
    }
}
