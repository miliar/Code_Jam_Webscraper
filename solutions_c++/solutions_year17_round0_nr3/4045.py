#include <vector>
#include <iostream>
#include <queue>

using namespace std;

class Interval {
private:
    long left;
    long right;
public:
    long getLeft() const { return left; }
    long getRight() const { return right; }
    long getMin() const { return left > right ? right : left; }
    long getMax() const { return left > right ? left : right; }
    Interval(long size) {
        left = right = (size - 1) / 2;
        if (size % 2 == 0) {
            right++;
        }
    }
};

struct compareInterval
{
    // Return true if less priority
    bool operator()(const Interval& a, const Interval& b)
    {
        if (a.getMin() < b.getMin()) {
            return true;
        } else if (a.getMin() == b.getMin() &&
            a.getMax() < b.getMax()) {
            return true;
        }
        return false;
    }
};

int main(int argc, char** argv) {
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; ++t) {
        int n, k;
        cin >> n >> k;
        priority_queue<Interval, vector<Interval>, compareInterval> pQueue;
        pQueue.push(Interval(n));
        for (int i = 0; i < (k - 1); ++i) {
            Interval stall = pQueue.top();
            pQueue.pop();
            if (stall.getLeft() > 0) {
                pQueue.push(Interval(stall.getLeft()));
            }
            if (stall.getRight() > 0) {
                pQueue.push(Interval(stall.getRight()));
            }
        }
        cout << "Case #" << t << ": " << pQueue.top().getMax() << " " << pQueue.top().getMin() << endl;
    }
    return 0;
}