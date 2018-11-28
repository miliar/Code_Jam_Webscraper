#include <iostream>
#include <queue>

using namespace std;

int main() {
        size_t testnum;
        cin >> testnum;
        for (size_t test {1}; test <= testnum; ++test) {
                int n, k;
                cin >> n >> k;
                priority_queue<int> q;
                q.push(n);
                int a, b;
                for(int i {0}; i < k; ++i) {
                        int m {q.top()};
                        q.pop();
                        m -= 1;
                        a = m / 2;
                        b = m - m / 2;
                        if (a > 0)
                                q.push(a);
                        if (b > 0)
                                q.push(b);
                }
                cout << "Case #" << test << ": " << b << " " << a << endl;
        }
        return 0;
}