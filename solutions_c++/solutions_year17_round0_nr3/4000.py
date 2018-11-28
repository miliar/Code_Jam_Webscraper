#include <iostream>
#include <map>

using namespace std;

int main(int argc, char* argv[]) {
    int T;
    long long N, K;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N >> K;
        //if (K > N / 2) { cout << "Case #" << i << ": " << 0 << " " << 0 << endl; continue; }

        long long max_R = 0, min_R = 0;
        map<long long, int> stalls; stalls[N] = 1;
        for (int j = 0; j < K; ++j) {
            long long size = (stalls.rbegin())->first;
            int count = -- (stalls.rbegin())->second;
            if (count == 0) stalls.erase(size);
            max_R = min_R = size / 2; if (size % 2 == 0) --min_R;
            if (max_R > 0) ++stalls[max_R];
            if (min_R > 0) ++stalls[min_R];
        }

        cout << "Case #" << i << ": " << max_R << " " << min_R << endl;
    }
}