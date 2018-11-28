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
using namespace std;
const long inf = 1000000021L*1000000021L;
int testcase;

map<long,long,std::greater<long>> runs;
void add(long n, long times)
{
    auto it = runs.find(n);
    if(it == runs.end())
        runs[n] = times;
    else
        runs[n] = runs[n] + times;
}

void solve()
{
    runs.clear();
    long N, K;
    cin >> N >> K;

    runs[N] = 1;
    while(K > 0)
    {
        auto it = *(runs.begin());
        runs.erase(runs.begin());

        long mine = it.first;
        long L,R;
        if(mine % 2 == 1)
        {
            L = R = mine/2;
        }
        else
        {
            L = mine/2;
            R = mine/2 - 1;
        }
        add(L, it.second);
        add(R, it.second);
        K -= it.second;
        if(K <= 0)
        {
            cout << L << " " << R;
        }
    }
}

int main()
{
    cout.precision(10);
    int T;
    cin >> T;
    for(testcase = 1; testcase <= T; testcase++)
    {
        cout << "Case #" << testcase << ": ";
        solve();
        cout << endl;
    }
    return 0;
}

