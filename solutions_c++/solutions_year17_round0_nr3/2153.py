#include <iostream>
#include <map>
using namespace std;


#define INP "C-large.in"
#define OUT "output.txt"

int main(int argc, char const *argv[]) {
    freopen(INP, "r", stdin);
    freopen(OUT, "w", stdout);

    int T;
    cin >> T;
    for (int tid = 0; tid < T; ++tid) {
        // Read inputs
        long long N, K;
        cin >> N >> K;

        // Solve
        map<long long, long long> counter;
        ++counter[N];
        while (counter.rbegin()->second < K) {
            long long length = counter.rbegin()->first;
            long long amount = counter.rbegin()->second;
            counter.erase(length);
            K -= amount;
            long long right = (length - 1) / 2;
            long long left = length - 1 - right;
            counter[left] += amount;
            counter[right] += amount;
        }

        // Output
        long long length = counter.rbegin()->first;
        long long right = (length - 1) / 2;
        long long left = length - 1 - right;
        cout << "Case #" << tid + 1 << ": " << left << " " << right << endl;
    }

    return 0;
}