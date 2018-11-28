#include <iostream>
#include <map>

using namespace std;

int main() {
    int T;
    unsigned long long stalls, user;
    cin >> T;

    for (int n = 1; n <= T; ++n) {
        cin >> stalls >> user;
        map<unsigned long long, unsigned long long> stallGaps;
        stallGaps.clear();
        stallGaps[stalls] = 1;
        while (true) {
            auto maxIter = stallGaps.rbegin();
            auto gap = maxIter->first - 1;
            auto count = maxIter->second;
            auto odd = gap % 2;
            if (user <= count) {
                cout << "Case #" << n << ": " << gap/2 + odd << " " << gap/2 << endl;
                break;
            }
            if (stallGaps.find(gap/2 + odd) == stallGaps.end()) {
                stallGaps[gap/2 + odd] = 0;
            }
            if (stallGaps.find(gap/2) == stallGaps.end()) {
                stallGaps[gap/2] = 0;
            }
            stallGaps[gap/2 + odd] += count;
            stallGaps[gap/2] += count;
            stallGaps.erase(gap + 1);
            user -= count;
        }
    }
}
