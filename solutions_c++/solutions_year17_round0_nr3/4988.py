#include <iostream>
#include <utility>
#include <queue>

using namespace std;

string bathStall(unsigned long long N, unsigned long long K) {
    auto y = N, z = N;
    priority_queue<int> pq;
    pq.push(N);

    for (int i = 1; i <= K; i++) {
        auto len = pq.top();
        pq.pop();
        y = len / 2;
        z = len % 2 == 0 ? len / 2 - 1 : len / 2;
        pq.push(y);
        pq.push(z);
    }
    return to_string(y) + " " + to_string(z);
}

int main() {
    int T, id = 1;
    unsigned long long N, K;
    cin >> T;
    while (T--) {
        cout << "Case #" << id << ": ";
        cin >> N >> K;
        id++;
        cout << bathStall(N, K) << endl;
    }

    return 0;
}