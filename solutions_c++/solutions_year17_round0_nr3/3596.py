#include <iostream>
#include <queue>

using namespace std;

struct seg {
    int l, r;
    bool operator <(const seg& other) const {
        int score = (r-l+1);
        int oscore = (other.r-other.l+1);
        if(score != oscore) {
            return score < oscore;
        } else {
            return l > other.l;
        }
    }
};

int T, N, K;
int main() {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> N >> K;
        priority_queue<seg> q;
        q.push({0, N-1});
        int minA, maxA;
        for(int i = 0; i < K; i++) {
            auto nex = q.top(); q.pop();
            int spl = (nex.r + nex.l)/2;
            //cerr << "Chose " << nex.l << " " << nex.r << "\n";
            //cerr << "put someone at " << spl << "\n";
            q.push({nex.l, spl-1});
            q.push({spl+1, nex.r});
            int lDist = spl - nex.l;
            int rDist = nex.r - spl;
            minA = min(lDist, rDist);
            maxA = max(lDist, rDist);
        }
        cout << "Case #" << t << ": " << maxA << " " << minA << "\n";
    }
}
