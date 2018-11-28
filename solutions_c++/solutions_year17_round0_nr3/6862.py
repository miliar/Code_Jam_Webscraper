#include <bits/stdc++.h>

template<typename T> T gcd(T a, T b) {
    if(!b) return a;
    return gcd(b, a % b);
}
template<typename T> T lcm(T a, T b) {
    return a * b / gcd(a, b);
}

template<typename T> void chmin(T& a, T b) { a = (a > b) ? b : a; }
template<typename T> void chmax(T& a, T b) { a = (a < b) ? b : a; }
int in() { int x; scanf("%d", &x); return x; }

using namespace std;

typedef long long Int;
typedef unsigned long long uInt;
typedef unsigned uint;

int N, K, T;

int main(void) {

    cin >> T;

    for(int t=1; t<=T; t++) {
        cin >> N >> K;

        priority_queue<int, vector<int> , greater<int> > q;
        q.push(-N);
        for(int idx = 1; idx < K; idx++) {
            int n = q.top();
            q.pop();
            q.push((n / 2));
            q.push((n / 2) + (n % 2 == 0));
        }

        int ans = -q.top();
        cout << "Case #" << t << ": ";
        cout << (ans / 2) << " " << (ans / 2) - (ans % 2 == 0) << "\n";
    }

    return 0;
}
