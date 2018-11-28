//// ngmq

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstdlib>
// #include <climits>
// #include <functional>
// #include <ctime>
#include <cmath>
#include <bitset>
// #include <utility>
#include <complex>
#include<fstream>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define inf (1e9 + 1e9)
#define linf 1e18
#define BASE 1000000
#define EPS 1e-10
#define PI acos(-1)
#define pii pair<int,int>
#define vi vector<int>
#define fi first
#define se second
#define ALL(x) (x).begin(), (x).end()
#define ms(x,val) memset(x, val, sizeof(x))
#define pb(x) push_back(x)
#define make_unique(x) sort(ALL(x)) ; x.erase( unique(ALL(x)), x.end()) ;
#define dbg(x) do { cout << #x << " = " << x << endl; } while(0)
#define mp(x, y) make_pair(x, y)

/*** IMPLEMENTATION ***/
bool exitInput = false;
int ntest = 1, itest = 1 ;

const int dx[4] =
{
    1, 0, -1, 0
};
const int dy[4] =
{
    0, 1, 0, -1
};
// const int dx[8] = {-2, -1, -1, +0, +0, +1, +1, +2};
// const int dy[8] = {+0, -1, +1, -2, +2, -1, +1, +0};

/** Knight Move **/
// const int dx[8] = {+1, +2, +2, +1, -1, -2, -2, -1};
// const int dy[8] = {+2, +1, -1, -2, -2, -1, +1, +2};

const char * directions[4] =
{
    "NE", "SE", "Sw", "Nw"
};

const ll Mod = 1000000007LL;
const int maxn = 200000 + 5;
const int maxv = 100000 + 5;
const int maxe = 1000011 + 5;

int n, K;
double a[55], cap;

int main()
{
#ifdef HOME
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
#endif
    int i, j, k;

    cin >> ntest;

    for(itest = 1; itest <= ntest; ++itest)
    {
        cin >> n >> K;
        cin >> cap;
        for(i = 0; i < n; ++i)
        {
            cin >> a[i];
            //cout << a[i] << endl;
        }
        sort(a, a + n);
        while(cap > 0 && abs(cap) > EPS)
        {
            int cnt = 0;
            for(i = 0; i < n; ++i)
            {
                if(abs(a[i] - a[0]) < EPS)
                {
                    ++cnt;
                }
                else break;
            }
            double max_add = cap / cnt;

//            cout << "cap = " << cap << endl;
//            cout << "cnt = " << cnt << "; max_add = " << max_add << endl;
//            for(i = 0; i < n; ++i)
//            {
//                cout << a[i] << endl;
//            }
            if(cnt == n)
            {
                for(i = 0; i < n; ++i)
                {
                    a[i] += max_add;
                    if(a[i] > 1)
                    {
                        a[i] = 1;
                    }
                }
                cap = 0;
                break;
            }
            else
            {
                double next_val = a[cnt];
                double max_add2 = next_val - a[0];
                if(max_add > max_add2)
                {
                    max_add = max_add2;
                }

                for(i = 0; i < cnt; ++i)
                {
                    a[i] += max_add;
                }
                cap -= max_add * cnt;
            }
        }
        double res = 1.0;
        for(i = 0; i < n; ++i)
        {
            res = res * a[i];
        }
        printf("Case #%d: %.10f\n", itest, res);
    }

    return 0;
}

