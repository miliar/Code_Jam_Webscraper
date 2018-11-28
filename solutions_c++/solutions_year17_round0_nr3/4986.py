#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct comparisonObj {
    bool operator()(const pair<long long, long long> &a, const pair<long long, long long> &b) const {
        if (a.first > b.first)
            return false;
        else if (a.first < b.first)
            return true;
        else {
            if (a.second < b.second)
                return false;
            else return true;
        }
    }
};

/* pair<long long, long long>
     first: number of contiguous empty stalls
     second: index of leftmost stall (start index)
     stall_to_occupy = (first - 1) / 2 + second;
     num_to_right will always be >= num_to_left
     num_to_left = (first - 1) / 2;
     num_to_right = first - (num_to_left + 1);
*/

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        long long N, K, num_to_left, num_to_right, left_start, right_start;
        cin >> N >> K;
        priority_queue<pair<long long, long long>, vector<pair<long long, long long>>, comparisonObj> stalls;
        stalls.emplace(N, 0);
        const pair<long long, long long> *next;
        for (long long j = 0; j < K; ++j) {
            next = &stalls.top();
            num_to_left = (next->first - 1) / 2;
            num_to_right = next->first - (num_to_left + 1);
            if (j == K - 1) {
                cout << "Case #" << i + 1 << ": " << num_to_right << " " << num_to_left << endl;
                break;
            }
            left_start = next->second;
            right_start = next->second + num_to_left + 1;
            stalls.pop();
            stalls.emplace(num_to_left, left_start);
            stalls.emplace(num_to_right, right_start);
        }
    }
}
