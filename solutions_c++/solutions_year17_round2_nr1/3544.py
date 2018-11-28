#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <deque>

using namespace std;



int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(6);
    cout << fixed;

    int T;

    cin >> T;

    for(int cs = 1;cs <= T;++cs) {
        int D, N;

        cin >> D;
        cin >> N;

        vector<pair<int,int>> h;
        for(int horses = 0;horses < N;++horses) {
            int K, S;
            cin >> K;
            cin >> S;
            h.push_back({K, S});
        }

        // 1. Find the slowest
        sort(h.begin(), h.end(), [](pair<int, int> a, pair<int, int> b) { return a.second > b.second; });

        double fh = -1;

        while(h.size() > 0) {
            int min_k = h.back().first;
            int min_s = h.back().second;

            // 2. Remove the slowest
            h.pop_back();

            // 3. Calculate time to end
            double time_end = ((double)(D - min_k)) / ((double) min_s);
            if (time_end > fh) {
                fh = time_end;
            }
        }



        double res = ((double) D) / fh;
        cout << "Case #" << cs << ": " << res << '\n';
    }

    return 0;
}

