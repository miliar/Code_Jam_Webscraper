// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 101;
const int INF = 0x3f3f3f3f;
const bool debug = true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector < int >VI;
typedef vector < string > VS;
typedef vector < VI > VVI;
typedef pair < int, int >PII;
typedef pair < int, PII > PIII;

int memo[M][M][M][M];

int B, D;
int origHd;

int calc(int Hd, int Ad, int Hk, int Ak)
{
    int &ans = memo[Hd][Ad][Hk][Ak];

    if (ans != INF)
	return ans;
    if (Hk == 0) {
	return ans = 0;
    }
    if (Hd == 0) {
	return ans = INF + 1;
    }

    ans = INF + 1;
    // Attack
    ans = min(ans, 1 + calc(max(0, Hd - Ak), Ad, max(0, Hk - Ad), Ak));
    // Buff
    if (B > 0 ) ans = min(ans, 1 + calc(max(0, Hd - Ak), min(100, Ad + B), Hk, Ak));
    // Cure
    ans = min(ans, 1 + calc(max(0, origHd - Ak), Ad, Hk, Ak));
    // Debuff
    if (D >0) {
        int newAk = max(0, Ak - D);
        ans = min(ans, 1 + calc(max(0, Hd - newAk), Ad, Hk, newAk));
    }

    return ans;

}

int main()
{
    int tc;
    cin >> tc;

    for (int t = 1; t <= tc; ++t) {

	int Hd, Ad, Hk, Ak;

	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

	origHd = Hd;

	SET(memo, INF);
	int ans = calc(Hd, Ad, Hk, Ak);

	cout << "Case #" << t << ": ";
	if (ans < INF) {
	    cout << ans;
	} else {
	    cout << "IMPOSSIBLE";
	}
	cout << "\n";
    }
    return 0;
}
