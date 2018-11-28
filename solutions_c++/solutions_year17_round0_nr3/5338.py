#include<iostream>
#include<queue>

using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        int N, K;
        cin >> N >> K;
        priority_queue<int> q;
        q.push(N);
        if (N == K) {
            cout << "Case #" << i+1 << ": " << "0 0" << endl;
            continue;
        }
        int min_d, max_d;
        for (int i=0; i<K; i++) {
            int n = q.top()-1;
            q.pop();
            if (n == 0) {
                min_d = max_d = 0;
                continue;
            }
            if (n%2 == 0) {
                q.push(n/2);
                q.push(n/2);
                min_d = max_d = n/2;
            } else {
                if (n/2) q.push(n/2);
                q.push(n/2+1);
                min_d = n/2;
                max_d = n/2+1;
            }
        }
        cout << "Case #" << i+1 << ": " << max_d << ' ' << min_d << endl;
    }
    return 0;
}
