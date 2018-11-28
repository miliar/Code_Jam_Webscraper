/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <bitset>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define pll pair < ll, ll >
#define pill pair< int, pll >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define REP(i,a,n) for(int i=a;i<(int)n;i++)
#define pb push_back
#define mp make_pair
#define pi 3.14159265358979323846
typedef long long ll;
int n,k;
vector<pii> V;
long double dp[1005][1005];
long double side(long double r, long double h)
{
    return 2.0 * pi * r * h;
}
long double top(long double r)
{
    return pi * r * r;
}
long double calc(int prev, int cnt)
{
    if(prev >= n)
        return -1000000000000000;
    if(cnt == k)
        return 0;
    long double ans = dp[prev][cnt];
    if(ans != -1)
        return ans;
    ans = -1000000000000000;
    for(int i=prev+1;i<n;i++)
    {
        int remain = n - i;
        int toGet = k - cnt;
        if(remain < toGet)
            break;
        ans = max(ans, side(V[i].first, V[i].second) + calc(i, cnt+1));
    }
    dp[prev][cnt] = ans;
    return ans;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int kas = 1;
    while(t--)
    {
        cout << "Case #" << kas++ << ": ";
        cin >> n >> k;
        V.clear();
        FOR(i,n+1)
        FOR(j,k+1)
        dp[i][j] = -1;
        FOR(i,n)
        {
            int r,h;
            cin >> r >> h;
            r = -r;
            h = -h;
            V.pb(pii(r,h));
        }
        sort(V.begin(),V.end());
        FOR(i,n)
        {
            V[i].first = -V[i].first;
            V[i].second = -V[i].second;
        }
        long double ans = -1000000000000000;
        FOR(i,n)
        {
            ans = max(ans, side(V[i].first, V[i].second) + top(V[i].first) + calc(i,1.0));
        }
        cout << std::setprecision(18)<< ans << endl;
    }
    return 0;
}
