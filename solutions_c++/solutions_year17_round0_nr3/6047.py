#include <iostream>
#include <queue>
using namespace std;

struct Neighbor {
    int left;
    int right;
    Neighbor(int left, int right)
        : left(left), right(right)
    {}
    int distance() const {
        return right - left;
    }
    bool operator<(const Neighbor& rhs) const {
        if (distance() != rhs.distance())
            return distance() < rhs.distance();
        return left > rhs.left;
    }
};

int main() {
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++cas) {
        int n, k;
        cin >> n >> k;
        priority_queue<Neighbor> q;
        q.push(Neighbor(0, n + 1));
        int ma, mi;
        for (int i = 0; i < k; ++i) {
            Neighbor top = q.top();
            q.pop();
            int mid = (top.left + top.right) / 2;
            if (i == k - 1) {
                ma = top.right - mid - 1;
                mi = mid - top.left - 1;
            }
            q.push(Neighbor(top.left, mid));
            q.push(Neighbor(mid, top.right));
        }
        cout << "Case #" << cas << ": " << ma << ' ' << mi << '\n';
    }
}
