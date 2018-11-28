#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <queue>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

typedef pair<long long, long long> LLP;

int main() {
    int T;
    long long K, N;
    cin >> T;
    auto comp = [] (LLP &a, LLP &b) -> bool {
        return a.second - a.first < b.second - b.first ||
            ((a.second - a.first == b.second - b.first) && a.first > b.first);
    };
    for (int i = 1; i <= T; ++i) {
        cin >> N >> K;
        priority_queue<LLP, vector<LLP>, decltype(comp)> intervals(comp);
        intervals.push(make_pair(0, N - 1));
        for (int j = 1; j < K; j++) {
            auto interval = intervals.top();
            intervals.pop();
            long long mid = (interval.second + interval.first) / 2;
            //cout << "start, mid, end: " << interval.first << ", " << mid << ", " << interval.second << endl;
            if (mid > interval.first) {
                //cout << "pushing " << interval.first << ", " << mid - 1 << endl;
                intervals.push(make_pair(interval.first, mid - 1));
            }
            if (interval.second > mid) {
                //cout << "pushing " << mid + 1 << ", " << interval.second << endl;
                intervals.push(make_pair((mid + 1), interval.second));
            }
        }
        auto interval = intervals.top();
        //cout << "top: " << interval.first << ", " << interval.second << endl;
        long long mid = (interval.second + interval.first) / 2;
        long long LS = mid - interval.first, RS = interval.second - mid;
        cout << "Case #" << i << ": " << max(LS, RS) << " " << min(LS, RS) << endl;
    }
    return 0;
}