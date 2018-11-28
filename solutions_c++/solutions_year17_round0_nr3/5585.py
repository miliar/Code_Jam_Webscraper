#include <iostream>
#include <queue>

using namespace std;

int main() {
    size_t T, N, K;
    cin >> T;
    for(size_t t = 1; t <= T; t++) {
        cin >> N >> K;

        priority_queue<size_t> pq;
        pq.push(N);

        size_t max_space = 0;
        size_t min_space = 0;
        for(size_t k = 0; k < K; k++) {
            size_t space = pq.top();
            pq.pop();

            if(space % 2 == 0) {
                min_space = space / 2 - 1;
                max_space = space / 2;
            } else {
                min_space = space / 2;
                max_space = space / 2;
            }
            pq.push(max_space);
            pq.push(min_space);
        }
        cout << "Case #" << t << ": " << max_space << ' ' << min_space << '\n';
    }
    return EXIT_SUCCESS;
}
