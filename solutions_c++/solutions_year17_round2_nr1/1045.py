#include <cstring>
#include <cmath>
#include <climits>
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
#include <cstdio>
using namespace std;
const long linf = 1000000000000000031L;
const long inf = 1000000009;

template <typename T>
void debug(T t) { cerr << t << "\n"; }
template <typename T, typename... Args>
void debug(T t, Args... args) { cerr << t << " "; debug(args...); }

int testcase;

using PI = pair<int,int>;

PI horses[1000];
double maxSpeed[1000];
void solve()
{
    int D,N;
    cin >> D >> N;
    for(int i = 0; i < N; i++)
    {
        int K,S;
        cin >> K >> S;
        horses[i] = make_pair(K,S);
    }
    debug("DN",D,N);

    sort(horses, horses+N);
    double maxS = 1e15;
    for(int n = N-1; n >= 0; n--)
    {
        double t = (double(D) - horses[n].first) / horses[n].second;
        maxSpeed[n] = double(D) / t;
        maxS = min(maxSpeed[n], maxS);
        debug(horses[n].first, horses[n].second, maxSpeed[n]);
    }

    debug(maxS);
    printf("%.10lf", maxS);

}

int main()
{
    cout.precision(10);
    cerr.precision(10);
    int T;
    cin >> T;
    for(testcase = 1; testcase <= T; testcase++)
    {
        debug("### ", testcase, " ###");
        cout << "Case #" << testcase << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
