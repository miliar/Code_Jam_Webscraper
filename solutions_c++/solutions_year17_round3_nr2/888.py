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
using Pi = pair<int,int>;

const int day = 1440;
int freeC[day];
int freeJ[day];
int baby[day];

void solve()
{
    int Ac, Aj;
    cin >> Ac >> Aj;
    for(int i = 0; i < day; i++)
    {
        freeC[i] = freeJ[i] = 1;
    }
    for(int i = 0; i < Ac+Aj; i++)
    {
        int a,b;
        cin >> a >> b;
        if(i < Ac)
            debug("C", a,b);
        else
            debug("J",a,b);
        for(int m = a; m < b; m++)
        {
            if(i < Ac)
                freeC[m] = 0;
            else
                freeJ[m] = 0;
        }
    }

    for(int swap1 = 0; swap1 < day/2; swap1++)
    {
        int goodC = 1; int goodJ = 1;
        int swap2 = swap1+day/2;
        for(int m = 0; m < day; m++)
        {
            if(m < swap1 || m >= swap2)
            {
                goodC = goodC && freeC[m];
                goodJ = goodJ && freeJ[m];
            }
            else
            {
                goodC = goodC && freeJ[m];
                goodJ = goodJ && freeC[m];
            }
        }

        if(goodC || goodJ)
        {
            debug(swap1, swap2, goodC, goodJ);
            cout << 2;
            return;
        }
    }
    cout << 4;

}

int main()
{
    cout.precision(10);
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
