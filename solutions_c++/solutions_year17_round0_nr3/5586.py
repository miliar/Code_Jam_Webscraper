#include <iostream>
#include <string>
#include <queue>

using namespace std;

string solve(uint64_t N, int K)
{
    priority_queue<uint64_t> bathroom;
    bathroom.push(N);
    for (int k = 1; k <= K; ++k) {
        auto space = bathroom.top();
        bathroom.pop();
        uint64_t left = space / 2;
        if (left > 0) bathroom.push(left);
        uint64_t right = space - left - 1;
        if (right > 0) bathroom.push(right);
        if (k == K) {
            return to_string(left) + " " + to_string(right);
        }
    }
    return "?";
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        uint64_t N, K;
        cin >> N >> K;
        cout << "Case #" << t << ": ";
        //cout << N << " " << K << "->";
        cout << solve(N, K);
        cout << endl;
    }
}