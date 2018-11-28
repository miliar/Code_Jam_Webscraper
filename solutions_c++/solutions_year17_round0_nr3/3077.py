#include <iostream>
#include <string>
#include <map>
#include <cstdint>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";

        uint64_t N, K;
        cin >> N >> K;

        map<uint64_t, uint64_t> numStalls;
        numStalls[N] = 1;
        for (uint64_t i = 1; i < K; i *= 2) {
            K -= i;
            map<uint64_t, uint64_t> tmp;
            for (const auto& stallE : numStalls) {
                uint64_t stallDist = stallE.first-1;
                tmp[stallDist / 2] += stallE.second;
                tmp[stallDist / 2 + (stallDist & 1)] += stallE.second;
            }
            numStalls = tmp;
        }
        for (auto iter = numStalls.rbegin(); iter != numStalls.rend(); iter++) {
            uint64_t num = iter->second;
            if (num < K) {
                K -= num;
            } else {
                uint64_t stallDist = iter->first-1;
                uint64_t left = stallDist / 2 + (stallDist & 1);
                uint64_t right = stallDist / 2;
                cout << left << " " << right << "\n";
                break;
            }
        }
    }
}
