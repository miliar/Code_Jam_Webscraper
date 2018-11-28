#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

int T, N, P;
int occ[4];

int go()
{
    int ret = occ[0];
    if (P == 2)
        ret += (occ[1] + 1)/2; //1 + 1
    else if (P == 3)
    {
        int a = min(occ[1], occ[2]); //1 + 2
        ret += a;
        occ[1] -= a;
        occ[2] -= a;
        ret += occ[1]/3;
        ret += occ[2]/3;
        if (occ[1] % 3 != 0 || occ[2] % 3 != 0)
            ret++;
    }
    else
    {
        int a = min(occ[1], occ[3]); //1 + 3
        ret += a;
        occ[1] -= a;
        occ[3] -= a;
        int left = occ[1] + occ[3]; //only one is left
        int best = 0;
        for (int i = 0; i <= occ[2]; i += 2)
        {
            int cur = i/2;
            int rem2 = occ[2] - i;
            int use = min(left/2, rem2);
            cur += use;
            rem2 -= use;
            int temp = left - 2*use;
            cur += temp/4;
            cur += rem2/2;
            if (temp % 4 != 0 || rem2 % 2 != 0)
                cur++;
            best = max(best, cur);
        }
        ret += best;
    }
    return ret;
}

int main()
{
	ios::sync_with_stdio(0);

    freopen("A.in", "r", stdin);
    freopen("Aout.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> P;
        memset(occ, 0, sizeof(occ));
        for (int i = 0, a; i < N; i++)
        {
            cin >> a;
            occ[a % P]++;
        }
        
        cout << "Case #" << t << ": " << go() << "\n";
    }

	return 0;
}
