#include <string>
#include <iostream>
#include <cassert>
#include <tuple>
#include <vector>
#include <map>
#include <random>
using namespace std;
using i64 = int64_t;

tuple<i64, i64, i64> findPlace(const vector<bool>& busy) {
    vector<i64> left(busy.size());
    i64 leftClosest = -1;
    for (i64 i = 0; i < (i64)busy.size(); ++i) {
        if (busy[i]) {
            leftClosest = i;    
        } else {
            left[i] = i - leftClosest - 1;
        }
    }

    tuple<i64, i64, i64> bestScore(-1, -1, -1);
    i64 rightClosest = busy.size();
    for (i64 i = (i64)busy.size() - 1; i >= 0; --i) {
        if (busy[i]) {
            rightClosest = i;
        } else {
            i64 right = rightClosest - i - 1;

            auto score = make_tuple(min(right, left[i]), max(right, left[i]), -i);
            if (score > bestScore) {
                bestScore = score;
            }
        }
    }

    return bestScore;
}

tuple<i64, i64> solveBrute(i64 N, i64 K) {
    vector<bool> busy(N, false);
    tuple<i64, i64, i64> score;
    for (i64 i = 0; i < K; ++i) {
        score = findPlace(busy);
        i64 place = -get<2>(score);
        busy[place] = true;
    }
    return make_tuple(get<1>(score), get<0>(score));
}

tuple<i64, i64> solve(i64 N, i64 K) {
    map<i64, i64> lines;
    i64 left = -1, right = -1;
    lines[N] = 1;
    while (K > 0) {
        auto largeLines = *lines.rbegin(); 
        lines.erase(largeLines.first);

        i64 toSplit = min(K, largeLines.second);
        K -= toSplit;

        left = (largeLines.first - 1) / 2;
        right = largeLines.first - 1 - left;
        if (left > 0) {
            lines[left] += toSplit;
        }
        if (right > 0) {
            lines[right] += toSplit;
        }
    }
    return make_tuple(max(left, right), min(left, right)); 
}

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    ios::sync_with_stdio(0);

    /*
    std::mt19937 gen(0);
    const i64 MAXN = 10000;
    for (int i = 0; i < 1000; ++i) {
        i64 N = uniform_int_distribution<i64>(1, MAXN)(gen);
        i64 K = uniform_int_distribution<i64>(N, N)(gen);
        auto solution1 = solveBrute(N, K);
        auto solution2 = solve(N, K);
        assert(solution1 == solution2);
        cerr << i << ": " << N << " " << K << ": " << get<0>(solution2) << '\n';
    }
    cerr << "tested\n";
    */

    int T;
    cin >> T;
    for (int __ = 1; __ <= T; ++__) {
        i64 N, K;
        cin >> N >> K;
        auto solution2 = solve(N, K);
        cout << "Case #" << __ << ": " << get<0>(solution2) << " " << get<1>(solution2) << "\n";
    }

    return 0;
}
