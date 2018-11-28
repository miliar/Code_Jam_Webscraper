#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

void solve(int);

struct gap {
    int l, r;

    bool operator<(const gap& other) const
    {
        if (this->r - this->l != other.r - other.l) {
            return this->r - this->l < other.r - other.l;
        } else {
            return this->l > other.l;
        }
    }
};

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        solve(i + 1);
    }
}

void solve(int t)
{
    priority_queue<gap> gaps;
    int n, m;
    cin >> n >> m;
    gaps.push({ 1, n });
    int mincons, maxcons;

    for (int i = 0; i < m; i++) {
        gap topgap = gaps.top();
        gaps.pop();
        int width = topgap.r + 1 - topgap.l;
        if (width == 2) {
            gaps.push({ topgap.l + 1, topgap.r });
            mincons = 0;
            maxcons = 1;
        } else {
            gaps.push({ topgap.l, (topgap.l + topgap.r) / 2 - 1 });
            gaps.push({ (topgap.l + topgap.r) / 2 + 1, topgap.r });
            mincons = min(width / 2 - (width % 2 == 0 ? 1 : 0), width / 2);
            maxcons = max(width / 2 - (width % 2 == 0 ? 1 : 0), width / 2);
        }
    }

    cout << "Case #" << t << ": " << maxcons << " " << mincons << endl;
}