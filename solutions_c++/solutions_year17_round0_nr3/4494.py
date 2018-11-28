#include <iostream>
#include <queue>
#include <vector>

#define REP(i,a,b) for(int i=int(a);i<int(b);i++)

using namespace std;

typedef long long int lli;

struct Data {
    int m, M;
    Data(int m, int M) : m(m), M(M) {}
};

bool operator<(Data d1, Data d2) {
    if (d1.m != d2.m) return (d1.m < d2.m);
    return (d1.M < d2.M);
}

int main () {
    int T;
    cin >> T;
    REP (_, 0, T) {
        int N, K;
        cin >> N >> K;
        priority_queue<Data, vector<Data>> pq;
        pq.emplace((N - 1) / 2, N / 2);
        REP (i, 0, K - 1) {
            auto t = pq.top();
            pq.pop();
            pq.emplace((t.m - 1) / 2, t.m / 2);
            pq.emplace((t.M - 1) / 2, t.M / 2);
        }
        cout << "Case #" << _ + 1 << ": " << pq.top().M << " " << pq.top().m << endl;
    }

    return 0;
}
