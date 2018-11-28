#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARINGS
#define _USE_MATH_DEFINES

#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;

const int INF = (int)(1e9 + 1337);
const int64 LINF = (int64)(4e18);
const double EPS = (double)(1e-11);
#define sq(x) ((x)*(x))
#define FAIL() ((*(int*)(0))++)

struct part
{
    int64 len;
    int64 l, r;
    int64 ctr;
    part() {}
    part(int64 len, int64 ctr) : len(len), ctr(ctr)
    {
        l = len >> 1;
        r = len - l - 1;
        if(l > r)
            swap(l, r);
    }
};

int64 n, k;
map<int64, int64> q;

void solve()
{
    q.clear();
    cin >> n >> k;
    part last;
    q[n] = 1;
    int64 cur = 0;
    while(cur < k)
    {
        auto it = q.rbegin();
        last = part(it->first, it->second);
        q.erase(last.len);
        cur += last.ctr;
        if(last.l)
            q[last.l] += last.ctr;
        if(last.r)
            q[last.r] += last.ctr;
    }
    cout << last.r << ' ' << last.l;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int ts;
    cin >> ts;
    for(int i = 1; i <= ts; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
    }
    return 0;
}

