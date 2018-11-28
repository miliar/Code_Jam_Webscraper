#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iomanip>

#define FOR(i, s, n) for (int i = (s); i < (n); ++i)
#define FOR2(i, s, n) for (int i = (s); i <= (n); ++i)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

typedef long long ll;
typedef vector<int> vi;

int D, N;

struct Horse{
    int K;
    int S;
    double rtime;

    bool operator < (const Horse &o) const {
        return K < o.K;
    }
};

Horse horses[1500];

void solve()
{    
    cin >> D >> N;
    REP(i, N) {
        cin >> horses[i].K >> horses[i].S;
    } 

    sort(horses, horses+N);

    double max_time = double(D - horses[N-1].K) / double(horses[N-1].S);

    for (int i = N-1; i >= 0; --i) {
        double time_to_dest = double(D - horses[i].K) / double(horses[i].S);
        if (time_to_dest < max_time) time_to_dest = max_time;
        horses[i].rtime = time_to_dest;
        max_time = max(max_time, time_to_dest);
    }

    cout << fixed << setprecision(7) << D / max_time << endl;
}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}