#include <bits/stdc++.h>

using namespace std;

long long t, n, k;

// void down(int low, int high, int k) {
//     int nextStall = (high + low - 1) / 2;
//     k--;
//     if (k == 0) {
//         cout << (high - nextStall - 1) << " " << (nextStall - low) << endl;
//     } else {
//         if (k % 2 )
//     }
// }

int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> n >> k;

        unordered_map<long long, long long> splitNums;

        priority_queue<long long> toSplits;
        toSplits.push(n);
        splitNums[n] = 1;

        cout << "Case #" << test << ": ";
        while (true) {
            long long toSplit = toSplits.top();
            toSplits.pop();
            long long splitNum = splitNums[toSplit];


            long long nextStall = (toSplit - 1) / 2;
            long long large = (toSplit - nextStall - 1), small = nextStall;

            // cout << toSplit << " " << large << " " << small << " " << k << " " << splitNum << endl;
            if (k <= splitNum) {
                cout << large << " " << small << endl;
                break;
            }
            k -= splitNum;

            if (splitNums.count(large) == 0) {
                splitNums[large] = 0;
                toSplits.push(large);
            }

            if (splitNums.count(small) == 0) {
                splitNums[small] = 0;
                toSplits.push(small);
            }

            splitNums[large] += splitNum;
            splitNums[small] += splitNum;
        }

    }
}