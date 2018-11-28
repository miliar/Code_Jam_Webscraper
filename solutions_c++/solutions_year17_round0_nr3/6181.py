#include <iostream>
#include <queue>

using namespace std;

const int INF = 0x3f3f3f3f;

struct ST {
    int l, r;

    ST(int x, int y) {
        l = x;
        r = y;
    }

    bool operator < (const ST &oth) const{
        return ((r-l) < (oth.r-oth.l)) || ((r-l) == (oth.r-oth.l) && l > oth.l);
    }
};

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n, k, ansl, ansr;
        cin >> n >> k;
        priority_queue<ST> pq;
        pq.push(ST(0, n+1));
        for (int i = 0; i < k; ++i) {
            ST t = pq.top(); pq.pop();
            int x = (t.r+t.l) >> 1;
            if (x > t.l + 1)
                pq.push(ST(t.l, x));
            if (x < t.r - 1)
                pq.push(ST(x, t.r));
            ansl = x-1-t.l;
            ansr = t.r-x-1;
        }      
        cout << "Case #" << t << ": ";
        cout << max(ansl, ansr) << " " << min(ansr, ansl) << endl;
    }
    return 0;
}