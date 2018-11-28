#include <iostream>
#include <queue>

using namespace std;

int main(void)
{
    int T, N, K;
    cin >> T;

    for (int i = 0; i < T; i++) {
        cin >> N >> K;

        priority_queue<int> q;
        q.push(N);

        for (int j = 0; j < K; j++) {
            int t = q.top();
            q.pop();

            q.push(t / 2);
            q.push((t - 1) / 2);

            if (j + 1 == K)
                cout << "Case #" << i + 1 << ": " << t / 2 << " " << (t - 1) / 2 << endl;
        }
    }

    return 0;
}
