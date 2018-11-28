#include <bits/stdc++.h>
using namespace std;

#define ifthen(x, y, z) (x ? y: z)
#define mp make_pair
#define mt make_tuple

const int INF = 1e9 + 1;
const double pi = acos(-1);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.precision(20);
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        unsigned long long N, K;
        cin >> N >> K;
        cout << "Case #" << i+1 << ": ";
        priority_queue<unsigned long long> pq;
        pq.push(N);
        for (unsigned long long i = 0; i < K-1; ++i) {
            auto t = pq.top();
            pq.pop();
            pq.push(t/2);
            pq.push(ifthen(t%2, t/2, t/2-1));
        }
        auto t = pq.top();
        cout << t/2 << ' ';
        cout << ifthen(t%2, t/2, t/2-1);
        cout << '\n';
    }
    return 0;
}
