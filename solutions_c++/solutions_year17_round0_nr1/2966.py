#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <utility>
using namespace std;

#define fi(i,a,b) for(int i=(a);i<(b); ++i)
#define fd(i,a,b) for(int i=(a);i>(b); --i)
#define fie(i,a,b) for(int i=(a);i<=(b); ++i)
#define fde(i,a,b) for(int i=(a);i>=(b); --i)
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define all(x) x.begin(), x.end()
#define rall(s) (s).rbegin(),(s).rend()
#define C(u) memset((u),0,sizeof((u)))
#define x first
#define y second
#define inf 1000000000
typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi > vvi;
typedef pair<int, int> pii;

#define INP_FILE "A-large.in"
#define OUT_FILE "output.txt"

int main()
{
    freopen(INP_FILE, "r", stdin);
    freopen(OUT_FILE, "w", stdout);
    char sum = '+' + '-';
    int tstCnt; cin >> tstCnt;
    for (int tst = 1; tst <= tstCnt; tst++)
    {
        string s; int k; cin >> s >> k;
        int ans = 0;
        fi(i, 0, s.size() - k + 1) if (s[i] == '-') {
            fi(j, i, i + k) s[j] = sum - s[j];
            ++ans;
        }
        bool good = true;
        fi(i, s.size() - k + 1, s.size()) good &= s[i] == '+';
        if (good) {
            printf("Case #%d: %d\n", tst, ans);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n", tst);
        }
        //printf("Case #%d: ",tst);
    }

    return 0;
}