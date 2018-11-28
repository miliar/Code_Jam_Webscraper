#include <iostream>
#include <map>
#include <queue>
using namespace std;

int T;
long long N, K;
map<long long, long long> mult;
priority_queue<long long> p;

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        mult.clear();
        p = priority_queue<long long>();

        cin >> N >> K;
        p.push(N);
        mult[N] = 1;
        long long k = 0, y, z;
        while (true) {
            long long t = p.top();
            p.pop();
            long long l = (t-1)/2, r = t/2;
            if (k + mult[t] >= K) {
                y = r; z = l;
                break;
            }
            if (mult.find(l) == mult.end()) p.push(l);
            if (mult.find(r) == mult.end()) p.push(r);
            mult[l] += mult[t];
            mult[r] += mult[t];
            k += mult[t];
            mult.erase(t);
        }
        cout << "Case #" << t << ": " << y << " " << z << endl;

    }
    return 0;
}
