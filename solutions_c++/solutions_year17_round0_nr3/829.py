#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("sample.in", "r", stdin);
//    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for (int ti = 1; ti <= tc; ++ti) {
        cout << "Case #" << ti << ": ";
        long long n, k;
        cin >> n >> k;
        map<long long, long long, greater<long long>> intervals; 
        intervals[n] = 1;
        do {
            auto f = intervals.begin();
            long long x = (f->first-1)>>1;
            if (f->second >= k) {
                cout << f->first-1-x << " " << x << "\n";
                break;
            }
            else {
                long long y = f->first-1-x;
                long long cnt = f->second;
                k -= cnt;
                intervals.erase(f);
                if (y) 
                    intervals[y] += cnt;
                if (x)
                    intervals[x] += cnt;
            }
        }
        while (true);
    }
    return 0;
}
