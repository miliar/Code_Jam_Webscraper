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
const long linf = 1000000000000000031L;
const long inf = 1000000009;

template <typename T>
void debug(T t) { cerr << t << "\n"; }
template <typename T, typename... Args>
void debug(T t, Args... args) { cerr << t << " "; debug(args...); }

int testcase;

int stalls[1000];
using Pa = pair<int,string>;
void solve()
{
    int N,A,AB,B,BC,C,AC;
    cin >> N >> A >> AB >> B >> BC >> C >> AC;
    int i = 0;

    string BOs = "B";
    string RGs = "R";
    string YVs = "Y";
    debug(AB,BC,AC);

    if(AB > 0 && AB + 1 > C)
    {
        if(AB == C && AB + C == N)
        {
            for(int n = 0; n < N; n += 2)
                cout << "BO";
            return;
        }
        cout << "IMPOSSIBLE";
        cerr << "ne C";
        return;
    }
    if(BC > 0 && BC + 1 > A)
    {
        if(BC == A && BC + A == N)
        {
            for(int n = 0; n < N; n += 2)
                cout << "RG";
            return;
        }
        if(testcase == 8)
            cerr << BC << A;
         cout << "IMPOSSIBLE";
        cerr << "ne A";
        return;
    }
    if(AC > 0 && AC + 1 > B)
    {
        if(AC == B && AC + B == N)
        {
            for(int n = 0; n < N; n += 2)
                cout << "YV";
            return;
        }
         cout << "IMPOSSIBLE";
        cerr << "ne B";
        return;
    }
    if(AB > 0)
        N -= (AB*2);
    if(BC > 0)
        N -= (BC*2);
    if(AC > 0)
        N -= (AC*2);
    while(AB > 0)
    {
        BOs += "OB";
        AB--;
        C--;
    }
    while(BC > 0)
    {
        RGs += "GR";
        BC--;
        A--;
    }
    while(AC > 0)
    {
        YVs += "VY";
        AC--;
        B--;
    }

    int a = A;// + AB + AC;
    int b = B;// + AB + BC;
    int c = C;// + BC + AC;
    //debug(a,b,c);

    if(a > N/2 || b > N/2 || c > N/2)
    {
        cout << "IMPOSSIBLE";
        cerr << "too many primary";
        return;
    }
    vector<pair<int,string>> colors = {{a,RGs}, {b,YVs}, {c,BOs}};
    map<int,string> cmap;
    sort(colors.begin(), colors.end(), [](const Pa &p1, const Pa &p2){return p1.first > p2.first;});
    int x = colors[0].first; cmap[0] = colors[0].second;
    int y = colors[1].first; cmap[1] = colors[1].second;
    int z = colors[2].first; cmap[2] = colors[2].second;
    //debug(x,y,z);


    while(x > 0 && y > 0 && z > 0)
    {
        if(x == y+z)
        {
            while(y > 0)
            {
                stalls[i++] = 0; x--;
                stalls[i++] = 1; y--;
            }
            while(z > 0)
            {
                stalls[i++] = 0; x--;
                stalls[i++] = 2; z--;
            }
        }
        else
        {
            stalls[i++] = 0; x--; 
            stalls[i++] = 1; y--; 
            stalls[i++] = 2; z--; 
        }

    }
    //debug(x,y,z,i);
    if(x > y)
    {
        if(y == 0)
        {
            debug("panicy",x,y,z);
            for(int n = 0; n < N; n++)
                cerr << cmap[stalls[n]];
            cerr << "\n";
            return;
        }
        stalls[i-1] = 0; x--;
        stalls[i] = 1; y--;
        stalls[N-1] = 2;
        i++;
    }
    //debug(x,y,z,i);
    while(x > 0 && y > 0)
    {
        stalls[i++] = 0; x--; 
        stalls[i++] = 1; y--; 
    }
    //debug(x,y,z,i);
    if(x > 0)
    {
        stalls[i++] = 0; x--;
    }
    if(x + y + z > 0)
    {
        debug("panic",x,y,z);
        for(int n = 0; n < N; n++)
            cerr << cmap[stalls[n]];
        cerr << "\n";
        return;
    }

    for(int n = 0; n < N; n++)
    {
        cout << cmap[stalls[n]];
        if(cmap[stalls[n]].size() > 1)
        {
            cmap[stalls[n]] = string(1, cmap[stalls[n]][0]);
        }
    }

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
