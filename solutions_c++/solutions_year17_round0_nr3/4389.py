#include <bits/stdc++.h>

using namespace std;

int main () {
    int tt; 
    cin >> tt;
    for (int cases = 1; cases <= tt; ++cases) {
        cout << "Case #" << cases << ": ";
        int n, k;
        cin >> n >> k;
        int twos = 1;
        int cur = n;
        vector<int> offsets(30, 0);
        offsets[0] = 1;
        while (k > twos) {
            int newCur = (cur-1)/2;
            vector<int> newOffsets(30, 0);
            for (int i = 0; i < 30; ++i) {
                int l = (cur + i - 1)/2;
                int r = (cur + i)/2;
                newOffsets[l - newCur] += offsets[i];
                newOffsets[r - newCur] += offsets[i];
            }
            offsets = newOffsets;
            cur = newCur;
            k -= twos;
            twos *= 2;
        }

        int i;
        for (i = 29; i >= 0; --i) {
            if (offsets[i] == 0)
                continue;
            if (k <= offsets[i])
                break;
            k -= offsets[i];
        }
        int l = (cur + i - 1)/2;
        int r = (cur + i)/2;
        cout << r << " " << l << "\n";
    }
}
