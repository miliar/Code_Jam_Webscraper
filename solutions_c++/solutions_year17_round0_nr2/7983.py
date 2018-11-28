#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define all(x) (x).begin(), (x).end()

string solve(long long N)
{
    ostringstream ss; ss << N; string s = ss.str();
    int l = s.size();

    /*
     * 132
     * 1061
     */
    while(true)
    {
        bool found = false;
        for(int i=l-2; i>=0; --i) if(s[i] > s[i+1])
        {
            //cout << "?" << s << endl;
            s[i] --;
            for(int j = i + 1; j < l; ++ j) s[j] = '9';
            found = true;
            break;
        }
        if(! found) break;
    }

    while(s[0] == '0') s = s.substr(1);
    return s;
}

int main()
{
    int T;
    cin >> T;

    for(int kase = 1; kase <= T; ++ kase) {
        long long N;
        cin >> N;

        printf("Case #%d: ", kase);
        cout << solve(N) << endl;
    }
    return 0;
}
