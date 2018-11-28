#include <iostream>
#include <queue>
#include <functional>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int T=1; T<=cases; ++T) {
        int N, K;
        cin >> N >> K;

        priority_queue < int > q;
        q.push(N);
        int smallN = N;
        for (int i=0; i<K; ++i) {
            smallN = q.top();
            q.pop();

            int half = (smallN - 1) / 2;
            q.push(half);
            q.push(smallN - half - 1);
        }
        cout << "Case #" << T << ": " << smallN - 1 - ((smallN - 1) / 2) << " " << (smallN - 1) / 2 << endl;
    }
    return 0;
}
