#include <cstring>
#include <cmath>
#include <climits>
#include <vector>
#include <deque>
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

bool tidy(long n)
{
    string S = to_string(n);
    for(int i = 1; i < S.size(); i++)
        if(S[i] < S[i-1])
            return false;
    return true;
}

void solve()
{
    long N;
    cin >> N;
    while(!tidy(N))
    {
        long d = 1;
        while(N / d % 10 == 9)
            d *= 10;
        N -= d;
    }

    cout << N;
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

