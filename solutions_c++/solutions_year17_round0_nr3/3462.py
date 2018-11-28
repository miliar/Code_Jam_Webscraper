#include<bits/stdc++.h>
using namespace std;

struct Range{
    int L, R;

    Range(int _L, int _R) {
        L = _L;
        R = _R;
    }

    bool operator<(Range other) const {
        if (other.R - other.L + 1 != R - L + 1)
            return (R - L + 1 < other.R - other.L + 1);
        else
            return L > other.L;
    }
};

int T, N, K, who[1000003], last;

int main() {
    cin >> T;
    for (int cases = 1; cases <= T; cases++) {
        cin >> N >> K;

        memset(who, 0, sizeof(who));

        priority_queue<Range> pq;
        pq.push(Range(1, N));

        who[0] = who[N + 1] = 1;
        for (int current = 1; current <= K; current++) {
            Range range = pq.top(); pq.pop();
            int l = range.L, r = range.R;

            last = l + (r - l)/2;
            who[last] = 1;

            pq.push(Range(l, last - 1));
            pq.push(Range(last + 1, r));

        }

        int Ls, Rs;
        for (int i = last - 1; i >= 0; i--) {
            if (who[i] != 0) {
                Ls = last - i - 1;
                break;
            }
        }

        for (int i = last + 1; i <= N + 1; i++) {
            if (who[i] != 0) {
                Rs = i - last - 1;
                break;
            }
        }

        cout << "Case #" << cases << ": " << max(Ls, Rs) << " " << min(Ls, Rs) << endl;
    }
}
