#include<iostream>
#include<queue>
#include<map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    long n, k, t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        priority_queue<long> Q;
        map<long, long> m;
        long counter = 0;
        cin >> n >> k;

        m[n] = 1;
        Q.push(n);
        while (!Q.empty()) {
            long c = Q.top();
            Q.pop();
            counter += m[c];
            if (counter >= k) {
                long a, b;
                if (c % 2 == 0) {
                    a = c / 2;
                    b = c / 2 - 1;
                } else {
                    a = b = c / 2;
                }
                cout << "Case #" << i + 1 << ": " << a << " " << b << endl;
                break;
            }

            if (c % 2 == 0) {
                if (m[c / 2] == 0) Q.push(c / 2);
                if (m[c / 2 - 1] == 0) Q.push(c / 2 - 1);
                m[c / 2] += m[c];
                m[c / 2 - 1] += m[c];
            } else {
                if (m[c / 2] == 0) Q.push(c / 2);
                m[c / 2] += m[c] * 2;
            }
        }
    }
}