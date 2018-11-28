#include <iostream>
#include <algorithm>
#include <queue>

using std::priority_queue;
using std::cin;
using std::cout;
using std::min;
using std::max;

struct Interval {
    int l, r;

    int length() const {
        return r - l + 1;
    }

    int mid() {
        return (l + r) / 2;
    }

    Interval(int l, int r) : l(l), r(r) {}

    bool operator < (const Interval &b) const {
        if (this->length() != b.length()) {
            return this->length() < b.length();
        }
        return this->l > b.l;
    }
};

int main() {
    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; ++test_case) {
        int N, K;
        cin >> N >> K;
        priority_queue<Interval> q;
        q.push(Interval(1, N));
        for (int i = 1; i < K; ++i) {
            Interval top = q.top();
            q.pop();
            if (top.mid() - 1 >= top.l) {
                q.push(Interval(top.l, top.mid() - 1));
            }
            if (top.mid() + 1 <= top.r) {
                q.push(Interval(top.mid() + 1, top.r));
            }
        }
        Interval top = q.top();
        q.pop();
        int Ls = top.mid() - top.l;
        int Rs = top.r - top.mid();
        cout << "Case #" << test_case << ": " << max(Ls, Rs) << " " << min(Ls, Rs) << "\n";
    }
    return 0;
}
