#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
using namespace std;

vector<bool> traversal(long long int K) {
    vector<bool> binary;
    while (K > 0) {
        binary.push_back((K % 2L) == 0L);
        K = K / 2L;
    }
    binary.pop_back(); // TODO
    // vector<bool> res;
    // long long int l = 0;
    // long long int h = bound;
    // long long int mid;
    // while (depth > 0) {
    //     mid = (l + h ) / 2LL;
    //     res.push_back( K <= mid);
    //     if (res.back()) {
    //         l = mid;
    //     } else {
    //         h = mid;
    //     }
    //     --depth;
    // }
    reverse(binary.begin(), binary.end());
    return binary;
//    return res;
}

long long int ceil_div(long long int x, long long int d) {
    if (x % d == 0) {
        return x / d;
    }
    return (x/d) + 1;
}

pair<long long int, long long int> evaluate(const vector<bool> &path, long long int N) {
    long long int mid;
    long long int L;
    long long int R;
    for (int i = 0; i < path.size(); ++i) {
        mid = ceil_div(N, 2L);
        L = mid - 1L;
        R = N - mid;
        if (path[i]) {
            N = R;
        } else {
            N = L;
        }
    }
    mid = ceil_div(N, 2L);
    L = mid - 1L;
    R = N - mid;
    return make_pair(
            L > R ? R : L,
            L > R ? L : R
            );
    
}

int main() {
    int T;
    long long int K;
    long long int N;

    cin >> T;
    for (int t = 0; t < T; ++t ) {
        cin >> N >> K;
        map<long long int, long long int> size_to_number;
        long long int highest = N;
        size_to_number[N] = 1;
        long long int mid;
        long long int L;
        long long int R;
        long long int old_number;
        while (true) {
            mid = ceil_div(highest, 2L);
            L = mid - 1L;
            R = highest - mid;
            old_number = size_to_number.rbegin()->second;
            if (old_number >= K) break;
            K -= old_number;
            size_to_number.erase(highest);
            if (L != 0) {
                if (size_to_number.find(L) == size_to_number.end()) {
                    size_to_number[L] = 0;
                }
                size_to_number[L] += old_number;
            }
            if (R != 0) {
                if (size_to_number.find(R) == size_to_number.end()) {
                    size_to_number[R] = 0;
                }
                size_to_number[R] += old_number;
            }
            highest = size_to_number.rbegin()->first;
        }

        pair<long long int, long long int> res = 
            make_pair(
                L > R ? R : L,
                L > R ? L : R
                );
        cout << "Case #" << t+1 << ": " << res.second << " " << res.first << endl;

    }
    return 0;
}
