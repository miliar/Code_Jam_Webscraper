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

int ratin() 
{
    int a,b;
    scanf("%d.%d", &a, &b);
    return a*10000 + b;
}
int probs[51];
double finalprobs[51];
void solve()
{
    int N,K;
    cin >> N >> K;
    int U = ratin();
    for(int n = 0; n < N; n++)
        probs[n] = ratin();
    probs[N] = 10000;

    sort(probs, probs+N);
    if(N < 10)
    {
        for(int p = 0; p < N; p++)
            cerr << probs[p] << " ";
        cerr << "\n";
    }

    int last = -1;
    while(U > 0)
    {
        for(last = 0; last < N; last++)
        {
            if(probs[last] < probs[last+1])
                break;
        }

        int diff = probs[last+1] - probs[last];
        if(diff * (last+1) < U)
        {
            U -= diff * (last+1);
            for(int u = 0; u <= last; u++)
                probs[u] = probs[last+1];
            continue;
        }
        break;
    }

    for(int p = 0; p < N; p++)
    {
        if(p <= last)
            finalprobs[p] = probs[p]/10000.0 + (double(U)/(last+1))/10000.0;
        else
            finalprobs[p] = probs[p]/10000.0;
    }
    debug("left", U, last);
    if(N < 10)
    {
        for(int p = 0; p < N; p++)
            cerr << probs[p] << " ";
        cerr << "\n";
    }
    if(N < 10 || testcase == 5)
    {
        for(int p = 0; p < N; p++)
            cerr << finalprobs[p] << " ";
        cerr << "\n";
    }



    double total = 1.0;
    for(int n = 0; n < N; n++)
    {
        total *= finalprobs[n];
    }
    cout << total;

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
