#include <cstring>
#include <cmath>
#include <climits>
#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <functional>
#include <utility>
using namespace std;
const long inf = 1000000000000000031L;
const double dinf = INFINITY;

template <typename T>
void debug(T t) { cerr << t << "\n"; }
template <typename T, typename... Args>
void debug(T t, Args... args) { cerr << t << " "; debug(args...); }

int testcase;

using Pi = pair<long,long>;

void solve()
{
    int N,K;
    cin >> N >> K;
    deque<Pi> sizes(N+1);
    deque<long> contr(N);
    for(int n = 0; n < N; n++)
    {
        long H,R;
        cin >> R >> H;
        sizes[n] = make_pair(R,H);
    }
    sizes[N] = make_pair(0,0);

    sort(sizes.begin(),sizes.begin()+N, [](Pi a, Pi b) {
            if(a.first == b.first)
                return a.second > b.second;
            return a.first > b.first;
            });

    for(int n = 0; n < N; n++)
        debug(sizes[n].first, sizes[n].second);
    for(int n = 0; n < N; n++)
    {
        long h = sizes[n].second, r = sizes[n].first, rn = sizes[n+1].first;
        contr[n] = 2*h*r + r*r - rn*rn;
    }
    for(int n = 0; n < N; n++)
        debug(contr[n]);

    int taken = 0;
    while(taken < N - K)
    {
        int best = 0;
        long worstc = inf;
        for(int n = 0; n < N - taken; n++)
        {
            long diff = contr[n];
            if(n != 0)
            {
                long r1 = sizes[n-1].first;
                long r2 = sizes[n].first;
                long r3 = sizes[n+1].first;
                diff -= (r1*r1 - r3*r3) - (r1*r1 - r2*r2);
            }
            if(diff < worstc)
            {
                worstc = diff;
                best = n;
            }
        }
        int n = best;
        debug("took", best, worstc, sizes[n].first, sizes[n].second);
        sizes.erase(sizes.begin()+n);
        contr.erase(contr.begin()+n);
        if(n != 0)
        {
            long h = sizes[n-1].second, r = sizes[n-1].first, rn = sizes[n].first;
            contr[n-1] = 2*h*r + r*r - rn*rn;
        }
        taken += 1;
    }
    for(int n = 0; n < K; n++)
        debug(contr[n]);
    long total = 0;
    for(int n = 0; n < K; n++)
        total += contr[n];
    cout << M_PI * total;
}

int main()
{
    cout.precision(10);
    fixed(cout);
    cerr.precision(10);
    int T;
    cin >> T;
    for(testcase = 1; testcase <= T; testcase++)
    {
        cout << "Case #" << testcase << ": ";
        debug("### ", testcase, " ###");
        solve();
        cout << endl;
    }
    return 0;
}
